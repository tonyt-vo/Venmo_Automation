from setup import chromedriver_path, venmo_url, username, password, people_charged
import os, time, pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = os.path.normpath(chromedriver_path) #Path of ChromeDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'credentials_enable_service': False}) # Ignore saving password
browser = webdriver.Chrome(executable_path=path,chrome_options=options) # Create the Chrome browser
browser.get(venmo_url) # Go to Venmo URL to login.


if os.path.isfile('cookies.pkl'):

    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    # Find the Username box and insert username
    username_location = browser.find_element_by_name("phoneEmailUsername")
    username_location.send_keys(username)

    # Find the Password box and insert password
    password_location = browser.find_element_by_name("password")
    password_location.send_keys(password)

    # Login
    send_button = browser.find_element_by_tag_name("form").submit()
    time.sleep(5)
    # Go through each recipient and charge them.
    for person in people_charged:
        charge = browser.find_element_by_id("onebox_charge_toggle").click() # Select Charge
        # Enter names of people being charged.
        recipient_location = browser.find_element_by_name("onebox_recipient_typeahead")
        recipient_location.send_keys(person + Keys.ENTER)
        time.sleep(2)

        # Enter price and notes.
        note_area = browser.find_element_by_id("onebox_details")
        price = "00.01"
        message = " testing"
        note_area.send_keys(price + message)
        time.sleep(2)

        # Locate the charge button and submit.
        final_submit = browser.find_element_by_xpath("//*[@id=\"onebox_send_button\"]").click()
        time.sleep(15) # Wait  20 seconds before next iteration.

else: # First time logging in will allow us to gather cookies to reuse in future scheduling tasks.
    print("Please Login for the first time")
    time.sleep(15) # Allow for 60 seconds to login and do 2 step verification.
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))




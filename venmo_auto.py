from setup import chromedriver_path, venmo_url, username, password, people_charged, spam_email, spam_password, notify_email
import os, time, pickle, smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PATH = os.path.normpath(chromedriver_path) #Path of ChromeDriver
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_experimental_option('prefs', {'credentials_enable_service': False}) # Ignore saving password
BROWSER = webdriver.Chrome(executable_path=PATH,chrome_options=OPTIONS) # Create the Chrome browser
BROWSER.get(venmo_url) # Go to Venmo URL to login.
NOTIFY = True


def charge():
    if os.path.isfile('cookies.pkl'):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            BROWSER.add_cookie(cookie)
        # Find the Username box and insert username
        username_location = BROWSER.find_element_by_name("phoneEmailUsername")
        username_location.send_keys(username)

        # Find the Password box and insert password
        password_location = BROWSER.find_element_by_name("password")
        password_location.send_keys(password)

        # Login
        send_button = BROWSER.find_element_by_tag_name("form").submit()
        time.sleep(5)
        # Go through each recipient and charge them.
        for person in people_charged:
            charge = BROWSER.find_element_by_id("onebox_charge_toggle").click() # Select Charge
            # Enter names of people being charged.
            recipient_location = BROWSER.find_element_by_name("onebox_recipient_typeahead")
            recipient_location.send_keys(person + Keys.ENTER)
            time.sleep(2)

            # Enter price and notes.
            note_area = BROWSER.find_element_by_id("onebox_details")
            price = "00.01"
            message = " testing"
            note_area.send_keys(price + message)
            time.sleep(2)

            # Locate the charge button and submit.
            final_submit = BROWSER.find_element_by_xpath("//*[@id=\"onebox_send_button\"]").click()
            if NOTIFY:
                subject = "Venmo Automatic Request"
                body = "Hello, \n Payment has been requested to " + person
                send_email(spam_email,spam_password,notify_email,subject,body)
            time.sleep(15) # Wait  20 seconds before next iteration.

    else: # First time logging in will allow us to gather cookies to reuse in future scheduling tasks.
        print("Please Login for the first time")
        time.sleep(60) # Allow for 60 seconds to login and do 2 step verification.
        pickle.dump(BROWSER.get_cookies(), open("cookies.pkl", "wb"))


def send_email(login_email, login_password, to_address, subject, body):
    """
    :param to_address:
    :param subject:
    :param body:
    :return:
    """
    msg = MIMEMultipart()
    msg['From'] = login_email
    msg['To'] = to_address
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login_email, login_password)
    text = msg.as_string()
    server.sendmail(login_email, to_address, text)
    server.quit()
    print("message sent")



charge()
# Venmo Automation
Created by Tony Vo
Date of initial commit: May 13th, 2017

## Short Description
The purpose of this project was to automate Venmo charges using a webscrapper implementation.

# Languages Used
1. Python 3.6

## Library's Used
1. Selenium library (Used for opening and browsing the website.)
2. pickle module (Used for extracting cookies to use for future automation.)

## Files Used
1. setup.py
   This file contains information to use for the automation.
   The user stores Venmo username and password here to allow application to login.
   In addition, the list "people_charged" will contain the usernames' of all those who are to be charged.
   chromedriver_path: This is needed by Selenium in order open up Chrome. Alternatively, Selenium can be used through different browsers, but this application has not yet supported.
   venmo_url: This is the url where Selenium loads into when first opening the application.

2. venmo_auto.py
   This file is the meat of the program. A breakdown of how the program work is as follows:
   The application takes information from setup.py and loads up the Venmo url via Chrome.
   If it is the first time user has ran the app, they will have to login manually which the program will save the cookies used for future logins.
   Upon setup, the application will then login using the credentials. The final step will be charging people a specified amount and leaving a message.

# Set-up guide:
1. Download the necessary files
2. Update setup.py to include your information.
3. Run venmo_auto.py
3a. If it is your first time setting up. Login and use 2-step verification.
3b. After this, run again.

## Implementation Ideas:
- [ ] Email notifications upon charges.
- [ ] Scheduling: Allowing the program to run a certain time of the month.
- [ ] Enter all user's in one charge rather than separate charges.
- [ ] User specified prices and notes.
- [ ] Remind users about payments via Venmo's remind button.

## Notes about project:
This project served as an intro into the idea of webscrapping for me. It was sparked when my friends and I wanted to manage rent money for our college house.
This task was simple but it was fun exploring the Selenium library. I hope to further this project and incorporate into Voma_Notifications which my friends and I plan to use for the school year of 2017-2018.

Below are a few of my experiences going through this project.
### Things learned:
* Read the documents
    * The documents are always filled with examples and tips on getting started. This is a central place to look for the information wanted rather than googling the whole web for a specific aspect you need.
* Selenium
   * A brief intro into this library made me realize how powerful it really is. Being able to connect online amazed me and as for a beginning programmer like me, I found this project really rewarding.
* Cookies
   * At one point in the project, I was stuck because Selenium would always use the default profile when opening Chrome. 


### Problems encountered:
* Approach
    * At first, I originally planned to use Venmo's API in order to implement this project. However with my current knowledge, I did not know how to start. Selenium seemed like a great option and that is why I chose it for this project. In the future, I hope learn HTTP GET and POST requests and more about how the web works. For the time being though, I am just happy to make something that is functional.
* Cookies
    * I briefly mentioned this in the section above but during the project I was stuck to how to login using options from a remembered user. This caused the program to be stuck at the 2-step verification all the time. After researching online about this problem, I realized that we could create a cookie file and save it so for future uses, it will use those cookies as part of the profile. Although this isn't ideal, I'm glad it functions.
* HTML
    * When trying to tell Selenium where to click and fill, I had a hard time trying to find the elements needed from the HTML. I have very limited knowledge on HTML and trying to go through the code was like a giant puzzle.   

### Moving foward:
* Webscrapping is cool. I definately want to further explore different web projects and automate tasks.
* Part of the learning experience for me was just getting out there and making something. Yes, it may not be impressive but it's exposure. Learning is a chain reaction. When trying to implement one thing, it leads to exploring different libraries, material and coding methods. The more I keep at it, the more I'll keep learning. 

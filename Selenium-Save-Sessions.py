# Import Modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json,os

# Open Chrome Browser
driverPath = ChromeDriverManager().install()
driver = webdriver.Chrome(executable_path=driverPath)


def saveCookies(driver):
    # Get and store cookies after login
    cookies = driver.get_cookies()

    # Store cookies in a file
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print('New Cookies saved successfully')


def loadCookies():
    # Check if cookies file exists
    if 'cookies.json' in os.listdir():

        # Load cookies to a vaiable from a file
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)

        # Set stored cookies to maintain the session
        for cookie in cookies:
            driver.add_cookie(cookie)
    else:
        print('No cookies file found')
    
    driver.refresh() # Refresh Browser after login




loginURL = 'https://realpython.com/account/login/'
driver.get(loginURL)

# Load old session into the browser
loadCookies()


# sometime session expired or something wrong with session
# so every time we need to check after visit the login page
# if it's redirect to the Homepage -> we can use old session
# if it's not redirect to Homepage and stayed on login page -> we need to create new session and save new cookies



# I'm checking with if condition. if 'login' word is there in current browser URL or not
if 'login' in driver.current_url:
    # Ask for login Manually
    # Demo Account Login  User: xp4224314@gmail.com   :: Password: FN2jY4vbgPx9Uk
    print('Please Login the the website')
    print('Press Enter after successful login ...')
    input('>: ')

    # After successful login save new session cookies ot json file
    saveCookies(driver)

else:
    print('Previous session loaded')
    



'''
                Your Code here
'''


# close the browser
driver.quit()


print('Finished ...')


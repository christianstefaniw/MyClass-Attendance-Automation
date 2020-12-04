from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from attendance.credentials import get_email, get_username, get_password

'''
IMPORTANT - Make a file named "credentials.py" in this directory, the file should look EXACTLY like this

def getUsername():
    return "YOUR STUDENT NUMBER"


def getPassword():
    return "YOUR TDSB PASSWORD"


def getEmail():
    return "YOUR TDSB EMAIL"

'''


class SignIn:
    def __init__(self, driver):
        self.driver = driver

    def sign_in(self):
        self.google_sign_in()
        self.tdsb_sign_in()

    def google_sign_in(self):
        emailInput = self.driver.find_element_by_id('identifierId')
        emailInput.send_keys(get_email())

        nextButton = self.driver.find_element_by_class_name('VfPpkd-LgbsSe')
        nextButton.click()

    def tdsb_sign_in(self):
        loaded = EC.presence_of_element_located((By.ID, 'UserName'))
        WebDriverWait(self.driver, 100).until(loaded)

        studentNumberInput = self.driver.find_element_by_id('UserName')
        studentNumberInput.send_keys(get_username())

        passwordInput = self.driver.find_element_by_id('Password')
        passwordInput.send_keys(get_password())

        loginButton = self.driver.find_element_by_id('TdsbLoginControl_Login')
        loginButton.click()

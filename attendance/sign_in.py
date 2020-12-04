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
        email_input = self.driver.find_element_by_id('identifierId')
        email_input.send_keys(get_email())

        next_button = self.driver.find_element_by_class_name('VfPpkd-LgbsSe')
        next_button.click()

    def tdsb_sign_in(self):
        loaded = EC.presence_of_element_located((By.ID, 'UserName'))
        WebDriverWait(self.driver, 100).until(loaded)

        student_number_input = self.driver.find_element_by_id('UserName')
        student_number_input.send_keys(get_username())

        password_input = self.driver.find_element_by_id('Password')
        password_input.send_keys(get_password())

        login_button = self.driver.find_element_by_id('TdsbLoginControl_Login')
        login_button.click()

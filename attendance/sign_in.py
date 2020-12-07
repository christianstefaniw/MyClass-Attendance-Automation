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
        self.continue_button()

    def google_sign_in(self):
        self.form('identifierId', get_email())

        self.click_button('identifierNext')

    def tdsb_sign_in(self):
        self.form('UserName', get_username())
        self.form('Password', get_password())

        self.click_button('TdsbLoginControl_Login')

    # click google continue button after sign in, element doesn't have an id
    def continue_button(self):
        loaded = EC.presence_of_element_located((By.CLASS_NAME, 'VfPpkd-LgbsSe'))
        WebDriverWait(self.driver, 100).until(loaded)
        button = self.driver.find_element_by_class_name("VfPpkd-LgbsSe")
        button.click()

    def click_button(self, button_id):
        loaded = EC.element_to_be_clickable((By.ID, button_id))
        WebDriverWait(self.driver, 100).until(loaded)

        btn = self.driver.find_element_by_id(button_id)
        btn.click()

    def form(self, form_id, cred):
        loaded = EC.presence_of_element_located((By.ID, form_id))
        WebDriverWait(self.driver, 100).until(loaded)

        student_number_input = self.driver.find_element_by_id(form_id)
        student_number_input.send_keys(cred)

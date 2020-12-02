from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from Attendance.Credidentials import *

'''
IMPORTANT - Make a file named "Credidentials.py" in this directory, the file should look EXACTLY like this

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

    def signIn(self):
        self.googleSignIn()
        self.tdsbSignIn()

    def googleSignIn(self):
        emailInput = self.driver.find_element_by_id('identifierId')
        emailInput.send_keys(getEmail())

        nextButton = self.driver.find_element_by_class_name('VfPpkd-LgbsSe')
        nextButton.click()

    def tdsbSignIn(self):
        loaded = EC.presence_of_element_located((By.ID, 'UserName'))
        WebDriverWait(self.driver, 100).until(loaded)

        studentNumberInput = self.driver.find_element_by_id('UserName')
        studentNumberInput.send_keys(getUsername())

        passwordInput = self.driver.find_element_by_id('Password')
        passwordInput.send_keys(getPassword())

        loginButton = self.driver.find_element_by_id('TdsbLoginControl_Login')
        loginButton.click()

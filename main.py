from datetime import datetime, timedelta
from threading import Timer
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Attendance.SignIn import SignIn


time = {'hour': 8, 'minute': 50, 'am_pm': 'am'}


def run():
    print('running...')
    driver = getDriver()
    signIn = SignIn(driver)
    signIn.signIn()
    continueButton(driver)
    submit(driver)
    print('form submitted')
    startTimer()


def submit(driver):
    loaded = EC.presence_of_element_located((By.CLASS_NAME, 'freebirdFormviewerViewNavigationSubmitButton'))
    WebDriverWait(driver, 100).until(loaded)
    submit_button = driver.find_element_by_class_name('freebirdFormviewerViewNavigationSubmitButton')
    submit_button.click()


def continueButton(driver):
    loaded = EC.presence_of_element_located((By.CLASS_NAME, 'VfPpkd-LgbsSe'))
    WebDriverWait(driver, 100).until(loaded)
    button = driver.find_element_by_class_name("VfPpkd-LgbsSe")
    button.click()


def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

    # REPLACE Link WITH YOUR CLASSES FORM
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfdwB-iT9t1kx8Yul0Sqgs9IqHADz9DicuL_YVZfPp2d4uPvA/viewform')
    return driver


def startTimer():
    print(f"Waiting for {time['hour']}:{time['minute']} {time['am_pm']}...")

    x = datetime.today()
    y = x.replace(day=x.day, hour=time['hour'], minute=time['minute'], second=0, microsecond=0) + timedelta(days=1)
    delta_t = y - x

    secs = delta_t.total_seconds()

    t = Timer(secs, run)
    t.start()


if __name__ == '__main__':
    startTimer()

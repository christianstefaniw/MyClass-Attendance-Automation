from selenium import webdriver

from SignIn import *


def run():
    driver = getDriver()
    signIn = SignIn(driver)
    signIn.signIn()
    continueButton(driver)
    submit_button = driver.find_element_by_class_name('appsMaterialWizButtonEl')
    submit_button.click()


def continueButton(driver):
    loaded = EC.presence_of_element_located((By.CLASS_NAME, 'VfPpkd-LgbsSe'))
    WebDriverWait(driver, 10).until(loaded)
    button = driver.find_element_by_class_name("VfPpkd-LgbsSe")
    button.click()


def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfdwB-iT9t1kx8Yul0Sqgs9IqHADz9DicuL_YVZfPp2d4uPvA/viewform')
    return driver


if __name__ == '__main__':
    run()

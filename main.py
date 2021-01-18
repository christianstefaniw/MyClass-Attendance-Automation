from datetime import datetime, timedelta
from threading import Timer
from selenium import webdriver

from attendance.submit_form import *
from attendance.sign_in import *

import os
from dotenv import load_dotenv

load_dotenv()

TIME = {'hour': '10', 'minute': '57', 'am_pm': 'am'}


def run():
    print('running...')
    driver = get_driver()
    sign_in = SignIn(driver)
    sign_in.sign_in()
    submit(driver)
    print('form submitted')


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome('ChromeDriver(v.87)/chromedriver.exe', chrome_options=options)

    driver.get(os.getenv('FORM_LINK'))
    return driver


def start_timer():
    print(f"Waiting for {TIME['hour']}:{TIME['minute']} {TIME['am_pm']}...")

    x = datetime.today()
    y = x.replace(day=x.day, hour=int(TIME['hour']), minute=int(TIME['minute']), second=0, microsecond=0)
    delta_t = y - x

    secs = delta_t.total_seconds()

    t = Timer(secs, run)
    t.start()


if __name__ == '__main__':
    start_timer()

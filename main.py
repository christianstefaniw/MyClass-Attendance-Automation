from datetime import datetime, timedelta
from threading import Timer
from selenium import webdriver
import asyncio

from attendance.submit_form import *
from attendance.sign_in import *

TIME = {'hour': 8, 'minute': 00, 'am_pm': 'am'}


async def run():
    print('running...')
    driver = get_driver()
    sign_in = SignIn(driver)
    await sign_in.sign_in()
    await submit(driver)
    print('form submitted')
    start_timer()


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome('ChromeDriver(v.87)/chromedriver.exe', chrome_options=options)

    # REPLACE Link WITH YOUR CLASSES FORM
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfdwB-iT9t1kx8Yul0Sqgs9IqHADz9DicuL_YVZfPp2d4uPvA/viewform')
    return driver


def start_timer():
    print(f"Waiting for {TIME['hour']}:{TIME['minute']} {TIME['am_pm']}...")

    x = datetime.today()
    y = x.replace(day=x.day, hour=TIME['hour'], minute=TIME['minute'], second=0, microsecond=0) + timedelta(days=1)
    delta_t = y - x

    secs = delta_t.total_seconds()

    t = Timer(secs, go_to_run)
    t.start()


def go_to_run():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run())


if __name__ == '__main__':
    start_timer()

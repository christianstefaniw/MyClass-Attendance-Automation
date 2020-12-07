from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# submit google form
async def submit(driver):
    loaded = EC.presence_of_element_located((By.CLASS_NAME, 'freebirdFormviewerViewNavigationSubmitButton'))
    WebDriverWait(driver, 100).until(loaded)
    submit_button = driver.find_element_by_class_name('freebirdFormviewerViewNavigationSubmitButton')
    await submit_button.click()


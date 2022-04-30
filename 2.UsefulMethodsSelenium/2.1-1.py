from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

try:
    browser = webdriver.Firefox()
    browser.get('https://suninjuly.github.io/selects1.html')

    num1 = browser.find_element(By.ID,'num1')
    num1 = num1.text

    num2 = browser.find_element(By.ID,'num2')
    num2 = num2.text

    sum = str(int(num1) + int(num2))

    dropdown = browser.find_element(By.ID, 'dropdown')
    dropdown.click()

    browser.find_element(By.CSS_SELECTOR, f"[value='{sum}']").click()
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
    time.sleep(1)
    browser.quit()
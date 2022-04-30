from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    
    button = browser.find_element_by_id('book')
    button.click()

    x = browser.find_element_by_id('input_value').text
    answer = calc(x)
    browser.find_element(By.ID,'answer').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR,'.form-group button').click()

    password = (browser.switch_to.alert.text).split(" ")[-1]
    print(password)

finally:
    browser.quit()
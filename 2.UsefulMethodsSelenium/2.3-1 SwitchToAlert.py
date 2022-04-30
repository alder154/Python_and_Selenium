from selenium import webdriver
import time, math
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get(link)

    bannerToGO = browser.find_element(By.CSS_SELECTOR,'div button').click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID,'input_value').text

    outputValue = calc(x)

    fillField= browser.find_element(By.ID,'answer').send_keys(outputValue)
    
    submitBtn = browser.find_element(By.CSS_SELECTOR,'button').click()

    password = (browser.switch_to.alert.text).split(" ")[-1]
    print(password)

finally:
    browser.quit()
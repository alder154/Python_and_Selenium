from selenium import webdriver
import time, math
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get(link)

    flyingBanner = browser.find_element(By.CSS_SELECTOR,'div button').click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x = browser.find_element(By.ID,'input_value').text

    outputValue = calc(x)

    fillField= browser.find_element(By.ID,'answer').send_keys(outputValue)
    
    submitBtn = browser.find_element(By.CSS_SELECTOR,'button').click()

    password = (browser.switch_to.alert.text).split(" ")[-1]
    print(password)

finally:
    browser.quit()
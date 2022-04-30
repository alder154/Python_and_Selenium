from selenium import webdriver
import time, math
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Firefox()
    browser.get('http://SunInJuly.github.io/execute_script.html')

    inputResult = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", inputResult)

    x = browser.find_element(By.ID,'input_value')
    x = int(x.text)
    func = calc(x)
    inputResult.send_keys(func)

    browser.find_element(By.CLASS_NAME, "form-check-label").click()
    browser.find_element(By.XPATH, '//*[text()="Robots rule"]').click()
    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(5)
    browser.quit()
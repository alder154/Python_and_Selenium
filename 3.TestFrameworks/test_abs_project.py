from selenium import webdriver
import time, random, string, unittest

from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
letters = string.ascii_lowercase

def getBrowser(link):
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get(link)
    return browser

def fillBlanks():
    element1 = browser.find_element(By.XPATH,'//*[text()="First name*"]/following-sibling::input')
    element1.send_keys(''.join(random.choice(letters) for _ in range(7)))
    element2 = browser.find_element(By.XPATH,'//*[text()="Last name*"]/following-sibling::input')
    element2.send_keys(''.join(random.choice(letters) for _ in range(7)))
    element3 = browser.find_element(By.XPATH,'//*[text()="Email*"]/following-sibling::input')
    element3.send_keys(''.join(random.choice(letters) for _ in range(7)))
    button = browser.find_element(By.XPATH,'//*[contains(text(), "Submit")]')
    button.click()
    txt = browser.find_element(By.TAG_NAME,"h1").text
    return txt

def test_should_login_to_first_page():
    browser = getBrowser(link1)
    text = fillBlanks()
    assert "Congratulations! You have successfully registered!" == txt, "ошибка ассерта"

def test_should_not_login_to_second_page():
    browser = getBrowser(link2)
    text = fillBlanks()
    assert "Congratulations! You have successfully registered!" == txt, "ошибка ассерта"

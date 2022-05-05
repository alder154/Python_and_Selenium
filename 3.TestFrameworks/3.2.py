from selenium import webdriver
import time, random, string, unittest

from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
letters = string.ascii_lowercase
browser = webdriver.Firefox()
browser.implicitly_wait(10)

class TestAbs(unittest.TestCase):
    def test_should_login_to_first_page(self):
        browser.get(link1)
        element1 = browser.find_element(By.XPATH,'//*[text()="First name*"]/following-sibling::input')
        element1.send_keys(''.join(random.choice(letters) for _ in range(7)))
        element2 = browser.find_element(By.XPATH,'//*[text()="Last name*"]/following-sibling::input')
        element2.send_keys(''.join(random.choice(letters) for _ in range(7)))
        element3 = browser.find_element(By.XPATH,'//*[text()="Email*"]/following-sibling::input')
        element3.send_keys(''.join(random.choice(letters) for _ in range(7)))
        button = browser.find_element(By.XPATH,'//*[contains(text(), "Submit")]')
        button.click()
        txt = browser.find_element(By.TAG_NAME,"h1").text
        self.assertEqual("Congratulations! You have successfully registered!", txt, "ошибка ассерта")

    def test_should_not_login_to_second_page(self):
        browser.get(link2)
        element1 = browser.find_element(By.XPATH,'//*[text()="First name*"]/following-sibling::input')
        element1.send_keys(''.join(random.choice(letters) for _ in range(7)))
        element2 = browser.find_element(By.XPATH,'//*[text()="Last name*"]/following-sibling::input')
        element2.send_keys(''.join(random.choice(letters) for _ in range(7)))
        element3 = browser.find_element(By.CSS_SELECTOR,'.form-control.third')
        element3.send_keys(''.join(random.choice(letters) for _ in range(7)))
        button = browser.find_element(By.XPATH,'//*[contains(text(), "Submit")]')
        button.click()
        txt = browser.find_element(By.TAG_NAME,"h1").text
        self.assertEqual("Congratulations! You have successfully registered!", txt, "ошибка ассерта")

if __name__ == "__main__":
    unittest.main()
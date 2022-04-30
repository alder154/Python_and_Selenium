from selenium import webdriver
import time, random, string, os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)
    letters = string.ascii_letters

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(''.join(random.choice(letters) for _ in range(6)))
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys(''.join(random.choice(letters) for _ in range(6)))
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys(''.join(random.choice(letters) for _ in range(8)))
    
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'empty.txt')
    attach = browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_css_selector("button")
    button.click()

    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

finally:
    time.sleep(1)
    browser.quit()

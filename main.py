import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100'))
print(button)
book = browser.find_element(By.ID, 'book')
book.click()
x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
input1.send_keys(y)
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()
time.sleep(10)

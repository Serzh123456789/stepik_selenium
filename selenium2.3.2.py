from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
alert = browser.switch_to.alert
alert.accept()

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
input1.send_keys(calc(x))

browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(5)
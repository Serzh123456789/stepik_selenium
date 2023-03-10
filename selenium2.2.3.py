from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
input1.send_keys('Ivan')
input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
input2.send_keys('Ivanov')
input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
input3.send_keys('Ivan@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element(By.CSS_SELECTOR, '#file')
element.send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(5)
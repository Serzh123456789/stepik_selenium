from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

summa = int(browser.find_element(By.CSS_SELECTOR, '#num1').text) + int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
browser.find_element(By.ID, "dropdown").click()
browser.find_element(By.CSS_SELECTOR, f"[value='{summa}']").click()
browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(5)
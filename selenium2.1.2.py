from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, '[src="images/chest.png"]')
x = x_element.get_attribute("valuex")
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

button1 = browser.find_element(By.ID, "robotCheckbox")
button1.click()
button2 = browser.find_element(By.ID, "robotsRule")
button2.click()
button3 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button3.click()
time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.ID, "answer")
# elem.clear()
answer.send_keys(y)

checkbox_element = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox_element.click()

radiobutton_element = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton_element.click()

button = browser.find_element(By.XPATH, "//button")
button.click()

time.sleep(10)
browser.quit()

# не забываем оставить пустую строку в конце файла

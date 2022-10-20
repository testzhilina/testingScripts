from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


browser = webdriver.Chrome

browser.get("https://www.google.com/")    
input = browser.find_element(By.XPATH, "//input[@title='Поиск'")
input.send_keys("selenium")
button = browser.find_element(By.XPATH, "//input[@class='gNO89b'")
button.click()
 
time.sleep(10)
browser.quit()

# не забываем оставить пустую строку в конце файла


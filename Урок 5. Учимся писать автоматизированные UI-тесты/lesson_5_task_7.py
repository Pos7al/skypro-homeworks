from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Открыть сайт:
chrome.get("http://the-internet.herokuapp.com/inputs")
firefox.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода
chrome_input_field = chrome.find_element(By.TAG_NAME, "input")
firefox_input_field = firefox.find_element(By.TAG_NAME, "input")

# Вводим текст "1000"
chrome_input_field.send_keys("1000")
firefox_input_field.send_keys("1000")
sleep(3)

# Очищаем поле
chrome_input_field.clear()
firefox_input_field.clear()
sleep(2)

# Вводим текст "999"
chrome_input_field.send_keys("999")
firefox_input_field.send_keys("999")
sleep(3)

chrome.quit()
firefox.quit()

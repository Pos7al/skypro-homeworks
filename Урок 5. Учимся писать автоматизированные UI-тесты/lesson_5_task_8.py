from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Открыть сайт:
chrome.get("http://the-internet.herokuapp.com/login")
firefox.get("http://the-internet.herokuapp.com/login")

# Найти поле Username и ввести в него значение:
chrome_input_login = chrome.find_element(By.ID, "username")
chrome_input_login.send_keys("tomsmith")

firefox_input_login = firefox.find_element(By.ID, "username")
firefox_input_login.send_keys("tomsmith")
sleep(3)

chrome_input_pass = chrome.find_element(By.ID, "password")
chrome_input_pass.send_keys("SuperSecretPassword!")

firefox_input_pass = firefox.find_element(By.ID, "password")
firefox_input_pass.send_keys("SuperSecretPassword!")
sleep(3)

chrome_button = chrome.find_element(By.TAG_NAME, "button").click()
firefox_button = firefox.find_element(By.TAG_NAME, "button").click()
sleep(3)

chrome.quit()
firefox.quit()

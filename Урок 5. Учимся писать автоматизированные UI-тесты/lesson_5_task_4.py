from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Открыть сайт:
chrome.get("http://uitestingplayground.com/dynamicid")
firefox.get("http://uitestingplayground.com/dynamicid")

# Счётчик кликов:
count = 0

# Кликнуть на синюю кнопку:
blue_button = chrome.find_element(
    By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
blue_button = firefox.find_element(
    By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

# Кликнуть на синюю кнопку 3 раза:
for x in range(3):
    blue_button = chrome.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    blue_button = firefox.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    count = count + 1
    sleep(5)
    print(count)

chrome.quit()
firefox.quit()

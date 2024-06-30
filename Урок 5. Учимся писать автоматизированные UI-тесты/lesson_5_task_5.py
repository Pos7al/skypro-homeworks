from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Открыть сайт:
chrome.get("http://uitestingplayground.com/classattr")
firefox.get("http://uitestingplayground.com/classattr")

# Счётчик кликов:
count = 0

# Кликнуть на синюю кнопку:
blue_button = chrome.find_element(
    By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
blue_button = firefox.find_element(
    By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
chrome.switch_to.alert.accept()
firefox.switch_to.alert.accept()

# Кликнуть на синюю кнопку 3 раза:
for x in range(3):
    blue_button = chrome.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    blue_button = firefox.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    sleep(2)
    chrome.switch_to.alert.accept()
    firefox.switch_to.alert.accept()
    count = count + 1

    print(count)

chrome.quit()
firefox.quit()

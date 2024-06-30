from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Открыть сайт:
chrome.get("http://the-internet.herokuapp.com/entry_ad")
firefox.get("http://the-internet.herokuapp.com/entry_ad")

# Ожидаем появления модального окна
chrome_wait = WebDriverWait(chrome, 10)
firefox_wait = WebDriverWait(firefox, 10)


modal_window = chrome_wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
chrome_close_button = chrome_wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".modal-footer")))

modal_window = firefox_wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
firefox_close_button = firefox_wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".modal-footer")))
sleep(3)

chrome_close_button.click()
firefox_close_button.click()
sleep(2)

chrome.quit()
firefox.quit()

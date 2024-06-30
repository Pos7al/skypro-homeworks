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

wait = WebDriverWait(chrome, 10)
wait = WebDriverWait(firefox, 10)

modal_window = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
close_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".modal-footer")))
sleep(5)

close_button.click()
sleep(2)

chrome.quit()
firefox.quit()

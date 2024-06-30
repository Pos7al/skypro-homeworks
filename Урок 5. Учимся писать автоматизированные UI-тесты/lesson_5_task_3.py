from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Открыть сайт
chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Нажать кнопку Add Element 5 раз
for x in range(5):
    add_button = chrome.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
    add_button = firefox.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
    sleep(5)
    # Собираем со страницы список кнопок Delete
    del_btns_chrome = chrome.find_elements(
        By.XPATH, '//button[text()="Delete"]')
    del_btns_firefox = firefox.find_elements(
        By.XPATH, '//button[text()="Delete"]')

# Вывод на экран размер списков в каждом браузере
print(f'Размер списка в Chrome: {len(del_btns_chrome)}')
print(f'Размер списка в Firefox: {len(del_btns_firefox)}')

chrome.quit()
firefox.quit()

import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def func(x):
    return str(math.log(abs(12 * math.sin(x))))
    pass

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price'), '$100')
    )

    # Нажать на кнопку "Book"
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    # Пройти капчу для робота и получить число-ответ
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    res = func(int(x))

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(res)

    # Нажать на кнопку "Submit".
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

    #  Запись результата в консоль
    print(browser.switch_to.alert.text)

finally:
    # Выход
    browser.quit()

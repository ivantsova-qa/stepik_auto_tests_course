import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x):
    return str(math.log(abs(12 * math.sin(x))))
    pass


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

# Нажать на кнопку
browser.find_element(By.CSS_SELECTOR, ' div > button').click()

# Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

# На новой странице решить капчу для роботов, чтобы получить число с ответом
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

res = func(int(x))

browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(res)

# Нажать на кнопку "Submit".
browser.find_element(By.CSS_SELECTOR, 'div > button').click()

# Тамер
time.sleep(3)

#  Запись результата в консоль
print(browser.switch_to.alert.text)

# Выход
browser.quit()

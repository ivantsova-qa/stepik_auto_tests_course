import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x):
    return str(math.log(abs(12 * math.sin(x))))
    pass


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

# Нажать на кнопку
browser.find_element(By.CSS_SELECTOR, 'div > button').click()

# Переключиться на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# Пройти капчу для робота и получить число-ответ
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

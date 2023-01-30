import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

# Заполнить текстовые поля: имя, фамилия, email
browser.find_element(By.CSS_SELECTOR, 'input:nth-child(2)').send_keys('N')
browser.find_element(By.CSS_SELECTOR, 'input:nth-child(4)').send_keys('S')
browser.find_element(By.CSS_SELECTOR, 'input:nth-child(6)').send_keys('Em@mail.ru')

# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
element = browser.find_element(By.CSS_SELECTOR, '#file')

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
element.send_keys(file_path)

# Нажать на кнопку "Submit".
browser.find_element(By.CSS_SELECTOR, ' form > button').click()

# Тамер
time.sleep(10)

# Выход
browser.quit()

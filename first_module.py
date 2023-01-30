from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest


class TestFirstModule(unittest.TestCase):
    def test_page_registration_1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
        input1.send_keys("One")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
        input2.send_keys("Two")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
        input3.send_keys("Three")
        time.sleep(3)

        # Отправить заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Поздравляем! Вы успешно зарегистировались!")

    def test_page_registration_2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
        input1.send_keys("One")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
        input2.send_keys("Two")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
        input3.send_keys("Three")
        time.sleep(3)

        # Отправить заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Поздравляем! Вы успешно зарегистировались!")


if __name__ == "__main__":
    unittest.main()

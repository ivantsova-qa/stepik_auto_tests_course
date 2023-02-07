
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('test', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_login_to_system( browser, test):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{test}/step/1"
    browser.get(link)
    time.sleep(5)

    # click on button
    browser.find_element(By.CSS_SELECTOR, '#ember33').click()
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('ivantsova111@gmail.com')
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('qwerty12345')
    browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
    time.sleep(8)
    browser.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea').send_keys((str(math.log(int(time.time())))))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    message = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text

    assert "Correct!" in message



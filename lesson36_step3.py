import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sample = "Correct!"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link):
    answer = str(math.log(int(time.time())))
    # формируем ссылку
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)

    # Ждем поле ввода
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.string-quiz__textarea')))

    # находим поле ввода и вводим текст
    input = browser.find_element_by_css_selector(".string-quiz__textarea")
    input.send_keys(answer)

    # отсылаем ответ
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    # ждем сообщения о том что проверка пройдена
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))

    # считываеем ответ
    success_elt = browser.find_element_by_css_selector('.smart-hints__hint')

    # записываем в переменную текст ответа
    success_text = success_elt.text

    # сравниваем ответ и ожидание
    assert success_text == sample

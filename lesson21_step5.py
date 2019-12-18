import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input4 = browser.find_element_by_xpath("//*[@id='answer']")
    input4.send_keys(y)
    input5 = browser.find_element_by_xpath("//html/body/div/form/div[2]/label")
    input5.click()
    input5 = browser.find_element_by_xpath("//label[text()='Robots rule']")
    input5.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

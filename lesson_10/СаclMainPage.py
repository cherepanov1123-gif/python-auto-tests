"""
Модуль содержит класс для работы со страницей калькулятора.
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для взаимодействия со страницей калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы калькулятора.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора в браузере.

        :return: self — возвращает текущий объект для цепочки вызовов.
        """
        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(base_url + "slow-calculator.html")
        return self

    @allure.step("Установить задержку калькулятора {seconds} секунд")
    def set_calculator_delay(self, seconds: str):
        """
        Устанавливает задержку калькулятора в поле ввода #delay.

        :param seconds: str — значение задержки в секундах.
        :return: self — возвращает текущий объект для цепочки вызовов.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    @allure.step("Нажать кнопку '{value}'")
    def click_button(self, value: str):
        """
        Нажимает на кнопку калькулятора с указанным текстом.

        :param value: str — текст на кнопке (например, "7", "+", "=").
        :return: self — возвращает текущий объект для цепочки вызовов.
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        )
        button.click()
        return self

    @allure.step("Получить результат с экрана калькулятора")
    def get_result(self) -> str:
        """
        Получает текущий результат с экрана калькулятора.

        :return: str — текст результата, отображаемый на экране.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    @allure.step("Ожидать результат '{expected_result}'")
    def wait_for_result(self, expected_result: str):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected_result: str — ожидаемый результат.
        :return: self — возвращает текущий объект для цепочки вызовов.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_result
            )
        )
        return self

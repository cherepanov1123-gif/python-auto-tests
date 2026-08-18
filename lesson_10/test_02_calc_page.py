"""
Модуль содержит тесты для проверки работы калькулятора с Allure-отчётами.
"""

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from СаclMainPage import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.

    :yield: WebDriver — объект драйвера Selenium.
    """
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title(
    "Тест калькулятора: {num1} {operation} {num2} = {expected_result}"
)
@allure.description(
    "Проверяет корректность работы калькулятора с задержкой. "
    "Выполняется операция {num1} {operation} {num2} с ожиданием "
    "результата {expected_result}."
)
@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 45),
    ],
)
def test_calculator_flow(driver, num1: str, operation: str, num2: str,
                         expected_result: str, delay: int) -> None:
    """
    Проверяет работу калькулятора с заданными параметрами.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param num1: str — первое число.
    :param operation: str — математическая операция (+, -, x, ÷).
    :param num2: str — второе число.
    :param expected_result: str — ожидаемый результат.
    :param delay: int — время задержки в секундах.
    """
    main_page = CalculatorPage(driver)

    with allure.step("Открыть страницу и настроить калькулятор"):
        main_page.open()
        # Вводим задержку 45 в поле #delay на странице (НЕ time.sleep)
        main_page.set_calculator_delay(str(delay))

    with allure.step(f"Выполнить операцию: {num1} {operation} {num2}"):
        main_page.click_button(num1)
        main_page.click_button(operation)
        main_page.click_button(num2)
        main_page.click_button("=")

    with allure.step("Проверить результат"):
        # Ожидание результата через WebDriverWait (НЕ time.sleep)
        main_page.wait_for_result(expected_result)
        result = main_page.get_result()
        assert result == expected_result, (
            f"Ожидалось {expected_result}, получено {result}"
        )

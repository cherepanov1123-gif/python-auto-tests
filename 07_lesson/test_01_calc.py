from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage


def test_calculator():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        result = (
            CalculatorPage(driver)
            .open()
            .set_delay("45")
            .click_button("7")
            .click_button("+")
            .click_button("8")
            .click_button("=")
            .wait_for_result("15")
            .get_result()
        )

        assert result == "15", f"Ожидалось '15', получено '{result}'"

    finally:
        driver.quit()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from login_page import LoginPage


def test_shop():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)

    try:
        total = (
            LoginPage(driver)
            .open()
            .login("standard_user", "secret_sauce")
            .add_item_to_cart("Sauce Labs Backpack")
            .add_item_to_cart("Sauce Labs Bolt T-Shirt")
            .add_item_to_cart("Sauce Labs Onesie")
            .go_to_cart()
            .proceed_to_checkout()
            .fill_form("Иван", "Петров", "123456")
            .get_total()
        )

        assert "$58.29" in total, f"Итоговая сумма не совпадает: {total}"

    finally:
        driver.quit()

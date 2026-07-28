from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def test_shop():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item_name in items:
            item_xpath = (
                f"//div[text()='{item_name}']/ancestor::"
                f"div[@class='inventory_item']//button"
            )
            driver.find_element(By.XPATH, item_xpath).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        total = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total.text
        assert "$58.29" in total_text, (
            f"Итоговая сумма не совпадает: {total_text}"
        )

    finally:
        driver.quit()

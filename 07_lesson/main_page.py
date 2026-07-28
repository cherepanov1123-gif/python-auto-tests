from selenium.webdriver.common.by import By
from cart_page import CartPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name: str):
        item_xpath = (
            f"//div[text()='{item_name}']/ancestor::"
            f"div[@class='inventory_item']//button"
        )
        self.driver.find_element(By.XPATH, item_xpath).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)

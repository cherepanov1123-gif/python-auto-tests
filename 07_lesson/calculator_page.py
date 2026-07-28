from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(base_url + "slow-calculator.html")
        return self

    def set_delay(self, seconds: str):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_button(self, value: str):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        )
        button.click()
        return self

    def get_result(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    def wait_for_result(self, expected_result: str):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_result
            )
        )
        return self

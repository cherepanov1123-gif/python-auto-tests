from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def test_form():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        fields = {
            "first-name": ("id", "Иван"),
            "last-name": ("id", "Петров"),
            "address": ("id", "Ленина, 55-3"),
            "e-mail": ("id", "test@skypro.com"),
            "phone": ("id", "+7985899998787"),
            "zip-code": ("id", ""),
            "city": ("id", "Москва"),
            "country": ("id", "Россия"),
            "job-position": ("id", "QA"),
            "company": ("id", "SkyPro")
        }

        for field_id, (locator_type, value) in fields.items():
            try:
                field = driver.find_element(By.ID, field_id)
            except Exception:
                try:
                    field = driver.find_element(By.NAME, field_id)
                except Exception:
                    field = driver.find_element(
                        By.XPATH, f"//input[@id='{field_id}']"
                    )
            field.clear()
            if value:
                field.send_keys(value)

        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()

        zip_field = driver.find_element(By.ID, "zip-code")
        zip_class = zip_field.get_attribute("class")
        assert (
            "alert-danger" in zip_class or "error" in zip_class
        ), f"Zip code не подсвечен красным. Класс: {zip_class}"

        green_fields = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]
        for field_id in green_fields:
            field = driver.find_element(By.ID, field_id)
            field_class = field.get_attribute("class")
            assert (
                "alert-success" in field_class or "success" in field_class
            ), f"Поле {field_id} не подсвечено зеленым. Класс: {field_class}"

    finally:
        driver.quit()

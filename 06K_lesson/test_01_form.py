import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_form_validation(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }


    for field_name, value in fields.items():
        browser.find_element(By.NAME, field_name).send_keys(value)


    browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()


    zip_code = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )
    assert "danger" in zip_code.get_attribute("class")


    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field_id in valid_fields:
        field = browser.find_element(By.ID, field_id)
        assert "success" in field.get_attribute("class")

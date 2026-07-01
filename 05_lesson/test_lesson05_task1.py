from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://httpbin.org/")

    link = driver.find_element(By.CSS_SELECTOR, "a[href='/forms/post']")
    link.click()

    assert "/forms/post" in driver.current_url

    driver.back()

    assert driver.current_url == "https://httpbin.org/"

    driver.quit()

from selenium import webdriver


def test_cookie_auth():
    driver = webdriver.Chrome()

    user1_cookie = {
        "name": "SESSION",
        "value": "YmM4MmVlNzUtNzgzOC00NmMwLTk3NzQtNzdjZjlkNzIwYjE2"
    }
    user2_cookie = {
        "name": "SESSION",
        "value": "MmNlMmFmZWMtNTdmZi00YTQ3LTkzMDAtNzIyNDE5MDJlZTlm"
    }

    # Пользователь 1
    driver.get("https://gitflic.ru/")
    driver.add_cookie(user1_cookie)
    driver.refresh()

    driver.get("https://gitflic.ru/profile")
    url_user1 = driver.current_url

    # Выход
    driver.delete_all_cookies()
    driver.refresh()

    # Пользователь 2
    driver.get("https://gitflic.ru/")
    driver.add_cookie(user2_cookie)
    driver.refresh()

    driver.get("https://gitflic.ru/profile")
    url_user2 = driver.current_url

    assert url_user1 != url_user2, (
        f"URL одинаковые: {url_user1} и {url_user2}"
    )

    driver.quit()

import os
import pytest
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
COMPANY_ID = os.getenv("COMPANY_ID")


@pytest.fixture(scope="session")
def api_session():
    """Создаёт сессию с авторизацией для всех тестов."""
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    })
    session.base_url = BASE_URL
    return session


@pytest.fixture
def company_id():
    """Возвращает ID компании."""
    return COMPANY_ID


@pytest.fixture
def project_data(company_id):
    """Данные для создания проекта (только title)."""
    # Пробуем упрощённый формат
    return {
        "title": "Test Project"
    }

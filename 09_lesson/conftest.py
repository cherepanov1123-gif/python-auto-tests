import pytest
from sqlalchemy import create_engine


@pytest.fixture(scope="session")
def db_connection():
    """Фикстура для подключения к базе данных."""
    connection_string = "postgresql://postgres:1234@localhost:5432/mydatabase"
    engine = create_engine(connection_string)
    connection = engine.connect()
    yield connection
    connection.close()

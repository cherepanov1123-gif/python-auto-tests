class TestProjects:
    """Тесты для методов работы с проектами."""

    # ==================== POST /projects ====================

    def test_create_project_positive(self, api_session, project_data):
        """Позитивный тест: создание проекта."""
        response = api_session.post(
            f"{api_session.base_url}/projects", json=project_data
        )
        assert response.status_code == 201, (
            f"Ожидался 201, получен {response.status_code}"
        )
        assert "id" in response.json(), "В ответе нет поля id"

    def test_create_project_negative_empty_title(self, api_session):
        """Негативный тест: создание проекта с пустым title."""
        invalid_data = {"title": ""}
        response = api_session.post(
            f"{api_session.base_url}/projects", json=invalid_data
        )
        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )
        assert "error" in response.json(), "В ответе нет поля error"

    def test_create_project_negative_no_title(self, api_session):
        """Негативный тест: создание проекта без поля title."""
        invalid_data = {}
        response = api_session.post(
            f"{api_session.base_url}/projects", json=invalid_data
        )
        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )
        assert "error" in response.json(), "В ответе нет поля error"

    # ==================== GET /projects/{id} ====================

    def test_get_project_positive(self, api_session, project_data):
        """Позитивный тест: получение проекта по ID."""
        create_response = api_session.post(
            f"{api_session.base_url}/projects", json=project_data
        )
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]

        get_response = api_session.get(
            f"{api_session.base_url}/projects/{project_id}"
        )
        assert get_response.status_code == 200
        assert get_response.json()["title"] == project_data["title"], (
            "Название проекта не совпадает"
        )

    def test_get_project_negative_not_found(self, api_session):
        """Негативный тест: получение проекта по несуществующему ID."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api_session.get(
            f"{api_session.base_url}/projects/{fake_id}"
        )
        assert response.status_code == 404
        assert "error" in response.json()

    def test_get_project_negative_invalid_id(self, api_session):
        """Негативный тест: получение проекта по невалидному ID."""
        fake_id = "invalid-id"
        response = api_session.get(
            f"{api_session.base_url}/projects/{fake_id}"
        )
        assert response.status_code == 404
        assert "error" in response.json()

    # ==================== PUT /projects/{id} ====================

    def test_put_project_positive(self, api_session, project_data):
        """Позитивный тест: обновление проекта."""
        create_response = api_session.post(
            f"{api_session.base_url}/projects", json=project_data
        )
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]

        update_data = {"title": "Updated Project Title"}
        update_response = api_session.put(
            f"{api_session.base_url}/projects/{project_id}",
            json=update_data
        )
        assert update_response.status_code == 200

        get_response = api_session.get(
            f"{api_session.base_url}/projects/{project_id}"
        )
        assert get_response.json()["title"] == "Updated Project Title", (
            "Название не обновилось"
        )

    def test_put_project_negative_not_found(self, api_session):
        """Негативный тест: обновление несуществующего проекта."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        update_data = {"title": "Updated Project"}
        response = api_session.put(
            f"{api_session.base_url}/projects/{fake_id}",
            json=update_data
        )
        assert response.status_code == 404
        assert "error" in response.json()

    def test_put_project_negative_invalid_id(self, api_session):
        """Негативный тест: обновление проекта с невалидным ID."""
        fake_id = "invalid-id"
        update_data = {"title": "Updated Project"}
        response = api_session.put(
            f"{api_session.base_url}/projects/{fake_id}",
            json=update_data
        )
        assert response.status_code == 404
        assert "error" in response.json()

    def test_put_project_negative_empty_title(self, api_session, project_data):
        """Негативный тест: обновление проекта с пустым title."""
        create_response = api_session.post(
            f"{api_session.base_url}/projects", json=project_data
        )
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]

        update_data = {"title": ""}
        response = api_session.put(
            f"{api_session.base_url}/projects/{project_id}",
            json=update_data
        )
        assert response.status_code == 400
        assert "error" in response.json()

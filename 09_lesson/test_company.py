from db_utils import DBUtils


class TestCompany:
    """Тесты для работы с компаниями."""

    def test_create_company(self, db_connection):
        """Тест: добавление новой компании."""
        db = DBUtils(db_connection)
        name = "Test Company"

        company_id = db.insert_company(name)
        company = db.get_company_by_id(company_id)

        assert company is not None, "Компания не была создана"
        assert company["name"] == name, "Название компании не совпадает"

        db.delete_company(company_id)

        company_after_delete = db.get_company_by_id(company_id)
        assert company_after_delete is None, "Компания не была удалена"

    def test_update_company(self, db_connection):
        """Тест: изменение названия компании."""
        db = DBUtils(db_connection)
        name = "Old Name"
        new_name = "New Name"

        company_id = db.insert_company(name)
        db.update_company_name(company_id, new_name)

        company = db.get_company_by_id(company_id)
        assert company is not None, "Компания не найдена после обновления"
        assert company["name"] == new_name, "Название не обновилось"

        db.delete_company(company_id)

    def test_delete_company(self, db_connection):
        """Тест: удаление компании."""
        db = DBUtils(db_connection)
        name = "Company to Delete"

        company_id = db.insert_company(name)

        company_before = db.get_company_by_id(company_id)
        assert company_before is not None, "Компания не была создана"

        db.delete_company(company_id)

        company_after = db.get_company_by_id(company_id)
        assert company_after is None, "Компания не была удалена"

    def test_create_and_get_all_companies(self, db_connection):
        """Дополнительный тест: добавление компании и проверка списка."""
        db = DBUtils(db_connection)
        name = "Company for List"

        companies_before = db.get_all_companies()
        count_before = len(companies_before)

        company_id = db.insert_company(name)

        companies_after = db.get_all_companies()
        count_after = len(companies_after)

        assert count_after == count_before + 1, (
            "Количество компаний не увеличилось"
        )

        found = False
        for company in companies_after:
            if company["id"] == company_id:
                found = True
                assert company["name"] == name, (
                    "Название компании в списке не совпадает"
                )
                break
        assert found, "Добавленная компания не найдена в списке"

        db.delete_company(company_id)

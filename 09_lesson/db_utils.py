from sqlalchemy.sql import text


class DBUtils:
    def __init__(self, connection):
        self.connection = connection

    def insert_company(self, name):
        """Добавляет новую компанию и возвращает её ID."""
        trans = self.connection.begin()
        sql = text(
            "INSERT INTO company(\"name\") VALUES (:new_name) RETURNING id"
        )
        result = self.connection.execute(sql, {"new_name": name})
        trans.commit()
        return result.fetchone()[0]

    def update_company_name(self, company_id, new_name):
        """Обновляет название компании по ID."""
        trans = self.connection.begin()
        sql = text("UPDATE company SET name = :new_name WHERE id = :id")
        self.connection.execute(sql, {"new_name": new_name, "id": company_id})
        trans.commit()

    def delete_company(self, company_id):
        """Удаляет компанию по ID."""
        trans = self.connection.begin()
        sql = text("DELETE FROM company WHERE id = :id")
        self.connection.execute(sql, {"id": company_id})
        trans.commit()

    def get_company_by_id(self, company_id):
        """Возвращает компанию по ID."""
        sql = text("SELECT * FROM company WHERE id = :id")
        result = self.connection.execute(sql, {"id": company_id})
        return result.fetchone()

    def get_all_companies(self):
        """Возвращает все компании."""
        sql = text("SELECT * FROM company")
        result = self.connection.execute(sql)
        return result.fetchall()

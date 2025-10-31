import sqlite3


class DatabaseManager:
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.init_database()

    def init_database(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_record(self, name, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO records (name, email) VALUES (?, ?)", (name, email))
            self.conn.commit()
            return True
        except:
            return False

    def get_all_records(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM records")
        return cursor.fetchall()

    def delete_record(self, record_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except:
            return False


class SimpleUI:
    def __init__(self):
        self.db = DatabaseManager()
        self.message = ""

    def add_record(self, name, email):
        if not name or not email:
            self.message = "Ошибка: заполните все поля"
            return False

        success = self.db.add_record(name, email)
        if success:
            self.message = "Запись добавлена"
        else:
            self.message = "Ошибка при добавлении записи"
        return success

    def show_records(self):
        return self.db.get_all_records()

    def get_message(self):
        return self.message

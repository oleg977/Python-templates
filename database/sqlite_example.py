
#### Пример содержимого файлов:

##### `sqlite_example.py`
```python
import sqlite3

def create_table():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_user(name, age):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def fetch_users():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_user("Alice", 25)
    insert_user("Bob", 30)
    fetch_users()
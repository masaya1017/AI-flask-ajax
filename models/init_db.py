import sqlite3

db_path = "./hw.sqlite3"

sql = '''
    CREATE TABLE IF NOT EXISTS greetings (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        greeting TEXT NOT NULL,
        image_path TEXT
    )
    '''
with sqlite3.connect(db_path) as conn:
    conn.execute(sql)

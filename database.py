# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('petadoption.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Pets (
            pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT,
            breed TEXT,
            age INTEGER,
            gender TEXT,
            status TEXT DEFAULT 'Available'
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Adoption_Requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            pet_id INTEGER,
            request_date TEXT,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (pet_id) REFERENCES Pets(pet_id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ Database initialized successfully.")

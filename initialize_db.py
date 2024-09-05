import sqlite3

def create_db():

    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

        #user table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            join_date TEXT NOT NULL
        )
    ''')

        #transaction table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            transaction_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')

    # conn.commit()
    # conn.close()

    users = [
        ("Rohit Kumar", "rohit@gmail.com", "2024-09-10"),
        ("Vicky Kumar", "vicky121@gmail.com", "2019-01-10"),
        ("Arav", "arravvv.im@gmail.com", "2020-09-10"),
        ("Bhargav", "Bhargavva@gmail.com", "2024-09-10"),
        ("Vishnu Khanapure", "vish.hero@gmail.com", "2025-09-10"),
        ("Urban Pahadi", "urban.pahadi10@gmail.com", "2024-06-15"),
        ("Kamalkishor", "kishorkamal11@gmail.com", "2023-02-10"),
        ("Anmol", "anmoool@gmail.com", "2023-02-10"),
        ("Prabhakar", "prabhakar@gmail.com", "2023-02-10"),
    ]

    cur.executemany('INSERT INTO users (name, email, join_date) VALUES (?, ?, ?)', users)

    transactions = [
        (1, 120.34, '2023-02-01'),
        (2, 120.34, '2023-02-18'),
        (2, 120.34, '2024-02-14'),
        (3, 120.34, '2024-03-01'),
        (3, 120.34, '2024-09-07'),
        (4, 120.34, '2023-04-01'),
        (4, 120.34, '2023-05-01'),
        (5, 120.34, '2024-08-16'),
        (5, 120.34, '2024-03-16'),
        (6, 120.34, '2023-01-01'),
        (6, 120.34, '2024-02-01'),
        (6, 120.34, '2023-03-01'),
        (6, 120.34, '2024-09-01'),
        (7, 120.34, '2023-04-11'),
        (7, 120.34, '2023-08-02'),
        (7, 120.34, '2023-06-06'),
        (7, 120.34, '2024-09-13'),
        (7, 120.34, '2024-10-11'),
        (7, 120.34, '2024-10-02')
    ]

    cur.executemany('INSERT INTO transactions(user_id, amount, transaction_date) VALUES (?, ?, ?)', transactions)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()

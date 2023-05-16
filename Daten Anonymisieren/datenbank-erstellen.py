import sqlite3

# Verbinde dich mit der Datenbankdatei
with sqlite3.connect('database-initial.db') as conn:
    c = conn.cursor()

    # Erstelle die Tabelle employees
    c.execute('''
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            date_of_birth TEXT,
            salary REAL,
            username TEXT,
            password_hash TEXT,
            is_vip INTEGER
        )
    ''')

    # Füge einige Einträge hinzu
    employees = [
        (1, "John", "Doe", "1980-01-01", 60000, "johndoe", "hash1", 1),
        (2, "Tomi", "Doe", "1990-01-01", 70000, "tomdoe", "hash2", 0),
        (3, "Jim", "Brown", "1985-01-01", 80000, "jimbrown", "hash3", 1),
        (4, "Bobi", "Smith", "1970-01-01", 90000, "bobismith", "hash4", 0),
        (5, "Mike", "Johnson", "1982-01-01", 100000, "mikejohnson", "hash5", 1),
    ]

    c.executemany('''
        INSERT INTO employees VALUES (?,?,?,?,?,?,?,?)
    ''', employees)

    # Speichere die Änderungen
    conn.commit()

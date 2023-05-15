import sqlite3
import random

# Definiere die Gehaltskategorien
LOW_SALARY = "low"
MEDIUM_SALARY = "medium"
HIGH_SALARY = "high"

# Verbinde dich mit der Datenbankdatei
with sqlite3.connect('database-initial.db') as conn:
    c = conn.cursor()

    # Anonymisiere die Vornamen
    c.execute("UPDATE employees SET first_name = substr(first_name,1,1) || '*********' WHERE first_name IS NOT NULL")

    # Anonymisiere Nachnamen mit Zufallszahlen
    c.execute("UPDATE employees SET last_name = CAST(ABS(RANDOM()) % 10000000000 AS TEXT) WHERE last_name IS NOT NULL")

    # Anonymisiere das Geburtsdatum auf das Jahr
    c.execute("UPDATE employees SET date_of_birth = strftime('%Y', date_of_birth) WHERE date_of_birth IS NOT NULL")

    # Anonymisiere Gehälter zu Kategorien
    c.execute("UPDATE employees SET salary = ? WHERE salary < 50000", (LOW_SALARY,))
    c.execute("UPDATE employees SET salary = ? WHERE salary >= 50000 AND salary < 100000", (MEDIUM_SALARY,))
    c.execute("UPDATE employees SET salary = ? WHERE salary >= 100000", (HIGH_SALARY,))

    # Entferne Benutzernamen, Passworthashes und VIP-Status
    c.execute("UPDATE employees SET username = NULL")
    c.execute("UPDATE employees SET password_hash = NULL")
    c.execute("UPDATE employees SET is_vip = 0")

    # Speichere die Änderungen
    conn.commit()

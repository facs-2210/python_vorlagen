annonymisiert daten von der datenbank namens database-initial.db


Konstanten werden definiert
(LOW_SALARY mittel MEDIUM_SALARY  hoch HIGH_SALARY


Eine Verbindung zur SQLite-Datenbank database-initial.db wird hergestellt

Die Vornamen in der Tabelle employees werden anonymisiert, indem nur der 
erste Buchstabe beibehalten und der Rest durch Sternchen ersetzt wird


Die Nachnamen werden durch Zufallszahlen ersetzt

Das Geburtsdatum wird auf das Jahr reduziert

Benutzernamen und Passworthashes werden entfernt 


script ausfuhren

python3 Daten_AnonymisierenSQL.py database-initial.db
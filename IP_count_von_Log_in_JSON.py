import sys
import json
from collections import Counter

# Überprüfung, ob ein Argument für die Protokolldatei angegeben wurde
if len(sys.argv) != 2:
    print("Verwendung: python program.py access.log")
    sys.exit(1)

try:
    # Öffnen der Protokolldatei und Zählen der Vorkommen jeder IP-Adresse
    with open(sys.argv[1]) as f:
        ip_counts = Counter(line.split()[0] for line in f)

    # Sortieren der IP-Adressen nach Auftreten und Schreiben in eine JSON-Datei
    with open('results.json', 'w') as f:
        # Erstellen einer Liste von Wörterbüchern mit IP-Adressen und Auftretenszahlen
        results = [{'ip': ip, 'count': count} for ip, count in ip_counts.most_common()]
        # Schreiben der Liste als JSON in die Datei
        json.dump(results, f, indent=2)

except FileNotFoundError:
    print(f"Fehler: Datei {sys.argv[1]} nicht gefunden.")
except IOError:
    print(f"Fehler: Kann Datei {sys.argv[1]} nicht lesen oder schreiben.")

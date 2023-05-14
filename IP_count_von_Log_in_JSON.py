import sys
import json
from collections import Counter

# Check if an argument for the log file was specified
# Prüfen, ob ein Argument für die Log-Datei angegeben wurde
if len(sys.argv) != 2:
    print("Usage: python program.py access.log")
    sys.exit(1)

try:
    # Open the log file and count the occurrence of each IP address
    # Öffnen der Log-Datei und Zählen der IP-Adressen
    with open(sys.argv[1]) as f:
        ip_counts = Counter(line.split()[0] for line in f)

    # Sort the IP addresses by occurrence and write them to a JSON file
    # Sortieren der IP-Adressen nach Häufigkeit und Schreiben in eine JSON-Datei
    with open('results.json', 'w') as f:
        # Create a list of dictionaries with IP addresses and occurrence counts
        # Erstellen einer Liste von Wörterbüchern mit IP-Adresse und Anzahl der Vorkommnisse
        results = [{'ip': ip, 'count': count} for ip, count in ip_counts.most_common()]
        # Write the list to the file as JSON
        # Schreiben der Liste als JSON in die Datei
        json.dump(results, f, indent=2)

except FileNotFoundError:
    print(f"Error: File {sys.argv[1]} not found.")
except IOError:
    print(f"Error: Cannot read or write file {sys.argv[1]}.")

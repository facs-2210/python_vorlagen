Einlesen von .log / CSV file:


# Importieren der benötigten Module
import os
import re
 
# Pfad zur Logdatei von Apache2
datei_pfad = "/var/log/apache2/access.log"
 
# Überprüfen, ob die Logdatei existiert
if not os.path.exists(datei_pfad):
    print("Logdatei existiert nicht!")
    exit(1)

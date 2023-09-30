#!/bin/bash

# Ordner erstellen, wenn er nicht existiert
mkdir -p security_results

# Dateien mit SUID-Bit suchen und in suid_files.txt speichern
find / -type f -executable -perm -4000 2>/dev/null > security_results/suid_files.txt

# Benutzer und Gruppen anzeigen und in user_groups.txt speichern
cat /etc/passwd /etc/group > security_results/user_groups.txt

# Crontab anzeigen und in crontab.txt speichern
crontab -l > security_results/crontab.txt
cat /etc/cron* >> security_results/crontab.txt

# Dienste anzeigen und in services.txt speichern
ps -aux > security_results/services.txt

# Offene Verbindungen anzeigen und in connections.txt speichern
netstat -tulpn > security_results/connections.txt

# SGID-Binärdateien suchen und in sgid_files.txt speichern
find / -type f -executable -perm -2000 2>/dev/null > security_results/sgid_files.txt

# Meldung ausgeben
echo "Die Überprüfung ist abgeschlossen. Ergebnisse wurden in security_results/ gespeichert."

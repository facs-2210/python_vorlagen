Den Scan ausfuhren
┌──(root㉿try)-[/home/hacker]
└─# bash linux-sec-audit.sh
Die Überprüfung ist abgeschlossen. Ergebnisse wurden in security_results/ gespeichert.


in den Ordner wechseln welche vom scan erstellt wurde
┌──(root㉿try)-[/home/hacker]
└─# cd security_results/                                                                                                                                                                                           
File wo erstellt wurden
┌──(root㉿try)-[/home/hacker/security_results]
└─# ls                                                                                                                                                                                                       
connections.txt  crontab.txt  services.txt  sgid_files.txt  suid_files.txt  user_groups.txt


Einzelne Files des scan analysieren

┌──(root㉿try)-[/home/hacker/security_results]
└─# cat sgid_files.txt 

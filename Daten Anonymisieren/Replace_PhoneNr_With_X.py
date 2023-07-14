
import csv

Origfile = "C:\\scripts\\User.csv"  # add additional \ in path to escape
Newfile = "C:\\scripts\\newUser.csv"

replacementstr = "xxxx"            # string to replace

with open(Origfile, newline="", encoding="utf-8-sig") as csv_orig:
    csv_reader = csv.reader(csv_orig, delimiter=",")            # "," set the correct delimiter
    linecount = 0

    for line in csv_reader:
        if linecount == 0:
            with open(Newfile, "a", newline="", encoding="utf-8-sig") as csv_newfile:       # "a" for append.  newline="" to avoid Carriage return and line feed (CRLF) under windows 
                csv_writer = csv.writer(csv_newfile, delimiter=",")
                csv_writer.writerow(line[0:]) 
            linecount +=1

        else:
            original_phone = line[2]                             # Set correct index of the to be edited column, Reminder: starts 0, 1, 2, ...                       
            new_phone = original_phone[:-4] + replacementstr     # [:-4] how many charackters will be deleted in the end of the string. warning: whitespaces count as well 
            line[2] = new_phone
            with open(Newfile, "a", newline="", encoding="utf-8") as csv_newfile:
                csv_writer = csv.writer(csv_newfile, delimiter=",")
                csv_writer.writerow(line[0:])  
            linecount +=1



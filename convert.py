import configparser
import os

file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 1
a = [] 
# Strips the newline character
config = configparser.ConfigParser()
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))
    a.append(line.strip())
    count+=1

if(os.path.isfile('convert_input.ini')==False):
    config[a[2]] = {"name": a[0],
                    "ip": a[1],
                    "id": a[2],
                    "register": a[3],
                    "datatype": a[4],
                    "readtype": a[5],
                    "precision": a[6],
                    "topic": a[7]}
    with open('convert_input.ini','w') as configfile:
        config.write(configfile)
else:
    config.read('convert_input.ini')
    config[a[2]] = {"name": a[0],
                    "ip": a[1],
                    "id": a[2],
                    "register": a[3],
                    "datatype": a[4],
                    "readtype": a[5],
                    "precision": a[6],
                    "topic": a[7]}
    with open('convert_input.ini','w') as configfile:
        config.write(configfile)

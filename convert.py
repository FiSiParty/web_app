import configparser
import os

file1 = open('test.txt', 'r') 
Lines = file1.readlines() 
  
count = 1
a = [] 
# Strips the newline character
config = configparser.ConfigParser()
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))
    a.append(line.strip())
    count+=1
print(a)
if(os.path.isfile('config.ini')==False):
    config[a[2]] = {"Name": a[0],
                    "IP": a[1],
                    "Register": a[3],
                    "readtype": a[4],
                    "precision": a[5],
                    "topic": a[6]}
    with open('config.ini','w') as configfile:
        config.write(configfile)
else:
    config.read('config.ini')
    config[a[2]] = {"Name": a[0],
                    "IP": a[1],
                    "Register": a[3],
                    "readtype": a[4],
                    "precision": a[5],
                    "topic": a[6]}
    with open('config.ini','w') as configfile:
        config.write(configfile)

file1.close()
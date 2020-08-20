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

if(os.path.isfile('config.ini')==False):
    config[a[0]] = {"Register": a[1]}
    with open('config.ini','w') as configfile:
        config.write(configfile)
else:
    config.read('config.ini')
    config[a[0]] = {"Register": a[1]}
    with open('config.ini','w') as configfile:
        config.write(configfile)

import paho.mqtt.client as mqtt
import configparser
import os

host = "siamgreenergy.com"
port = 1883
client = mqtt.Client()
client.connect(host)

def CheckNumSect():
    parser = configparser.ConfigParser()
    parser.read('sub_data.ini')
    i=1
    for sect in parser.sections():
       i+=1
    return i

def ShowAllSect():
    parser = configparser.ConfigParser()
    parser.read('sub_data.ini')
    i = 1
    print("All sections in flie...")
    for sect in parser.sections():
       print('%d'%i, sect)
       i+=1
    print()

def EachSect(c):
    parser = configparser.ConfigParser()
    parser.read('sub_data.ini')
    i = 1
    for sect in parser.sections():
        if i==c:
            print(sect)
            for k,v in parser.items(sect):
                print(' {} = {}'.format(k,v))
                client.publish("eiei", v)
            print()
            i+=1
        else:
            i+=1

def ReadIndex():
    parser = configparser.ConfigParser()
    parser.read('sub_data.ini')
    a = CheckNumSect()
    ShowAllSect()
    while True :
        try:
            c = int(input("Select section: "))
            break
        except ValueError:
            print("Please try again!!")
    while c>=a or c<=0:
        print("Please try again!!")
        ShowAllSect()
        while True :
            try:
                c = int(input("Select section: "))
                break
            except ValueError:
                print("Please try again!!")
        print()
    EachSect(c)

ReadIndex()

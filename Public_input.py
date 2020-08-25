import paho.mqtt.client as mqtt
import configparser
import os

host = "siamgreenergy.com"
port = 1883
client = mqtt.Client()
client.connect(host)

path = 'convert_input.ini'

def get_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, sett):
   
    config = get_config(path)
    value = config.get(section, sett)
    msg = "{section} {sett} = {value}".format(
        section=section, sett=sett, value=value)
    return value

def get_section(path):
    config = get_config(path)
    sect = config.sections()
    return sect

def CheckNumSect():
    parser = configparser.ConfigParser()
    parser.read('convert_input.ini')
    i=1
    for sect in parser.sections():
       i+=1
    return i

def ShowAllSect():
    parser = configparser.ConfigParser()
    parser.read('convert_input.ini')
    i = 1
    print("All sections in flie...")
    for sect in parser.sections():
       print('%d'%i, sect)
       i+=1
    print()

def EachSect(c):
    parser = configparser.ConfigParser()
    parser.read('convert_input.ini')
    section = get_section(path)
    i = 0
    for sect in parser.sections():
        if i==c:
            print(sect)
            for k,v in parser.items(sect):
                print('{} = {}'.format(k,v))
                topic = get_setting(path, section[i], "topic")
                print(section)
                print(topic)
                client.publish(topic, v)
                
            print()
            i+=1
        else:
            i+=1

def ReadIndex():
    parser = configparser.ConfigParser()
    parser.read('convert_input.ini')
    a = CheckNumSect()
    ShowAllSect()
    c=0
    print("a: ",a)
    while c<a :
        EachSect(c)
        print("c: ",c)
    
        c+=1
    

ReadIndex()

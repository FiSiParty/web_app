from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.compat import iteritems
import struct
import paho.mqtt.client as mqtt 
import time
import configparser
import os
from tkinter import messagebox

########## write data connection to config
def main():
    getValue()
##    path = 'config.ini'
##    section = get_section(path) #Array Section name
##    ad1 = get_setting(path, section[0], "register" ) #value in section
##    ans = int(ad1)
##    a = connect(ans)
##    config = configparser.ConfigParser()
##    config['The result'] = {"Answer": a}
##    with open('result.ini','w') as configfile:
##        config.write(configfile)
##    print("a = ", a)
    
    #function = get_setting(path, section[0], "function" )
    #print(function)
    #datatype = get_setting(path, section[0], "data type" )
    #print(datatype)
    


def getValue():
    path = 'sub_data.ini'
    config = configparser.RawConfigParser()
    section = get_section(path)
    print("section = ",section)
    couta = len(section)
    print("couta: ",couta)
    i =0
    while i<couta:
        ad1 = get_setting(path, section[i], "register")
        ad1 = ad1[2:]
        print("ad1: ",ad1)
        ans = int(ad1)
        print(ans)  
        a = connect(ans)
        print("ad1: ",ad1)
        print("a = ",a)
        
        config.read('sub_data.ini')
        config.set(section[i], 'answer', a)
        with open('sub_data.ini','w') as configfile:
            config.write(configfile)

        
        i+=1
        print("i = ",i)



def connect(ad1):
    client = ModbusTcpClient("192.168.0.7")
    if client.connect():
        #ad1=int(input("address1: ")) # Address input normal
        register = int(ad1)
        print("register: ",register)
        
        try:
            result1 = client.read_input_registers(address=register-1,count=1,unit=1)  #Uint32/1
            result2 = client.read_input_registers(address=register,count=1,unit=1)   #Uint32/2
            r = result2.registers + result1.registers #[Uint32/2, Uint32/1]
            print(r)
        except AttributeError:
            print("attributeError")
            connect(ad1)
        try:
    
            try:
                b=struct.pack('HH',r[0],r[1]) 
                ans=struct.unpack('f',b)[0]
                ans = '%.2f'%ans
                allans = ans
                print('Ans: ',allans)
                client.close()
                return allans
            except UnboundLocalError:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!UnboundLocalError!!!!!!!!!!!!!!!!!!!!!!!!!!")
                connect(ad1)
        except :
            messagebox.askretrycancel("Message", "Cannot connect to the Modbus Server/Slave")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!Cannot connect to the Modbus Server/Slave!!!!!!!!!!!!!!!!!!!!!!!!!!")
            connect(ad1)
            raise
        
    else:
        
        
        print('Cannot connect to the Modbus Server/Slave')
        connect(ad1)

##    except:
##        messagebox.askretrycancel("Message", "Cannot connect to the Modbus Server/Slave")
##        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!Cannot connect to the Modbus Server/Slave!!!!!!!!!!!!!!!!!!!!!!!!!!")
##        connect(ad1,comport)
##        raise
        

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


main()
    

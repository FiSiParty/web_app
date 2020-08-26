import paho.mqtt.client as mqtt
import configparser
import os
host = 'siamgreenergy.com'
port = 1883

def CheckNumSect():
    parser = configparser.ConfigParser()
    parser.read('convert_input.ini')
    i=1
    for sect in parser.sections():
       i+=1
    return i

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

def on_connect(self, client, userdata, rc):
    print("MQTT Connected :" +str(rc))
    
    
    
    self.subscribe('topic2')
 
def on_message(client, userdata,msg):
    
    data = msg.payload.decode("utf-8", "strict")
    print("DataFromMQTT = ",data)
    f = open('sub_write_input.txt','a')
    f.write(data + '\n')
    f.close()
    #read_file()
    



    
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host)
client.loop_forever()

client.disconnect() # disconnect


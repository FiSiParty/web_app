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
    
    
    
    self.subscribe('topic1')
 
def on_message(client, userdata,msg):
    
    data = msg.payload.decode("utf-8", "strict")
    print(data)
    f = open('sub_write_input.txt','a')
    
    f.write(data + '\n')
    f.close()
    read_file()
    

def read_file():
    config = configparser.ConfigParser()
    a = []
    count = 0
    file1 = open('sub_write_input.txt', 'r') 
    Lines = file1.readlines()
    for line in Lines: 
        print("Line{}: {}".format(count, line.strip()))
        a.append(line.strip())
        count+=1
        if(count == 6):
            count=0
            
    print("count = ", count) 
#     print("a",a)
    con_a = len(a)
    print("con     ",con_a)
    
    if(con_a >= 6 and count == 0):
        
        if(os.path.isfile('sub_data.ini')==False):
            config[a[2]] = {"name": a[0],
                            "ip": a[1],
                            "id": a[2],
                            "register": a[3],
                            "datatype": a[4],
                            "readtype": a[5],
                            "precision": a[6],
                            "topic": a[7]
                            }
            with open('sub_data.ini','w') as configfile:
                config.write(configfile)
            print("wrote!!")
            a.clear()
            print("a_clean: ",a)
####            os.remove("mqtt_to_write.txt")
####            print("File Removed!")
####        
####            a.clear()
####            print("a_clean: ",a)
##        
        else:
            config.read('sub_data.ini')
            config[a[con_a-6]] = {"name": a[con_a-8],
                                    "ip": a[con_a-7],
                                    "id": a[con_a-6],
                                    "register": a[con_a-5],
                                    "datatype": a[con_a-4],
                                    "readtype": a[con_a-3],
                                    "precision": a[con_a-2],
                                    "topic": a[con_a-1]
                                     }
            
##            config[a[con_a-6]] = {"IP": a[con_a-5],
##                            "register": a[con_a-4],
##                            "readtype": a[con_a-3],
##                            "precision" : a[con_a-2],
##                            "topic" : a[con_a-1],
##                                }
            with open('sub_data.ini','w') as configfile:
                config.write(configfile)
            print("wrote!!")
##          
##        os.remove("mqtt_to_write.txt")
##        print("File Removed!")
        
##            a.clear()
##            print("a_clean: ",a)
                    

    
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host)
client.loop_forever()

client.disconnect() # disconnect


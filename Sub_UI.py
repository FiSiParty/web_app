import paho.mqtt.client as mqtt
import configparser
import os
host = 'siamgreenergy.com'
port = 1883



def on_connect(self, client, userdata, rc):
    print("MQTT Connected :" +str(rc))
    self.subscribe("eiei")
 
def on_message(client, userdata,msg):
    
    data = msg.payload.decode("utf-8", "strict")
    print(data)
    f = open('mqtt_to_write_ui.txt','a')
    
    f.write(data + '\n')
    f.close()
    read_file()
    

def read_file():
    config = configparser.ConfigParser()
    a = []
    count = 0
    file1 = open('mqtt_to_write_ui.txt', 'r') 
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
        
        if(os.path.isfile('sub_data_ui.ini')==False):
            config[a[0]] = {"IP": a[1],
                            "register": a[2],
                            "readtype": a[3],
                            "precision" : a[4],
                            "topic" : a[5],
                            }
            with open('sub_data_ui.ini','w') as configfile:
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
            config.read('sub_data_ui.ini')
            config[a[con_a-6]] = {"IP": a[con_a-5],
                            "register": a[con_a-4],
                            "readtype": a[con_a-3],
                            "precision" : a[con_a-2],
                            "topic" : a[con_a-1],
                                }
            with open('sub_data_ui.ini','w') as configfile:
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


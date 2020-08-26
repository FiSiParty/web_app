import configparser
import os

i =0
file1 = open('sub_write_UI.txt', 'r') 
Lines = file1.readlines()
for line in Lines:
    i += 1
i = i//9
file1.close()
print("i = ",i)

while (i>0):
    config = configparser.ConfigParser()
    a = []
    count = 0
    file1 = open('sub_write_UI.txt', 'r') 
    Lines = file1.readlines()
    l_a = 0

    for line in Lines:
        element = line.strip()
        print("Line{}: {}".format(count, line.strip()))
        a.append(line.strip())
        count+=1
        print("count in loop LINES: ", count)
        if(count == 9):
            print("set c to 0")
            count=0
        print("next loop Lines")
        l_a+=1
        print("l_a = ",l_a)
                
    print("count = ", count) 
    print("a",a)
    con_a = len(a)
    print("con     ",con_a)

    if(con_a >= 9 and count == 0):
        if(os.path.isfile('sub_data_UI.ini')==False):
            config[a[2]] = {"name": a[0],
                            "ip": a[1],
                            "id": a[2],
                            "register": a[3],
                            "datatype": a[4],
                            "readtype": a[5],
                            "precision": a[6],
                            "topic": a[7],
                            "answer": a[8]
                            }
            with open('sub_data_UI.ini','w') as configfile:
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
            config.read('sub_data_UI.ini')
            config[a[con_a-7]] = {"name": a[con_a-9],
                                    "ip": a[con_a-8],
                                    "id": a[con_a-7],
                                    "register": a[con_a-6],
                                    "datatype": a[con_a-5],
                                    "readtype": a[con_a-4],
                                    "precision": a[con_a-3],
                                    "topic": a[con_a-2],
                                    "answer": a[con_a-1]
                                     }
            
    ##            config[a[con_a-6]] = {"IP": a[con_a-5],
    ##                            "register": a[con_a-4],
    ##                            "readtype": a[con_a-3],
    ##                            "precision" : a[con_a-2],
    ##                            "topic" : a[con_a-1],
    ##                                }
            with open('sub_data_UI.ini','w') as configfile:
                config.write(configfile)
            print("wrote!!")
    ##          
    ##        os.remove("mqtt_to_write.txt")
    ##        print("File Removed!")
        
    ##            a.clear()
    ##            print("a_clean: ",a)
    i-=1
file1.close()
#os.system('deletebycmd_UI.cmd')
print("sub_write_UI.txt Removed!")

                    

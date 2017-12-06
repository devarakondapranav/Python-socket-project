import socket
import _thread
import time

def server(name, port):
    s = socket.socket()
    host = "192.168.15.8"
    
    #port = 5007
    s.bind((host, port))
    while True:
        print( name +" ready....waiting for clients")
          
        s.listen(1)
        c,addr = s.accept()
        print("Client connected: " + str(addr))
        filename = c.recv(1024)
        
        filename = filename.decode("utf-8")
        if(filename[0] =="1"):#reqFile in new.py
            f = open(filename[1:], "r")
            data = f.read()
            if(len(data) == 0):
                data = "-1"
            data = str.encode(data)
            c.send(data)
        elif(filename[0] =="2"):#send_mess in new.py
            dest = filename[1:13]
            message = filename[13:]
            try:
                f = open(dest+".txt", "a")
                f.write(message)
                f.close()
            except:
                pass
        elif(filename[0] == "3"):#register in new.py
            content = filename[1:]
            hallticket = content.split(" ")[0]
            f = open("names.txt", "a")
            f.write(content)
            f.close()
            f1 = open(hallticket+".txt", "w")
            f1.close()
            f2 = open(hallticket+"status.txt", "w")
            f2.write("Hey there I am using python socket network")
            #f2.write(content)
            f2.close()
        elif(filename[0] == "4"):
            content = filename.split("*")
            hallticket = content[1]
            f = open(hallticket+"status.txt", "w")
            f.write(content[2])
            f.close()

    s.close()



try:
   _thread.start_new_thread( server, ("Server-1",5002, ) )
   _thread.start_new_thread( server, ("Server-2",5003, ) )
except:
   print ("Unable to start thread")

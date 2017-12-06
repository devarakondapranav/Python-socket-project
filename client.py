import time
import socket
current_status = 0

current_user = ""

def reqFile(filename):
    host = "192.168.15.8"
    port = 5002
    s = socket.socket()
    s.connect((host, port))
    filenameBytes = str.encode("1"+filename)
    s.send(filenameBytes)
    data = s.recv(1024)
    data = data.decode("utf-8")
    s.close()
    return(data)
    
def send_mess(message):
    host = "192.168.15.8"
    port = 5002
    s = socket.socket()
    s.connect((host, port))
    #message = str.encode(message)
    s.send(message)
    s.close()

def register(details):
    host = "192.168.15.8"
    port = 5002
    s = socket.socket()
    s.connect((host, port))
    #message = str.encode(message)
    s.send(details)
    s.close()


def upd_status(status):
    host = "192.168.15.8"
    port = 5002
    s = socket.socket()
    s.connect((host, port))
    s.send(status)
    s.close()
    
#print("Hi")   
#los = reqFile("names.txt").split("**")

#print("Bye")
while (True):
    try:
        los = reqFile("names.txt").split("**")
        if(current_status == 0):
            print("Namasthe")
            print("****************")
            print("1)Login \n2)Signup")
            uc = input()
            if(int(uc) ==1):
                print("Enter your hall ticket no")
                hallticket = (input())
                if(int(hallticket) > 160116733000 and int(hallticket) < 160116733060):
                    print("Enter your password")
                    password = input()
                    
                    for i in los:
                        x = i.split(" ")
                        if(x[0] == hallticket and x[2]==password):
                            print("Login successful \nWelcome " + x[1])
                            current_user = x[1]
                            current_status = 1
                            break
                    if current_status!=1:
                        print("You entered the wrong password")
                        time.sleep(1)
            elif(int(uc) == 2):
                print("Enter your hall ticket no")
                hallticket = input()
                exist = 0
                for i in los:
                    x = i.split(" ")
                    if(x[0] == hallticket):
                        exist = 1
                        print("You are already on the network.Please login first")
                        
                        time.sleep(1)
                if exist==0:
                    if(int(hallticket) > 160116733000 and int(hallticket) < 160116733060):
                        print("Enter your name")
                        current_user = input()
                        print("Enter a password")
                        password = input()
                        details = ("3" + hallticket + " " + current_user + " " + password + "**")
                        details = str.encode(details)
                        register(details)
                        print("Congrats " + current_user + "! You have signed up for the network")
                        current_status = 1
                        
        elif(current_status ==1):
            print("1) Check status\n2)Send messages 3)See messages 4)Send an anonymous message 5)Logout")
            action = input()
            if(int(action) ==5):
                print("Logged out successfully")
                print("See you soon " + current_user + "!!!")
                current_status = 0
                current_user = ''
            elif(int(action) == 2):
                print("The following students are on the network")
                los = reqFile("names.txt").split("**")
                for i in range(len(los)-1):
                    x = los[i].split(" ")
                    if(x[1]!=current_user):
                        print(str(i+1)+ ". " + x[0] + " " + x[1])
                print("Whom do you want to send the message(hall ticketno)")
                dest = input()
                
                exist = 0
                for i in range(len(los)-1):
                    x = los[i].split(" ")
                    if((i+1)) == int(dest):
                        exist = 1
                        print("Enter the message")
                        message = input()
                        send_mess(str.encode("2"+x[0] +time.ctime() + " :: Message from " + current_user+ ":- "+message+"**"))
                        print("Successful")
                        time.sleep(2)
                if not exist:
                    print(dest + "is not on the network yet, cannnot send message. Select someone who is on the network")
            elif(int(action) == 3):
                print("Fetching your messages....")
                time.sleep(1)
                
                messages = reqFile(hallticket+".txt")
                if(messages=="-1"):
                    print("Sorry you have no messages yet..")
                else:
                    messages = messages.split("**")
                    for i in messages:
                        print(i)
                print("********")
                time.sleep(2)
            elif(int(action) == 1):
                for i in range(len(los) -1):
                    x = los[i].split(" ")
                    status = reqFile(x[0]+"status.txt")
                    print(x[1] + " :: " + status)
                    time.sleep(0.25)
                print("Enter 1 to change your status")
                print("Enter 2 to go back")
                choice_user = input()
                if (choice_user == "1"):
                    print("Enter a new status")
                    new_status = input()
                    l = "4*"+hallticket + "*"+new_status;
                    l = str.encode(l)
                    upd_status(l)
                    print("You have updated your status successfully")
                    print("********")
                    time.sleep(2)
            elif (int(action) == 4):
                print("The following students are on the network")
                los = reqFile("names.txt").split("**")
                for i in range(len(los)-1):
                    x = los[i].split(" ")
                    if(x[1]!=current_user):
                        print(str(i+1) + "." + x[0] + " " + x[1])
                print("Whom do you want to send the anonymous message(hall ticketno)?")
                dest = input()
                exist = 0
                for i in range(len(los)-1):
                    x = los[i].split(" ")
                    if(i+1) == int(dest):
                        exist = 1
                        print("Enter the message")
                        message = input()
                        send_mess(str.encode("2"+x[0] +time.ctime() + " !!! Anonymous message!!! " + " :- "+message+"**"))
                        print("Successful")
                        time.sleep(2)
                if not exist:
                    print(dest + "is not on the network yet, cannnot send message. Select someone who is on the network")


            else:
                print("Choose a valid option")
    except ValueError:
        print("Arey waste fellow dont click enter without entering any value");

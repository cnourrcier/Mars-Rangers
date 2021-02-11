import socket
from threading import *

#setting up a file for the server to write to.


class Communications(Thread):
    #function that build the thread and identifies the rover name
    def __init__(self,socket,address):
        Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.start()
     
    def run(self):
        #if file does not already exist, this will create one
        txtFile = open("roverInfoFile.txt","w") 
        while True:
            client_msg = self.socket.recv(1024).decode()
            print('Client sent: ', client_msg)
            self.socket.send(b'Message was received.')
            #write the received client data to a text file called txtFile.txt
            txtFile.write(client_msg + '\n')
            txtFile.flush()
        
        txtFile.close()
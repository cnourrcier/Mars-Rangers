from ClassTest import Communications
import socket
from threading import *
import signal

#setting up server connection
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
#host = 'put your ip address here'
port = 5555

#error checking to make sure that the socket actually binded to the address
try:
    serversocket.bind((host,port))
except socket.error as e:
    print(str(e))

# When ctl+c is pressed, the server will immediately jump to this function.
# The purpose of this function will be to manually disconnect a client from the server.
def keyboardInterruptHandler(signal, frame):
        pass
        
def main():
    #Starting messages
    print("The Rover Server is Starting:......")
    print("The Host IP is: " + host)
    print("Port that is listening: " + str(port))
    print(socket.gethostname())
    
    #this is listing for the clients to connect 
    serversocket.listen(5)

    #This loop will use the class to build the threading for the rover
    # --Note: need to create additional statement to address if connection fails
    while True:
        clientsocket,address = serversocket.accept()
        Communications(clientsocket,address)
        signal.signal(signal.SIGINT, keyboardInterruptHandler)
    #important need to close files!!
    serversocket.close()

main()
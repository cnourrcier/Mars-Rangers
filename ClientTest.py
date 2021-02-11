import socket
from RoverNameClass import RoverName
import time
from datetime import date, datetime

roverSocket = socket.socket()
host = socket.gethostbyname(socket.gethostname())
#host = 'put your ip address here'
port = 5555
roverSocket.connect((host,port))


def sendData(message):
    roverSocket.send(message.encode())
    data = ""
    data = roverSocket.recv(1024).decode()
    print("Server sent :", data)

roverBilly = RoverName("Billy")

print(roverBilly.name)

while True:
    # message = input()
    current_date = date.today()
    current_time = datetime.now()
    d = current_date.strftime("%m/%d/%y")
    t = current_time.strftime("%H:%M:%S")
    
    sendData(roverBilly.name + ': ' + 'DATE: ' + d + ' TIME: ' + t )
    sendData('Location: ' + '15' + u'\N{DEGREE SIGN}' + 'N, ' + '30' + u'\N{DEGREE SIGN}' + 'E')
    sendData('Temperature: ' + '75' + u'\N{DEGREE SIGN}' + 'F')

    # sendData(message)
    time.sleep(5)
    
roverSocket.close()

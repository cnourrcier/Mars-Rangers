import socket
from RoverNameClass import RoverName
import time
import RPi.GPIO as GPIO
import dht11
import datetime

roverSocket = socket.socket()
host = "192.168.0.13"
port = 5555
roverSocket.connect((host,port))

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# define the sensor data pin
instance = dht11.DHT11(pin=27) # works on pin 4, 14, 17, 27,

def sendData(message):
    roverSocket.send(message.encode())
    data = ""
    data = roverSocket.recv(1024).decode()
    print("Server sent :", data)

roverBilly = RoverName("Billy")

print(roverBilly.name)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            sendData("Last valid input: " + str(datetime.datetime.now()))
            sendData("Temperature: %-3.1f C" % result.temperature)
            sendData("Humidity: %-3.1f %%" % result.humidity)

        time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()


    # message = input()
    #current_date = date.today()
    #current_time = datetime.now()
    #d = current_date.strftime("%m/%d/%y")
    #t = current_time.strftime("%H:%M:%S")
    
    #sendData(roverBilly.name + ': ' + 'DATE: ' + d + ' TIME: ' + t )
    #sendData('Location: ' + '15' + u'\N{DEGREE SIGN}' + 'N, ' + '30' + u'\N{DEGREE SIGN}' + 'E')
    #sendData('Temperature: ' + '75' + u'\N{DEGREE SIGN}' + 'F')

    # sendData(message)
    #time.sleep(5)
    
roverSocket.close()
# Mars-Rangers

I am developing communication code designed for a server and three clients. Each client will be an identical 6 wheel rover with identical functions using Raspberry Pis. These functions include: 

1) Autonomous choreographed movement based on a premeditated scenerio.
2) DHT11 Temperature and Humidity sensing and data collecting.
3) GPS location.
4) PiCamera picture taking.
5) Communication via sockets, each client will send and receive data to and from the server. 

The scenario: A client will send its GPS location to the server. Based on this location, the server will calculate equidistant peripheral points North, South, East, and West. Then the server will assign each rover one of these calculated points, and all three will move to their respective location. Once the rovers are in place, they will collect temperature and humidity data, and send it to the server with a timestamp. The server will then store this data in a database. After a designated period of time, a rover will move to a new location, and the scenario will restart and repeat.

Depending on progress, I will add PiCamera functions and other additions along the way if time permits. 

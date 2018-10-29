# importing socket module
import socket
# importing RPI gpio plugin
import RPi.GPIO as GPIO
# importing time but not used
import time

HOST = '192.168.1.45'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
# the type of socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to the socket
s.connect((HOST, PORT))


# looping throught the pins
while True:
	# defining pin1
	pin1 = 14
	# defining pin2
	pin2 = 15
	# gpio mode set to bcm
	GPIO.setmode(GPIO.BCM)
	# turn off warnings
	GPIO.setwarnings(False)
	# saying that pin2 will be out so that we turn on the led
	GPIO.setup(pin1,GPIO.OUT)
	# saying that pin2 will receive data
	GPIO.setup(pin2,GPIO.IN)
	# grabbing the data of pin2
	sensor = GPIO.input(pin2)
	# checking if the data is true so if the thing is broken (intruder)
	if sensor == 1:
		# turning on the led on pin1
		GPIO.output(pin1,GPIO.HIGH)
		# making data true that will be send later on
		data = 'True'
	# else if the chain is not broken turn of the led on pin 1
	else:
		# turning of the led
	 	GPIO.output(pin1,GPIO.LOW)
		# also data always can be handy
	 	data = 'False'
	# sending the data to the server
	s.sendall(data)
	# look if data is received
	data = s.recv(1024)
import socket

import RPi.GPIO as GPIO
import time

HOST = '192.168.1.45'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))



while True:
	pin1 = 14
	pin2 = 15
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pin1,GPIO.OUT)
	GPIO.setup(pin2,GPIO.IN)
	sensor = GPIO.input(pin2)
	if sensor == 1:
		GPIO.output(pin1,GPIO.HIGH)
		data = 'True'
	else:
	 	GPIO.output(pin1,GPIO.LOW)
	 	data = 'False'
	s.sendall(data)
	data = s.recv(1024)
	# print('Received', repr(data))
	# print(data)
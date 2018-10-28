import socket
import sys
import RPi.GPIO as GPIO

HOST = '192.168.1.45'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(20)
conn, addr = s.accept()
print('Connected by', addr)
green = 15
red = 14
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)	
GPIO.output(green,GPIO.LOW)
GPIO.output(red,GPIO.LOW)
# GPIO.output(green,GPIO.HIGH)
while True:
    data = conn.recv(10)
    if data == 'False':
    	bol = True
    else:
    	bol = False
    	# GPIO.output(green,GPIO.HIGH)
    	# sleep(10)
    	# GPIO.output(red,GPIO.LOW)
		# GPIO.output(red,GPIO.HIGH)
		# sleep(10)
		# GPIO.output(red,GPIO.LOW)
    conn.sendall('hi')
    print(bol)
    if bol:
    	GPIO.output(green,GPIO.HIGH)
    else:
    	GPIO.output(red,GPIO.HIGH)
	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.LOW)
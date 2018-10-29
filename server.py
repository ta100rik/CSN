# importing some modules to run the system
import socket
import sys
import RPi.GPIO as GPIO
import time
# defining listen ip
HOST = '192.168.1.45'  # Standard loopback interface address (localhost)
# defining port to listen to
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
# defining type of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding the host to the socket and the port so the socket will no what he/she is
s.bind((HOST, PORT))
# listening to the socket
s.listen(20)
# look if connection is accepted and is completed
conn, addr = s.accept()
# print that the things is connected
print('Connected by', addr)
# define pins where led is green or red
green = 15
red = 14
# turning the mode of the GPIO pins to BCM
GPIO.setmode(GPIO.BCM)
# don't show warnings
GPIO.setwarnings(False)
# say that green en red ar both will send energy (bits) out
GPIO.setup(green,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
# turn of all the lamps to be sure the that no 2 lamps will burn at the same time
GPIO.output(green,GPIO.LOW)
GPIO.output(red,GPIO.LOW)
# looking for data loop
while True:
    # the received data will be in data
    data = conn.recv(10)
    # checking if data is false or true
    # when false green light will burn because system is on
    if data == 'False':
    	bol = True
    else:
    	bol = False
    # send something random back just to be sure that the package is received
    conn.sendall('hi')
    # printing the status of the lamp
    print(bol)
    # turning on the right light by checking the bolean above
    if bol:
    	GPIO.output(green,GPIO.HIGH)
    else:
    	GPIO.output(red,GPIO.HIGH)
        # let the thing sleep because the red light need to be on for a while
        time.sleep(10)
    #turning of every lamp and check what the new status is
	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.LOW)
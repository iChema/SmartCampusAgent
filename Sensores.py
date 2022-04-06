
import serial
import time
import numpy as np

MAX_BUFF_LEN = 255

typeSensor = ['CO2','CO','Sound','Humidity','Temperature °C','Temperature °F','Heat index °C', 'Heat index °F']
sensors = [0,0,0,0,0,0,0,0]

# Serial port(windows-->COM), baud rate, timeout msgse
port = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)

# read one char (default)
def read_ser(num_char = 1):
	string = port.read(num_char)
	return string.decode()

# Write whole strings
def write_ser(cmd):
	cmd = cmd + '\n'
	port.write(cmd.encode())


def main():
    write_ser("SENSORS")
    string = read_ser(MAX_BUFF_LEN)
    if(len(string)):
        sensors = string.split(',')
    return sensors

def onOff(status):
    write_ser(status)

# Super loop
'''
while True:
    string = read_ser(MAX_BUFF_LEN)
    if(len(string)):
        sensors = string.split(',')
        sensores = np.array([typeSensor,sensors])
        print(sensores)
    write_ser("True")
'''
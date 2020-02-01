import time
import serial

class SerialEx:
    '''Manages Serial connection and behavior'''
    def __init__(self):        
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=.5);

        print('serial communication initiated')
        
    def sendData(self, data):
        print('Data : ' + data)
        self.ser.write(str.encode(data))
        time.sleep(1)
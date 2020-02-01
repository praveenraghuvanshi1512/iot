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
    
    def blinkLed(self):
        print('**** GPIOEX::Person Detected')
        if(self.ser.isOpen()):
            print('LED On')
            self.ser.write(str.encode('LED ON'))
            self.turnOnATCommands()
            time.sleep(2)
            print('LED Off')
            self.turnOffATCommands()
        
    def turnOnATCommands(self):
        print('Turn on')
        self.ser.write(str.encode('+++'))
        time.sleep(0.5)
        print(self.ser.read(100))
        time.sleep(2)
        self.ser.write(str.encode('ATD05\r\n'))
        time.sleep(0.5)
        print(self.ser.read(100))
        self.ser.write(str.encode('ATDCN\r\n'))
        time.sleep(0.5)
        print(self.ser.read(100))
                
    def turnOffATCommands(self):
        self.ser.write(str.encode('+++'))
        time.sleep(2)
        self.ser.write(str.encode('ATD04\r\n'))
        self.ser.write(str.encode('ATDCN\r\n'))
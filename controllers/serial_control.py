import serial
from time import sleep
from settings import config

class ArduinoSerial:

    def __init__(self):
        self.serial = serial.Serial(
            port    =config()['port'],\
            baudrate=config()['baudrate'],\
            parity  =serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout =config()['timeout']
        )

    def bytes_to_int(self, bytes):
        result = 0
        for b in bytes:
            result = result * 256 + int(b)
        return result

    def read(self):
        # Get decoded serial output
        read = self.serial.readline().decode()
        return read

    def write_byte(self, byte):
        self.serial.write(byte)
        return

    def close(self):
        self.serial.close()
        return
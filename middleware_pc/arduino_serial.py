import serial
import time

class ArduinoSerial:
    def __init__(self, port='COM3', baud=115200):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)  # Let Arduino reset

    def send(self, message):
        self.ser.write((message + '\n').encode())

    def read(self):
        if self.ser.in_waiting:
            return self.ser.readline().decode().strip()
        return None

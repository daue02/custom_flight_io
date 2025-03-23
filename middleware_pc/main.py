from arduino_serial import ArduinoSerial
from xplane_udp import XPlaneUDPReceiver
import time

arduino = ArduinoSerial(port='COM3', baud=115200)
xplane = XPlaneUDPReceiver(port=49003)

last_alt = None

while True:
    alt = xplane.listen()
    if alt is not None:
        alt_rounded = int(alt)
        if alt_rounded != last_alt:
            arduino.send(f"ALT:{alt_rounded}")
            last_alt = alt_rounded
            print(f"Sent to Arduino: ALT:{alt_rounded}")

    msg = arduino.read()
    if msg:
        print(f"Arduino sent: {msg}")

    time.sleep(0.05)

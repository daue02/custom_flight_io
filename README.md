## Project Overview
This repo contains:
- `firmware_arduino/`: Embedded firmware for Arduino Mega 2560 using PlatformIO.
- `middleware_pc/`: Python middleware that communicates with X-Plane 12 and forwards sim data to the Arduino via Serial.

## How to Run:
1. Flash Arduino using PlatformIO (`cd firmware_arduino && pio run -t upload`)
2. Install PC dependencies (`pip install -r middleware_pc/requirements.txt`)
3. Run middleware script (`python middleware_pc/main.py`)

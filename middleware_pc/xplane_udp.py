import socket
import struct

class XPlaneUDPReceiver:
    def __init__(self, port=49003):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', port))

    def listen(self):
        data, _ = self.sock.recvfrom(1024)
        return self.parse_altitude(data)

    def parse_altitude(self, data):
        # Dummy parse for now: Assume altitude is at byte offset 8-12
        # Real X-Plane packets use complex struct; will fix later
        try:
            header = data[:5].decode()
            if header != 'DATA@':
                return None

            # Simplified assumption: first record, altitude at offset 8–12
            # Skip header (5 bytes), index (4 bytes), get float at next 4 bytes
            altitude_bytes = data[9:13]
            altitude = struct.unpack('<f', altitude_bytes)[0]
            return altitude
        except:
            return None

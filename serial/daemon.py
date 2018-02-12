import re
from serial import Serial
from mpd import MPDClient

client = MPDClient()

IS_TAG = re.compile("^[0-9A-F]+$")


with Serial(port="/dev/ttyACM0", baudrate=115200, timeout=1, writeTimeout=1) as serial_port:
    if serial_port.isOpen():
        previous_line = None
        while True:
            line = serial_port.readline()
            line = line.decode().strip()
            if not IS_TAG.match(line):
                continue

            if line == '0000000':
                action = "stop"
            else:
                action = "play"

            if action is not None:
                try:
                    client.connect("localhost", 6600)
                    if action == "stop" and previous_line:
                        print("Stopping", previous_line)
                        client.stop()
                        previous_line = None
                    elif action == "play":
                        print("Starting", line)
                        client.clear()
                        client.load(str(line))
                        client.play(0)
                        previous_line = line
                except Exception as e:
                    print('Error', e)
                finally:
                    client.close()
                    client.disconnect()

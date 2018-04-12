import signal
import sys

from pirc522 import RFID


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def hexlify_uid(uid):
    return ''.join('{:02x}'.format(byte) for byte in uid).upper()


rc522 = RFID()
previous_uid = None


while True:
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()
    if not error:
        (error, uid) = rc522.anticoll()
        uid = hexlify_uid(uid)
        if not error:
            if uid != previous_uid:
                previous_uid = uid
                print("UID: " + str(uid))
        else:
            if previous_uid:
                print("Tag removed")
            previous_uid = None
    else:
        if previous_uid:
            print("Tag removed")
        previous_uid = None

from pirc522 import RFID
from mpd import MPDClient


rc522 = RFID()
client = MPDClient()

previous_uid = None
while True:
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error:
        (error, uid) = rc522.anticoll()
        if not error:
            if uid != previous_uid:
                action = "play"
        else:
            action = "stop"
    else:
        action = "stop"

    try:
        client.connect("localhost", 6600)
        if action == "stop" and previous_uid:
            print("Stopping", previous_uid)
            client.stop()
            previous_uid = None
        elif action == "play":
            print("Starting", uid)
            client.clear()
            client.load(str(uid))
            client.play(0)
            previous_uid = uid
    except Exception as e:
        print('Error', e)
    finally:
        client.close()
        client.disconnect()

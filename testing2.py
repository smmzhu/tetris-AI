from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
time.sleep(1)
for x in range(100):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    
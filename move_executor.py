import time
from pynput.keyboard import Key, Controller
from tetris import keyboard
import random
delay_time = random.uniform(0.03,0.03)

def delay():
    time.sleep(delay_time)
def execute(IfSave, rotations, lane):
    if IfSave:
        keyboard.press("c")
        keyboard.release("c")
        delay()

    if rotations == 3:
        keyboard.press("z")
        keyboard.release("z")
        delay()
    else:
        for x in range(rotations):
            keyboard.press("x")
            keyboard.release("x")
            delay()
    
    dlane = lane - 4
    if dlane > 0:
        for x in range(dlane):
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            delay()
    elif dlane < 0:
        for x in range(abs(dlane)):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            delay()

    keyboard.press(Key.space)
    keyboard.release(Key.space)
    delay()

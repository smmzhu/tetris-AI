from pynput import keyboard
from pynput.mouse import Button, Controller
from tetris import mouse

first_coordinates = None
second_coordinates = None
third_coordinates = None
fourth_coordinates = None
fifth_coordinates = None
running = True
def on_press(key):
    global first_coordinates,second_coordinates,third_coordinates,fourth_coordinates,fifth_coordinates
    global running
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == "1":
            print(mouse.position)
            first_coordinates = mouse.position
        elif key.char == "2":
            print(mouse.position)
            second_coordinates = mouse.position
        elif key.char == "3":
            print(mouse.position)
            third_coordinates = mouse.position
        elif key.char == "4":
            print(mouse.position)
            fourth_coordinates = mouse.position
        elif key.char == "5":
            print(mouse.position)
            fifth_coordinates = mouse.position
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    global running
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        running = False
        # Stop listener
        return False

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
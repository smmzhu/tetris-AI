import pynput
from pynput.mouse import Button
mouse = pynput.mouse.Controller()
from PIL import ImageGrab

def check_color(input_color,actual_color):
    for x in range(3):
        if abs(input_color[x] - actual_color[x]) > 20:
            return False
    return True

def isEmptyColor(input_color):
    r,g,b,a = input_color
    if abs(r - 248) < 6 and abs(g - 200) < 6 and abs(b - 69) < 6: #if its the countdown font then void it
        return True
    if r > 60 or g > 60 or b > 60:
        return False
    return True

def match_color(rgb):

    #using rgb of a falling block
    purple_rgb = [207,80,202]
    green_rgb = [188,242,87]
    red_rgb = [229,68,68]
    blue_rgb = [85,71,217]
    orange_rgb = [231,127,65]
    yellow_rgb = [242,213,86]
    light_blue_rgb = [118,242,177]

    if check_color(rgb,purple_rgb):
        return "purple"
    elif check_color(rgb,green_rgb):
        return "green"
    elif check_color(rgb,red_rgb):
        return "red"
    elif check_color(rgb,blue_rgb):
        return "blue"
    elif check_color(rgb,orange_rgb):
        return "orange"
    elif check_color(rgb,yellow_rgb):
        return "yellow"
    elif check_color(rgb,light_blue_rgb):
        return "light blue"

    #using rgb values of queued blocks
    purple_rgb = [152,70,150] 
    green_rgb = [143,178,73]
    red_rgb = [175,61,63]
    blue_rgb = [75,65,159]
    orange_rgb = [169,102,60]
    yellow_rgb = [175,163,69]
    light_blue_rgb = [92,176,135]

    if check_color(rgb,purple_rgb):
        return "purple"
    elif check_color(rgb,green_rgb):
        return "green"
    elif check_color(rgb,red_rgb):
        return "red"
    elif check_color(rgb,blue_rgb):
        return "blue"
    elif check_color(rgb,orange_rgb):
        return "orange"
    elif check_color(rgb,yellow_rgb):
        return "yellow"
    elif check_color(rgb,light_blue_rgb):
        return "light blue"
    else:
        return "Not a Color"

if __name__ == "__main__":
    pass

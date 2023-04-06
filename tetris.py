import pynput
from pynput.mouse import Button
from pynput.keyboard import Key
import time
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

from board_generator import generate_board
from rgb_detector import return_color
import keylogger
import main_brain
from main_brain import best_move
from move_executor import execute
from put_piece_on_board import calc_board
from clear_lines import clear_lines
from print_board_module import print_board
from rgb_detector import grab_board_from_screen
import random

def main():
    board = generate_board()
    running = True
    top_left = None
    bottom_right = None
    while running:
        #from keylogger import first_coordinates, second_coordinates,third_coordinates, fourth_coordinates, fifth_coordinates
        if mouse.position == (0.0,0.0): #failsafe/breakloop
            running = False
        if mouse.position == (1439.984375, 0.0):
            #board = generate_board() #only used if board is not manually detected
            pass
        
        #hardcoded values:
        first_coordinates = (708,236)
        second_coordinates = (522,321)
        third_coordinates = (926,310)
        fourth_coordinates = (602,260)
        fifth_coordinates = (838,752)
        #hardcoded values end

        color1 = return_color(first_coordinates) #1 is falling
        color2 = return_color(second_coordinates) #2 is hold
        color3 = return_color(third_coordinates) #3 is queued
        top_left = fourth_coordinates #4 is top left bound
        bottom_right = fifth_coordinates #5 is bottom right bound
        first_color = color1
        second_color = color2
        if second_color == "Not a Color":
            second_color = color3
        print(first_color, second_color)
        if top_left != None and bottom_right != None:
            #start = time.time()
            board = grab_board_from_screen(top_left, bottom_right)
            #print(time.time()-start)
        print_board(board)
        if first_color != "Not a Color" and second_color != "Not a Color" and top_left != None and bottom_right != None:
            IfSave, rotations, lane = best_move(first_color,second_color,board)
            print(IfSave, rotations, lane)
            execute(IfSave, rotations, lane)
            color = first_color
            if IfSave:
                color = second_color
            
            #board, positions = calc_board(color,rotations,lane,board)
            #board = clear_lines(board)

        time.sleep(random.uniform(0.03,0.03)) #low is 0.03

if __name__ == "__main__":
    main()




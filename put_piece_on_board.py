import copy
import board_generator
from board_generator import generate_board
from print_board_module import print_board
from clear_lines import clear_lines
class OverlapError(Exception):
    "There seems to be some overlap"
def calc_board(color, rotns, lane, board):
    #create positions (prolly just hard code all these)
    positions = []
    (x,y) = [lane,20]
    positions.append([x,y])
    if color == "purple":
        if rotns == 0:
            positions.append([x,y + 1])
            positions.append([x - 1,y])
            positions.append([x + 1,y])
        elif rotns == 1:
            positions.append([x,y + 1])
            positions.append([x,y - 1])
            positions.append([x + 1, y])
        elif rotns == 2:
            positions.append([x,y - 1])
            positions.append([x - 1,y])
            positions.append([x + 1,y])
        elif rotns == 3:
            positions.append([x,y + 1])
            positions.append([x,y - 1])
            positions.append([x - 1, y])
    elif color == "green":
        if rotns == 0:
            positions.append([x,y + 1])
            positions.append([x - 1,y])
            positions.append([x + 1,y + 1])
        elif rotns == 1:
            positions.append([x,y + 1])
            positions.append([x + 1,y])
            positions.append([x + 1,y - 1])
    elif color == "red":
        if rotns == 0:
            positions.append([x - 1,y + 1])
            positions.append([x,y + 1])
            positions.append([x + 1,y])
        elif rotns == 1:
            positions.append([x + 1,y + 1])
            positions.append([x + 1,y])
            positions.append([x,y - 1])
    elif color == "blue":
        if rotns == 0:
            positions.append([x - 1,y + 1])
            positions.append([x - 1,y])
            positions.append([x + 1,y])
        elif rotns == 1:
            positions.append([x + 1,y + 1])
            positions.append([x,y + 1])
            positions.append([x,y - 1])
        elif rotns == 2:
            positions.append([x - 1,y])
            positions.append([x + 1,y])
            positions.append([x + 1,y - 1])
        elif rotns == 3:
            positions.append([x,y + 1])
            positions.append([x,y - 1])
            positions.append([x - 1,y - 1])
    elif color == "orange":
        if rotns == 0:
            positions.append([x + 1,y + 1])
            positions.append([x - 1,y])
            positions.append([x + 1,y])
        elif rotns == 1:
            positions.append([x + 1,y - 1])
            positions.append([x,y + 1])
            positions.append([x,y - 1])
        elif rotns == 2:
            positions.append([x - 1,y])
            positions.append([x + 1,y])
            positions.append([x - 1,y - 1])
        elif rotns == 3:
            positions.append([x,y + 1])
            positions.append([x,y - 1])
            positions.append([x - 1,y + 1])
    elif color == "yellow":
        positions.append([x,y - 1])
        positions.append([x + 1,y])
        positions.append([x + 1,y - 1])
    elif color == "light blue":
        if rotns == 0:
            positions.append([x - 1,y])
            positions.append([x + 1,y])
            positions.append([x + 2,y])
        elif rotns == 3:
            positions.append([x,y + 1])
            positions.append([x,y - 1])
            positions.append([x,y - 2])
    
    for position in positions:
        x,y = position
        if board[x][y] == 1:
            return "Error" 
    Landed = False
    while True:
        old_positions = copy.deepcopy(positions)
        positions = []
        for position in old_positions:
            x,y = position
            y -= 1
            positions.append([x,y])
        for position in positions:
            x,y = position
            if board[x][y] == 1 or y == -1:
                old_positions = copy.deepcopy(positions)
                positions = []
                for position in old_positions:
                    x,y = position
                    y += 1
                    positions.append([x,y])
                Landed = True
                break
        if Landed:
            break
    for (x,y) in positions:
        if board[x][y] == 1:
            raise OverlapError("its updating wrong")
        board[x][y] = 1

    #board = clear_lines(board)
    return board, positions

if __name__ == "__main__":
    test_board = generate_board()
    test_board, positions = calc_board("light blue",1,0,test_board)
    test_board, positions = calc_board("purple",0,7,test_board)
    test_board, positions = calc_board("blue",0,2,test_board)
    test_board, positions = calc_board("red",0,4,test_board)
    test_board, positions = calc_board("yellow",0,5,test_board)
    test_board, positions = calc_board("orange",2,3,test_board)
    test_board, positions = calc_board("green",1,7,test_board)
    test_board, positions = calc_board("yellow",0,0,test_board)
    print_board(test_board)
import board_grader
from board_grader import grade_board
import board_generator
from board_generator import generate_board
import poss_instructions
from poss_instructions import poss_instructions
import put_piece_on_board
from put_piece_on_board import calc_board
from print_board_module import print_board
from tetris_ready_checker import isTetrisReady
from hole_checker import hasHoles
import time
import copy

def best_move(first_piece,second_piece,board):
    lowest_score = 1000000000
    IfSave = None
    final_rotations = None
    final_lane = None
    tetrisReady = isTetrisReady(board)
    doesHaveHoles = hasHoles(board)

    #the whole process is 
    first_instructions = poss_instructions(first_piece, includeTetris = tetrisReady, hasHoles = doesHaveHoles)
    for instruction in first_instructions:
        rotns, lane = instruction
        board, positions = calc_board(first_piece,rotns,lane,board)
        score = grade_board(board)
        if score < lowest_score:
            lowest_score = score
            final_rotations = rotns
            final_lane = lane
            IfSave = False    
        for (x,y) in positions:
            board[x][y] = 0
    second_instructions = poss_instructions(second_piece, includeTetris = tetrisReady, hasHoles = doesHaveHoles)
    for instruction in second_instructions:
        rotns, lane = instruction
        board, positions = calc_board(second_piece,rotns,lane,board)
        score = grade_board(board)
        if score < lowest_score:
            lowest_score = score
            final_rotations = rotns
            final_lane = lane
            IfSave = True
        for (x,y) in positions:
            board[x][y] = 0
    
    return IfSave, final_rotations, final_lane

if __name__ == "__main__":
    start = time.time()
    test_board = generate_board()
    #IfSave, rotations, lane = best_move("blue","red",test_board)
    test_board[0][0] = 1
    test_board[0][1] = 1
    test_board[1][0] = 1
    test_board[2][0] = 1
    IfSave, rotations, lane = best_move("red","green",test_board)
    print(IfSave,rotations,lane)
    print("Elapsed time:", str(time.time() - start))
else:
    print("brain loaded, too bad u got none lol")



from print_board_module import print_board
from board_generator import generate_board
def isTetrisReady(board):
    #total_blocks = sum(map(sum, board))
    for column in board[0:9]:
        if column[0] == 1 and column[1] == 1 and column[2] == 1 and column[3] == 1:
            pass
        else:
            print("tetrisnotready")
            return False
    print("tetrisisready")
    return True
    
if __name__ == "__main__":
    board = generate_board()
    print(board)
    print(isTetrisReady(board))



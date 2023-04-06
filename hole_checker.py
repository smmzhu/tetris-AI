from print_board_module import print_board
from board_generator import generate_board
def hasHoles(board):
    for x in range(10):
        zeroFound = False
        for y in range(22):
            if board[x][y] == 0:
                if not zeroFound:
                    zeroFound = True
            if board[x][y] == 1 and zeroFound:
                return True
    return False

if __name__ == "__main__":
    print(hasHoles(generate_board(GenRandom = True)))
    print(hasHoles(generate_board(GenRandom = False)))

                
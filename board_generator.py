import random
def generate_board(GenRandom = False): #format of board is 10 lists of 22-long lists of 0s and 1s
    if GenRandom:                      #board[0][0] refers to the bottom left of the screen
        board = []
        row = []
        for x in range(10):
            for x in range(22):
                row.append(random.choice([0,1]))
            board.append(row.copy())
        return board
    else:
        board = []
        row = []
        for x in range(22):
            row.append(0)
        for x in range(10):
            board.append(row.copy())
    return board

if __name__ == "__main__":
    from print_board_module import print_board
    print(generate_board(GenRandom = True))
else:
    print("board_generator imported successfully")

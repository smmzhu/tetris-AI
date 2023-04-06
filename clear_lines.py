from board_generator import generate_board
from print_board_module import print_board
def clear_lines(board):
    for x in range(21,-1,-1):
        FullRow = True
        for y in range(10):
            if board[y][x] != 1:
                FullRow = False
                break
        if FullRow:
            for y in range(10):
                board[y].pop(x)
                board[y].append(0)
    return board

if __name__ == "__main__":
    board = generate_board()
    for x in range(10):
        board[x][0] = 1
    board[9][0] = 0
    board = clear_lines(board)
    print_board(board)

            

            

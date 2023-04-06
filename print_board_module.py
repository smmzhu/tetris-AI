
from board_generator import generate_board
def print_board(board):
    rows = []
    marker = -1
    for column in range(22):
        row = []
        for rrow in range(10):
            row.append(board[rrow][marker])
        marker -= 1
        rows.append(row)
    for row in rows:
        print(row)
if __name__ == "__main__":
    test_board = generate_board()
    test_board[0][0] = 1
    print_board(test_board)
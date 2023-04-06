import time
def grade_board(board): #board should be 10x22
    #penalties list
    a = 25 #holes base modifier
    b = 1.5 #holes multiplier per hole
    max_cap = 500 #max possible multipiler for holes
    c = 10 #height penalty per block
    d = 1 #sideways penalty
    e1 = 2#penalty for dx = 1
    e2 = 5#penalty for dx = 2
    e3 = 10#penalty for dx = 3
    e4mas = 15#penalty for dx = 4+
    fbase = 2 #penalty for chain
    fmodifier = 1.25 #penalty per chain len

    score = 0
    #penalize overhang
    overhang_blocks = 0
    for x in range(10):
        tblocks = 0
        for y in range(22):
            if board[x][y] == 0:
                tblocks += 1
            else:
                overhang_blocks += tblocks
                tblocks = 0
    score += a * min(b*overhang_blocks,max_cap)

    
    #penalize insane dx
    heights = [] 
    for row in range(9):
        top = 21
        while board[row][top] != 1:
            top -= 1
            if top == 0:
                break
        heights.append(top)
    dx_heights = []
    for x in range(8):
        dx_heights.append(heights[x+1] - heights[x])
    for dx in dx_heights: #penalize streak, penalize a single dx
        if abs(dx) == 0:
            pass
        elif abs(dx) == 1:
            score += e1
        elif abs(dx) == 2:
            score += e2
        elif abs(dx) == 3:
            score += e3
        else:
            score += e4mas
    streak = 0
    for dx in dx_heights:
        if dx != 0:
            streak =+1
        else:
            if streak != 0:
                score += fbase ** min(fmodifier**(streak-1),5)
                streak = 0
    score += fbase ** min(fmodifier**(streak-1),5)

    #penalize height, then insideness 
    for row in range(10):
        for column in range(22):
            if board[row][column] == 1:
                score += c * column
                score += min(row,8-row)*d
    return(score)    
     
if __name__ == "__main__":
    start = time.time()
    print("board graded directly")
   
    #artificially creating a board
    board = []
    row = []
    for x in range(22):
        row.append(0)
    for x in range(10):
        board.append(row.copy())
    
    for x in range(80):
        grade_board(board)
    print("Elapsed time:", str(time.time() - start))

else:
    print("board_graded imported successfully")

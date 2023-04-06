# Tetris AI

This project is a Tetris AI that plays the classic Tetris game using a greedy algorithm about where to place incoming pieces. The project includes several modules, each responsible for a specific task in the AI.

## Requirements

- Python 3.x

## Files

- `board_generator.py`: Generates the game board with specified dimensions
- `board_grader.py`: Calculates the score of a given board based on the number of holes, evenness of the board, and a variety of other factors
- `clear_lines.py`: Checks for and clears completed lines on the board
- `color_check.py`: Detects the color of a Tetris piece
- `hole_checker.py`: Detects holes in the board
- `keylogger.py`: Captures and processes keyboard inputs from the user
- `main_brain.py`: The main module that ties all the other modules together to make decisions about where to place incoming pieces
- `move_executor.py`: Executes moves on the board (e.g., rotate, move left/right, drop)
- `poss_instructions.py`: Defines the set of possible moves that the AI can make
- `print_board_module.py`: Prints the current state of the board to the console
- `put_piece_on_board.py`: Places a given Tetris piece on the board given a certain instruction
- `rgb_detector.py`: Detects the RGB color value of a pixel on the screen
- `tetris.py`: The main Tetris AI game script
- `tetris_ready_checker.py`: A module that checks if the board is ready for a tetris (i.e. it has a 4 block deep well on the right)

## Credits

This project was created by Samuel Zhu.

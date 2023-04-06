\documentclass{article}

\title{Tetris AI}
\author{Samuel Zhu}
\date{}

\begin{document}

\maketitle

This project is a Tetris AI that plays the classic Tetris game using a greedy algorithm about where to place incoming pieces. The project includes several modules, each responsible for a specific task in the AI.

\section{Requirements}

\begin{itemize}
\item Python 3.x
\end{itemize}

\section{Files}

\begin{itemize}
\item \texttt{board_generator.py}: Generates the game board with specified dimensions
\item \texttt{board_grader.py}: Calculates the score of a given board based on the number of holes, evenness of the board, and a variety of other factors
\item \texttt{clear_lines.py}: Checks for and clears completed lines on the board
\item \texttt{color_check.py}: Detects the color of a Tetris piece
\item \texttt{hole_checker.py}: Detects holes in the board
\item \texttt{keylogger.py}: Captures and processes keyboard inputs from the user
\item \texttt{main_brain.py}: The main module that ties all the other modules together to make decisions about where to place incoming pieces
\item \texttt{move_executor.py}: Executes moves on the board (e.g., rotate, move left/right, drop)
\item \texttt{poss_instructions.py}: Defines the set of possible moves that the AI can make
\item \texttt{print_board_module.py}: Prints the current state of the board to the console
\item \texttt{put_piece_on_board.py}: Places a given Tetris piece on the board given a certain instruction
\item \texttt{rgb_detector.py}: Detects the RGB color value of a pixel on the screen
\item \texttt{tetris.py}: The main Tetris AI game script
\item \texttt{tetris_ready_checker.py}: A module that checks if the board is ready for a tetris (i.e. it has a 4 block deep well on the right)
\end{itemize}

\section{Credits}

This project was created by Samuel Zhu. 

\end{document}

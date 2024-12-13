
# def check_winner()
# def check_draw()

# board is global variables
# board is a list, the tic tac toe board that store in a list

# ===================================================================================================
"""
@brief Checks if a player has won the game.

This function evaluates the current state of the board against predefined
winning conditions (rows, columns, and diagonals). If all positions in any
winning condition are occupied by the specified player, the function returns True.

@param player The symbol of the player to check ('X' or 'O').
@return A boolean value: True if the player has won, otherwise False.
"""


def check_winner(player, board):
    win_conditions = [
        # Rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonals
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False


"""
@brief Determines if the game is a draw.

This function checks the board to see if there are no empty spots remaining.
If all positions are filled and no winner has been declared, the game is a draw.

@param None
@return A boolean value: True if the board has no empty spaces, otherwise False.
"""


def check_draw(board):
    return " " not in board

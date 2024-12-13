import random

# def easy()

# board is global variables
# borad is a list, the tic tac toe board that store in a list


# ===================================================================================================
"""
@brief Selects a random available move for the AI.

This function identifies all empty spots on the board and randomly selects one of them 
as the AI's move. It ensures the AI always makes a valid move, even if all moves are random.

@param None
@return An integer representing the index of the selected move.
"""


def easy(board: list[str]):
    available_moves = [i for i, spot in enumerate(board) if spot == ""]
    move = random.choice(available_moves)
    return move

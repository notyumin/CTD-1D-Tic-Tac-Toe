from ZQ_Algo.easy import easy
import ZQ_Algo.checker as checker

# def medium()

# board is global variables
# board is a list, the tic tac toe board that store in a list


# ===================================================================================================
"""
@brief Chooses a move for the AI, balancing offense and defense.

This function identifies all empty spots on the board, prioritizing blocking
the opponent's winning move or securing a win for itself if possible. If neither
condition is met, it selects a random valid move.

@param player The symbol of the AI player ('X' or 'O').
@return An integer representing the index of the selected move.
"""


def medium(player, board):
    # Assign player and find available moves
    opponent = "X" if player == "O" else "O"
    available_moves = [i for i, spot in enumerate(board) if spot == ""]

    # Check if AI can win
    for move in available_moves:
        board[move] = player
        if checker.check_winner(player, board):
            board[move] = ""
            return move
        board[move] = ""

    # Block Opponent's winning move
    for move in available_moves:
        board[move] = opponent
        if checker.check_winner(opponent, board):
            board[move] = ""
            return move
        board[move] = ""

    # Otherwise return random move
    return easy(board)

import ZQ_Algo.checker as checker

# def hard()
# def minimax(is_maximazing, player)

# board is global variables
# borad is a list, the tic tac toe board that store in a list


# ===================================================================================================
"""
@brief Chooses the best possible move using the Minimax algorithm.

This function evaluates all valid moves on the board using the Minimax algorithm
to ensure the AI never loses. It is computationally intensive but guarantees an
optimal move.

@param player The symbol of the AI player ('X' or 'O').
@return An integer representing the index of the selected move.
"""


def minimax(is_maximizing, player, board):
    opponent = "X" if player == "O" else "O"
    available_moves = [i for i, spot in enumerate(board) if spot == ""]

    # Base cases
    if checker.check_winner(player, board):
        return 1 if is_maximizing else -1
    if checker.check_winner(opponent, board):
        return -1 if is_maximizing else 1
    if checker.check_draw(board):
        return 0

    scores = []
    for move in available_moves:
        board[move] = player if is_maximizing else opponent
        scores.append(minimax(not is_maximizing, player))
        board[move] = ""

    return max(scores) if is_maximizing else min(scores)


def hard(player, board):
    # find available moves
    available_moves = [i for i, spot in enumerate(board) if spot == ""]
    best_score = float("-inf")
    best_move = None

    for move in available_moves:
        board[move] = player
        score = minimax(False, player, board)
        board[move] = ""
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

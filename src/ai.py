import chess

# Piece values for evaluation
PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0  # King's value is not used directly
}

def evaluate_board(chess_board):
    """
    Evaluates the board for the AI.
    Positive scores favor Black, negative scores favor White.
    """
    value = 0
    for square in chess.SQUARES:
        piece = chess_board.piece_at(square)
        if piece:
            piece_value = PIECE_VALUES.get(piece.piece_type, 0)
            # Add value for Black pieces, subtract for White pieces
            if piece.color == chess.BLACK:
                value += piece_value
            else:
                value -= piece_value
    return value

def minimax(chess_board, depth, is_maximizing_player):
    """
    Minimax algorithm for evaluating the best move.
    - depth: How many moves ahead to calculate.
    - is_maximizing_player: True if AI is playing (Black), False if it's White's turn.
    """
    if depth == 0 or chess_board.is_game_over():
        return evaluate_board(chess_board)

    if is_maximizing_player:
        max_eval = -float('inf')
        for move in chess_board.legal_moves:
            chess_board.push(move)
            eval = minimax(chess_board, depth - 1, False)
            chess_board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in chess_board.legal_moves:
            chess_board.push(move)
            eval = minimax(chess_board, depth - 1, True)
            chess_board.pop()
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(chess_board, depth):
    """
    Finds the best move for the AI using the minimax algorithm.
    """
    best_move = None
    best_value = -float('inf')

    for move in chess_board.legal_moves:
        chess_board.push(move)
        board_value = minimax(chess_board, depth - 1, False)
        chess_board.pop()

        if board_value > best_value:
            best_value = board_value
            best_move = move

    return best_move

def ai_move(chess_board, depth=2):
    """
    AI makes a move using the minimax algorithm.
    - depth: Number of moves ahead to evaluate (adjust for performance).
    """
    best_move = find_best_move(chess_board, depth)
    if best_move:
        chess_board.push(best_move)

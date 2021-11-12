import board
from const import BLACK, ROWS, COLS, RED, WHITE, SQUARE_SIZE, CROWN, BLUE, GREEN
from copy import deepcopy
import pygame
import board as b

pygame.init()

def minimax(position , depth, max_player, game):
    """
    :param position: the current board state
    :param depth: how deep the minimax tree will go
    :param max_player: bool value if true algorithm will try to max the value if false minimise
    :param game: the game object that handles the board draw
    :return:
    """
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)    # this function is called to visualise the process of the ai going through all possible moves
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def draw_moves(game, board, piece):
    # visualises the process of the ai's "thinking" (drawing a circle around the considered move, for all the moves that are considered in the algorithm
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.screen)
    pygame.draw.circle(game.screen, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)
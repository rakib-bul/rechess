import pygame

def calculate_square_dimensions(screen_size):
    board_size = screen_size
    tile_size = board_size // 8
    return board_size, tile_size

def highlight_moves(screen, chess_board, selected_square, board_x, board_y, tile_size):
    if selected_square is not None:
        for move in chess_board.legal_moves:
            if move.from_square == selected_square:
                dest_square = move.to_square
                row, col = divmod(dest_square, 8)
                color = (0, 255, 0, 128)  # Transparent green
                highlight_rect = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
                highlight_rect.fill(color)
                screen.blit(highlight_rect, (board_x + col * tile_size, board_y + row * tile_size))

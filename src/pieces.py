import pygame

# Load Chess Pieces
piece_sprites = {
    "p": pygame.image.load(r"assets/black/pawn.png"),
    "r": pygame.image.load(r"assets/black/rook.png"),
    "n": pygame.image.load(r"assets/black/knight.png"),
    "b": pygame.image.load(r"assets/black/bishop.png"),
    "q": pygame.image.load(r"assets/black/queen.png"),
    "k": pygame.image.load(r"assets/black/king.png"),
    "P": pygame.image.load(r"assets/white/pawn.png"),
    "R": pygame.image.load(r"assets/white/rook.png"),
    "N": pygame.image.load(r"assets/white/knight.png"),
    "B": pygame.image.load(r"assets/white/bishop.png"),
    "Q": pygame.image.load(r"assets/white/queen.png"),
    "K": pygame.image.load(r"assets/white/king.png"),
}

def draw_pieces(screen, chess_board, board_x, board_y, tile_width, tile_height):
    fen = chess_board.board_fen()
    for row, rank in enumerate(fen.split("/")):
        col = 0
        for char in rank:
            if char.isdigit():
                col += int(char)  # Skip empty squares
            else:
                piece = piece_sprites[char]
                x = board_x + col * tile_width
                y = board_y + row * tile_height
                screen.blit(piece, (x, y))
                col += 1

def scale_sprites(tile_width, tile_height):
    for key in piece_sprites:
        piece_sprites[key] = pygame.transform.scale(piece_sprites[key], (tile_width, tile_height))

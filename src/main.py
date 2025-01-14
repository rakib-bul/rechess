import pygame
import sys
import chess
from menu import draw_menu, handle_menu_events
from game import draw_game_screen, handle_move
from ai import ai_move
from utils import calculate_square_dimensions

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))  # Square resolution
    pygame.display.set_caption("ReChess")
    clock = pygame.time.Clock()
    
    chess_board = chess.Board()
    selected_square = None
    player_turn = True
    running = True
    game_started = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_started:
                # Game Loop
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    board_size, tile_size = calculate_square_dimensions(800)
                    selected_square = handle_move(chess_board, selected_square, mouse_pos, board_size, tile_size)
                    player_turn = not player_turn  # Toggle player turn
                
                if not player_turn and not chess_board.is_game_over():
                    ai_move(chess_board)
                    player_turn = not chess_board.turn

            else:
                # Main Menu
                start_button = draw_menu(screen)
                game_started = handle_menu_events(event, start_button)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

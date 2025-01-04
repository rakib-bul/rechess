import pygame
import sys
import time
import chess
from menu import draw_menu, handle_menu_events
from game import draw_game_screen, handle_move, track_legal_moves
from ai import ai_move
from utils import calculate_dimensions, highlight_moves


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Initial resolution
    pygame.display.set_caption("Chess Game")
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
                    board_width, board_height, tile_width, tile_height = calculate_dimensions(800, 600)
                    board_x, board_y = draw_game_screen(screen, chess_board, player_turn, selected_square,
                                                         board_width, board_height, tile_width, tile_height)
                    selected_square = handle_move(chess_board, selected_square, mouse_pos)
                    player_turn = not player_turn  # Toggle player turn after player's move
                
                if not player_turn and not chess_board.is_game_over():
                    # AI Move
                    time.sleep(1)
                    chess_board.push(ai_move(chess_board))
                    player_turn = not player_turn

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
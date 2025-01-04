import pygame

def draw_menu(screen):
    font = pygame.font.Font(None, 72)
    text = font.render("ReChess", True, (255, 255, 255))
    screen.blit(text, (150, 100))

    # Start Game Button
    start_button = pygame.Rect(150, 250, 200, 50)
    pygame.draw.rect(screen, (0, 76, 61), start_button)
    start_text = pygame.font.Font(None, 36).render("Start Game", True, (255, 255, 255))
    screen.blit(start_text, (200, 260))
    
    return start_button

def handle_menu_events(event, start_button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button.collidepoint(event.pos):
            return True
    return False

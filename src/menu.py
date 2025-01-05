import pygame

def draw_menu(screen):
    screen.fill((30, 30, 30))  # Minimalistic dark background
    font = pygame.font.Font(None, 72)
    title = font.render("ReChess", True, (255, 255, 255))
    screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 150))

    # Start Game Button
    start_button = pygame.Rect(screen.get_width() // 2 - 100, 300, 200, 50)
    pygame.draw.rect(screen, (70, 130, 180), start_button)  # Steel blue button
    start_text = pygame.font.Font(None, 36).render("Start Game", True, (255, 255, 255))
    screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2, start_button.y + 10))
    
    return start_button

def handle_menu_events(event, start_button):
    if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
        return True
    return False

import pygame

pygame.init()
width, height = 400, 200
screen = pygame.display.set_mode((width, height))

text = "Hello, World! World World World "
text_color = (255, 255, 255)
border_color = (255, 0, 0)
border_width = 2

font = pygame.font.Font(None, 36)
text_surface = font.render(text, True, text_color)

border_surfaces = [
    font.render(text, True, border_color)
    for _ in range(border_width)
]

text_rect = text_surface.get_rect()
text_rect.center = (width // 2, height // 2)

border_rects = [
    border_surface.get_rect(center=text_rect.center)
    for border_surface in border_surfaces
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for border_rect, border_surface in zip(border_rects, border_surfaces):
        screen.blit(border_surface, border_rect.move(border_width, 0))
        screen.blit(border_surface, border_rect.move(-border_width, 0))
        screen.blit(border_surface, border_rect.move(0, border_width))
        screen.blit(border_surface, border_rect.move(0, -border_width))

    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()

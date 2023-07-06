import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400, 400))

circle_radius = 150
center_x, center_y = screen.get_width() // 2, screen.get_height() // 2

image = pygame.image.load("naruto.png")
image_rect = image.get_rect(center=(center_x, center_y - circle_radius))

angle = 0
rotation_speed = 0.02

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    # Vẽ đường tròn
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), circle_radius, 2)
    
    # Tính toán vị trí của ảnh trên đường tròn
    image_x = center_x + math.cos(math.radians(angle)) * circle_radius
    image_y = center_y + math.sin(math.radians(angle)) * circle_radius
    image_rect.center = (image_x, image_y)
    
    # Vẽ ảnh lên màn hình
    screen.blit(image, image_rect)
    
    pygame.display.flip()
    
    # Cập nhật góc xoay
    angle += rotation_speed

pygame.quit()

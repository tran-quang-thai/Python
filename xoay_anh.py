import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

image = pygame.image.load("naruto.png")
image_rect = image.get_rect(center=screen.get_rect().center)

angle = 0
rotation_speed = 0.05

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    # Xoay hình ảnh
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)
    
    # Vẽ hình ảnh xoay lên màn hình
    screen.blit(rotated_image, rotated_rect)
    
    pygame.display.flip()
    
    # Cập nhật góc xoay
    angle += rotation_speed

pygame.quit()

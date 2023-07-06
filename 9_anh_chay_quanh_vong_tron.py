import pygame
import math

pygame.init()
screen = pygame.display.set_mode((540, 960))
clock = pygame.time.Clock()

image = pygame.image.load("naruto.png")

circle_radius = 200
center_x, center_y = screen.get_width() // 2, screen.get_height() // 2

images = []  # Danh sách chứa 9 hình ảnh
image_width, image_height = 50, 50  # Kích thước của mỗi hình ảnh
angles = [0, 40, 80, 120, 160, 200, 240, 280, 320]  # Các góc ban đầu cho 9 hình ảnh
rotation_speed = 0.25
angle = 0  # Góc xoay chung cho tất cả hình ảnh

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    for i, angle in enumerate(angles):
        # Tính toán vị trí của ảnh trên đường tròn
        image_x = center_x + math.cos(math.radians(angle)) * circle_radius - image_width // 2
        image_y = center_y + math.sin(math.radians(angle)) * circle_radius - image_height // 2
        image_rect = pygame.Rect(image_x, image_y, image_width, image_height)
        
        # Vẽ ảnh lên màn hình
        screen.blit(image, image_rect)
        
        # Cập nhật góc xoay cho hình ảnh
        angles[i] += rotation_speed
        if angles[i] >= 360:
            angles[i] -= 360
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()

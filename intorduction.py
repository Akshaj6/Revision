import pygame
pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Window")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((173, 216, 230))
    pygame.display.update()
pygame.quit()
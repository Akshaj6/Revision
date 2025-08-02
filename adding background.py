import pygame
pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Window")
running = True
background = pygame.image.load(r"C:\Users\JB\Desktop\Python Classes\Revision\space.jfif")
background = pygame.transform.scale(background, (300, 500))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((173, 216, 230))
    screen.blit(background, (0, 0))
    pygame.display.update()
pygame.quit()
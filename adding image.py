import pygame
pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Window")
running = True
image = pygame.image.load(r"C:\Users\JB\Desktop\Python Classes\Revision\space.jfif")
pygame.transform.scale(image, (100, 200))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((173, 216, 230))
    screen.blit(image, (50, 100))
    pygame.display.update()
pygame.quit()
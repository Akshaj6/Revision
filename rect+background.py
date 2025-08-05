import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
background = pygame.image.load(r"C:\Users\JB\Desktop\Python Classes\Revision\space.jfif")
background = pygame.transform.scale(background, (300, 500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((173, 216, 230))
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 234, 23), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
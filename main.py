import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480

def player(x,y):
    screen.blit(playerimg, (x,y))

#Game Loop
running = True
while running:

    #RGB
    screen.fill((0, 128, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()


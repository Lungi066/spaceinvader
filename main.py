import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space-background-with-nebula.jpg')

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyimg = pygame.image.load('alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1.5
enemyY_change = 40

# bullet

# bullet ready state = you can't see the bullet on the screen
# fire = the bullet is currently moving

bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


# Game Loop
running = True
while running:

    # RGB
    screen.fill((0, 128, 128))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check keystroke pressed
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Spaceship boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 1.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1.5
        enemyY += enemyY_change

    #bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

import pygame
import random
import math

# Intialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# Background
background = pygame.image.load('background.jpg')

# Caption and Icon
pygame.display.set_caption("Space Batlle")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
# Player
playerImg = pygame.image.load('player.png')
playerX = 340
playerY = 480
playerX_change = 0
# Enemy
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_aliens = 6

for i in range(num_of_aliens):
    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 735))
    alienY = random.randint(50, 150)
    alienX_change.append(0.2)
    alienY_change.append(40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 35, y + 10))


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt((math.pow(alienX - bulletX, 2)) + (math.pow(alienY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    screen.fill((0, 0, 80))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # 5 = 5 + -0.1 -> 5 =  5 - 0.1
    # 5 = 5 + 0.1

    # checking for boundaries of spaceship so it doesn't go out of bound
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 700:
        playerX = 700
    # Enemy Movement
    for i in range(num_of_aliens):
        alienX[i] += alienX_change[i]
        if alienX[i] <= 0:
            alienX_change[i] = 0.2
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 700:
            alienX_change[i] = -0.2
            alienY[i] += alienY_change[i]
        # Collision
        collision = isCollision(alienX(int(i)), alienY(int(i)), bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            alienX[i] = random.randint(0, 735)
            alienY[i] = random.randint(50, 150)

        alien(alienX[i], alienY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)

    pygame.display.update()





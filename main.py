import pygame
import random
import math

# Initialize
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Title & Logo

pygame.display.set_caption("Asteroid Blaster")
logo = pygame.image.load('ufo.png')
pygame.display.set_icon(logo)

# Rocket Image
RocketImg = pygame.image.load('spaceship_small.png')
RocketX = 370
RocketY = 480
RocketX_change = 0

# Asteroid Image



AsteroidImg=pygame.image.load('asteroid_small.png')
AsteroidX=random.randint(0, 735)
AsteroidY=random.randint(50, 150)
AsteroidX_change=0.3
AsteroidY_change=35

# bullet

# ready - You can't see the bullet on screen
# fire - the bullet is moving
bulletImg = pygame.image.load('bullet_small.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = 'ready'

score=0

def rocket(x, y):
    screen.blit(RocketImg, (x, y))


def asteroid(x, y):
    screen.blit(AsteroidImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(AsteroidX, AsteroidY, bulletX, bulletY):
    distance = math.sqrt(math.pow(AsteroidX - bulletX, 2) + (math.pow(AsteroidY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                RocketX_change = -0.3
            if event.key == pygame.K_RIGHT:
                RocketX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = RocketX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                RocketX_change = 0.3

    RocketX += RocketX_change

    if RocketX <= 0:
        RocketX = 0
    elif RocketX >= 736:
        RocketX = 736


    # Asteroid Movement

    AsteroidX+= AsteroidX_change

    if AsteroidX <= 0:
       AsteroidX_change = 0.3
       AsteroidY += AsteroidY_change
    elif AsteroidX >= 740:
        AsteroidX_change = -0.3
        AsteroidY += AsteroidY_change



    # collision
    collision = isCollision(AsteroidX, AsteroidY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        AsteroidX = random.randint(0, 735)
        AsteroidY = random.randint(50, 150)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'


    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change




    rocket(RocketX, RocketY)
    asteroid(AsteroidX, AsteroidY)
    pygame.display.update()

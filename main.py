import pygame
from player import Player

pygame.init()
pygame.display.set_caption('Game')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen1 = pygame.display.set_mode(size)
running = True
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
fps = 60
c = 0
vx, vy, v = 0, 0, 100
clock = pygame.time.Clock()
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key in (119, 97, 115, 100):
            if event.key == 119:
                vy -= v
            elif event.key == 97:
                vx -= v
            elif event.key == 115:
                vy += v
            elif event.key == 100:
                vx += v
        if event.type == pygame.KEYUP and event.key in (119, 97, 115, 100):
            if event.key == 119:
                vy += v
            elif event.key == 97:
                vx += v
            elif event.key == 115:
                vy -= v
            elif event.key == 100:
                vx -= v

    screen1.fill((0, 0, 0))
    player.update(vx / fps, vy / fps)
    all_sprites.draw(screen1)
    clock.tick(fps)
    screen.blit(screen1, (0, 0))
    pygame.display.flip()
import pygame
from player import Player
from mob import Mob
from random import randint

pygame.init()
pygame.display.set_caption('Game')
size = width, height = 1200, 675
screen = pygame.display.set_mode(size)
bg = pygame.image.load('sprites/background3.png').convert()
scroll = 0
running = True
player = Player()
fps = 60
c = 0
mobs = pygame.sprite.Group()
clock = pygame.time.Clock()
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == 32:
            player.v *= -1
        if event.type == pygame.KEYUP and event.key == 32:
            player.v *= -1
    screen.fill((0, 0, 0))
    if randint(0, 100) == 1:
        mobs.add(Mob())
    mobs.update(fps, player)
    player.update(fps, height)
    screen.blit(bg, (0 - scroll, 0))
    screen.blit(bg, (width - scroll, 0))
    if not player.died:
        scroll += 1
    scroll %= width
    screen.blit(player.image, (player.rect.x + player.kx, player.rect.y + player.ky))
    mobs.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
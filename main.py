import pygame
from pygame.examples.music_drop_fade import volume

from player import Player
from mob import Mob, Coin, Heal
from random import randint
from se import start_screen, end_screen, pause_screen

pygame.init()
pygame.display.set_caption('Game')
size = width, height = 1200, 675
screen = pygame.display.set_mode(size)
screen1 = pygame.display.set_mode(size)
font = pygame.font.Font(None, 24)

pygame.mixer.music.load('song1.mp3')
pygame.mixer.music.play(-1)
volume = 1

start_screen(screen, width, height)

bg = pygame.image.load('sprites/background3.png').convert()
pl_im = {'run':[pygame.image.load(f"sprites/run/{i}.png").convert_alpha() for i in range(15)],
         'fly': [pygame.image.load(f"sprites/fly/{i}.png").convert_alpha() for i in range(15)],
         'die': [pygame.image.load(f"sprites/die/{i}.png").convert_alpha() for i in range(5)]}

mb_im = {'roket': pygame.image.load(f"sprites/roket.png").convert_alpha(),
         'explosion': [pygame.image.load(f"sprites/explosion/{i}.png").convert_alpha() for i in range(9)],
         'coin': [pygame.image.load(f"sprites/coins/{i}.png").convert_alpha() for i in range(10)],
         'heal': [pygame.image.load(f"sprites/heal/{i}.png").convert_alpha() for i in range(10)]}

scroll = 0
running = True
player = Player(pl_im['run'], pl_im['fly'], pl_im['die'])
fps = 60
c = 0
mobs = pygame.sprite.Group()
clock = pygame.time.Clock()
pygame.display.flip()
time = 0
st = pygame.time.get_ticks()
while running:
    if player.died:
        if time == 0:
            time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - time >= 3000:
            time = 0
            pygame.mixer.music.stop()
            pygame.time.delay(500)
            pygame.mixer.music.load('loose.mp3')
            pygame.mixer.music.play()
            end_screen(screen, width, height, player.money, (pygame.time.get_ticks() - st) // 1000)
            player.died = False
            player.hp = 3
            player.money = 0
            mobs.empty()
            pygame.mixer.music.load('song1.mp3')
            pygame.mixer.music.play(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == 32:
            player.v *= -1
        if event.type == pygame.KEYUP and event.key == 32:
            player.v *= -1
        if event.type == pygame.KEYDOWN and event.key == 27:
            pause_screen(screen, width, height, player.money, (pygame.time.get_ticks() - st) // 1000)
    screen.fill((0, 0, 0))

    if randint(0, 100) == 1:
        mobs.add(Mob(mb_im['roket'], mb_im['explosion']))
    if randint(0, 150) == 1:
        mobs.add(Coin(mb_im['coin']))
    if randint(0, 500) == 1:
        mobs.add(Heal(mb_im['heal']))
    mobs.update(fps, player)
    player.update(fps, height)
    screen.blit(bg, (0 - scroll, 0))
    screen.blit(bg, (width - scroll, 0))
    if not player.died:
        scroll += 1
    scroll %= width

    #pygame.draw.rect(screen1, 'green', (player.rect.x,player.rect.y, player.rect.width, player.rect.height))
    screen1.blit(player.image, (player.rect.x + player.kx, player.rect.y + player.ky))
    mobs.draw(screen1)

    hp = font.render(str(player.hp), True, 'red')
    screen1.blit(hp, (10, 10))
    screen1.blit(pygame.transform.scale(mb_im['heal'][0], (20, 20)), (25, 7))

    money = font.render(str(player.money), True, 'gold')
    screen1.blit(money, (60, 10))
    screen1.blit(pygame.transform.scale(mb_im['coin'][0], (20, 20)), (75, 7))

    screen.blit(screen1, (0, 0))
    clock.tick(fps)
    pygame.display.flip()
import pygame
from player import Player
from mob import Mob, Coin, Heal
from random import randint
from se import start_screen, end_screen, pause_screen
import ctypes

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()
pygame.display.set_caption('Flight')
size = width, height = 1200, 675
screen = pygame.display.set_mode(size)
screen1 = pygame.display.set_mode(size)
font = pygame.font.Font(None, 30)

pygame.mixer.music.load('song1.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.init()
sounds = (pygame.mixer.Sound('explosion.mp3'),
          pygame.mixer.Sound('coins.mp3'))
volume = 1

start_screen(screen, width, height)

bg = pygame.image.load('sprites/background3.png').convert()
pl_im = {'run':[pygame.image.load(f"sprites/run/{i}.png").convert_alpha() for i in range(15)],
         'fly': [pygame.image.load(f"sprites/fly/{i}.png").convert_alpha() for i in range(15)],
         'die': [pygame.image.load(f"sprites/die/{i}.png").convert_alpha() for i in range(5)]}

mb_im = {'roket': pygame.image.load(f"sprites/roket.png").convert_alpha(),
         'clock': pygame.image.load(f"sprites/clock.png").convert_alpha(),
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
            end_screen(screen, width, height, player.money, (pygame.time.get_ticks() - st) // 1000 - 4)
            player.died = False
            player.hp = 3
            player.money = 0
            mobs.empty()
            pygame.mixer.music.load('song1.mp3')
            pygame.mixer.music.play(-1)
            st = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == 1073741906:
            if (v := pygame.mixer.music.get_volume()) < 1:
                pygame.mixer.music.set_volume(v + 0.1)
                volume += 0.1
        if event.type == pygame.KEYDOWN and event.key == 1073741905:
            if (v := pygame.mixer.music.get_volume()) > 0:
                pygame.mixer.music.set_volume(v - 0.1)
                volume -= 1
        if event.type == pygame.KEYDOWN and event.key == 32:
            player.v *= -1
        if event.type == pygame.KEYUP and event.key == 32:
            player.v *= -1
        if event.type == pygame.KEYDOWN and event.key == 27:
            pause_screen(screen, width, height, player.money, (pygame.time.get_ticks() - st) // 1000)
    screen.fill((0, 0, 0))

    if randint(0, 50) == 1:
        mobs.add(Mob(mb_im['roket'], mb_im['explosion'], (pygame.time.get_ticks() - st) // 1000, sounds[0]))
    if randint(0, 150) == 1:
        mobs.add(Coin(mb_im['coin'], sounds[1]))
    if randint(0, 1000) == 1:
        mobs.add(Heal(mb_im['heal'], sounds[1]))
    mobs.update(fps, player, volume)
    player.update(fps, height)
    screen.blit(bg, (0 - scroll, 0))
    screen.blit(bg, (width - scroll, 0))
    if not player.died:
        scroll += 1
    scroll %= width

    #pygame.draw.rect(screen1, 'green', (player.rect.x,player.rect.y, player.rect.width, player.rect.height))
    screen1.blit(player.image, (player.rect.x + player.kx, player.rect.y + player.ky))
    mobs.draw(screen1)

    for i in range(player.hp):
        screen1.blit(pygame.transform.scale(mb_im['heal'][0], (20, 20)), (5 + 25 * i, 5))

    money = font.render(str(player.money), True, 'gold')
    screen1.blit(money, (30, 30))
    screen1.blit(pygame.transform.scale(mb_im['coin'][0], (20, 20)), (5, 30))

    if player.hp:
        p_t = font.render(str((pygame.time.get_ticks() - st) // 1000), True, 'green')
    screen1.blit(p_t, (30, 55))
    screen1.blit(pygame.transform.scale(mb_im['clock'], (20, 20)), (5, 55))

    screen.blit(screen1, (0, 0))
    clock.tick(fps)
    pygame.display.flip()

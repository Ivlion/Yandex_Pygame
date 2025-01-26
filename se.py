import pygame
import sys


def terminate():
    pygame.quit()
    sys.exit()

def start_screen(screen, WIDTH, HEIGHT):
    intro_text = ["ИГРА", "",
                  "Для полёта нажать пробел",
                  "Для регулировки громкости используйте стрелки вверх/вниз",
                  "Для просмотра статистики нажмите T",
                  "Для продолжения нажмите любую другую клавишу"]

    fon = pygame.transform.scale(pygame.image.load('sprites/background3.png').convert(), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == 1073741906:
                if (v := pygame.mixer.music.get_volume()) < 1:
                    pygame.mixer.music.set_volume(v + 0.1)
            elif event.type == pygame.KEYDOWN and event.key == 1073741905:
                if (v := pygame.mixer.music.get_volume()) > 0:
                    pygame.mixer.music.set_volume(v - 0.1)
            elif event.type == pygame.KEYUP and event.key not in (1073741906, 1073741905, 116):
                return
        pygame.display.flip()


def end_screen(screen, WIDTH, HEIGHT, money, t):
    intro_text = ["ТЫ ПРОИГРАЛ!!!", "",
                  "ТЫ ЛОХ!!!",
                  f"Монет собрано: {money}",
                  f"Время жизни: {t} секунд", "",
                  "Для регулировки громкости используйте стрелки вверх/вниз",
                  "Для просмотра статистики нажмите T",
                  "Для сохранения результата нажмите S",
                  "Для продолжения нажмите любую другую клавишу"]

    fon = pygame.transform.scale(pygame.image.load('sprites/background3.png').convert(), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == 1073741906:
                if (v := pygame.mixer.music.get_volume()) < 1:
                    pygame.mixer.music.set_volume(v + 0.1)
            elif event.type == pygame.KEYDOWN and event.key == 1073741905:
                if (v := pygame.mixer.music.get_volume()) > 0:
                    pygame.mixer.music.set_volume(v - 0.1)
            elif event.type == pygame.KEYUP and event.key not in (1073741906, 1073741905, 116, 115):
                return
    pygame.display.flip()

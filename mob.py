import pygame.sprite
from random import randint

class Mob(pygame.sprite.Sprite):
    def __init__(self, roket, explosion, t):
        super().__init__()
        self.roket = roket
        self.exp_im = explosion
        self.image = self.roket
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1400
        self.rect.y = randint(1, int(675 - self.rect.height))
        self.v = 300
        k = 1.0
        if k + (0.2 * (t // 10)) <= 900:
            self.v *= k + (0.2 * (t // 20))
        else:
            self.v = 900
        self.frame = 0
        self.explosion = False

    def update(self, fps, player):
        if pygame.sprite.collide_mask(self, player) and player.hp:
            self.explosion = True
            player.hp -= 1
            player.frame = 0
        if self.explosion:
            self.delete()
        elif not self.explosion:
            if self.rect.x + self.rect.width < -2:
                self.delete()
            self.rect.x -= self.v / fps

    def delete(self):
        if self.explosion:
            if self.frame == 0:
                self.rect.x -= 250
                self.rect.y -= 150
            self.frame += 0.2
            if self.frame >= 8:
                self.explosion = False
            self.image = self.exp_im[int(self.frame)]
        else:
            self.kill()


class Coin(pygame.sprite.Sprite):
    def __init__(self, coin):
        super().__init__()
        self.coin = coin
        self.image = self.coin[0]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1400
        self.rect.y = randint(1, int(675 - self.rect.height))
        self.v = 150
        self.frame = 0

    def update(self, fps, player):
        if pygame.sprite.collide_rect(self, player) and player.hp:
            player.money += 1
            self.kill()
        if self.rect.x + self.rect.width < 0:
            self.kill()
        self.frame += 0.2
        if self.frame > 9:
            self.frame -= 9
        self.image = self.coin[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.mask = pygame.mask.from_surface(self.image)
        if not player.died:
            self.rect.x -= self.v / fps


class Heal(pygame.sprite.Sprite):
    def __init__(self, heal):
        super().__init__()
        self.heal = heal
        self.image = self.heal[0]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1400
        self.rect.y = randint(1, int(675 - self.rect.height))
        self.v = 150
        self.frame = 0

    def update(self, fps, player):
        if pygame.sprite.collide_rect(self, player) and player.hp:
            player.hp += (1 if player.hp < 5 else 0)
            self.kill()
        if self.rect.x + self.rect.width < 0:
            self.kill()
        self.frame += 0.2
        if self.frame > 9:
            self.frame -= 9
        self.image = self.heal[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.mask = pygame.mask.from_surface(self.image)
        if not player.died:
            self.rect.x -= self.v / fps

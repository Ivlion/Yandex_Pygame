import pygame.sprite
from random import randint

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/roket.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1400
        self.rect.y = randint(1, int(675 - self.rect.height))
        self.v = 300
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
            self.frame += 0.1
            if self.frame >= 8:
                self.explosion = False
            self.image = pygame.image.load(f"sprites/explosion/{int(self.frame)}.png")
        else:
            self.kill()

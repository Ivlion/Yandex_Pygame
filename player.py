import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, run, fly, die):
        super().__init__()
        self.run = run
        self.fly = fly
        self.die = die
        self.image = self.run[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 200
        self.rect.y = 20
        self.rect.width = 55
        self.rect.height = 105
        self.frame = 0
        self.kx = -55
        self.ky = -3
        self.v = 300
        self.hp = 3
        self.money = 0
        self.died = False

    def update(self, fps, floor):
        if not self.hp and self.v < 0:
            self.v *= -1
        if self.hp:
            if self.rect.y + self.rect.height == floor:
                self.kx = -55
                self.frame += 0.3
                if self.frame > 14:
                    self.frame -= 14
                self.image = self.run[int(self.frame)]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.kx = -60
                self.frame += 0.1
                if self.frame > 14:
                    self.frame -= 14
                self.image = self.fly[int(self.frame)]
                self.mask = pygame.mask.from_surface(self.image)
        elif not self.died:
            self.frame += 0.1
            if self.frame >= 4:
                self.died = True
            self.image = self.die[int(self.frame)]
        if 0 <= (self.rect.y + self.v / fps) <= floor - self.rect.height:
            self.rect.y += self.v / fps




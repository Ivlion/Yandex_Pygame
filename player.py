import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/run/0.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.rect.x = 100
        self.rect.y = 20
        self.rect.width = 60
        self.rect.height = 105
        self.frame = 0
        self.kx = -55
        self.ky = -3
        self.v = 300
        self.hp = 3
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
                self.image = pygame.image.load(f"sprites/run/{int(self.frame)}.png")
                self.mask = pygame.mask.from_surface(self.image.convert_alpha())
            else:
                self.kx = -60
                self.frame += 0.1
                if self.frame > 14:
                    self.frame -= 14
                self.image = pygame.image.load(f"sprites/fly/{int(self.frame)}.png")
                self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        elif not self.died:
            self.frame += 0.1
            if self.frame >= 4:
                self.died = True
            self.image = pygame.image.load(f"sprites/die/{int(self.frame)}.png")
        if 0 <= (self.rect.y + self.v / fps) <= floor - self.rect.height:
            self.rect.y += self.v / fps




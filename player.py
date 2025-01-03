import pygame.sprite


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/player/stay.png")
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 20
        self.frame = 0

    def update(self, x, y):
        if x == y == 0:
            self.frame = 0
            self.image = pygame.image.load("sprites/player/stay.png")
        else:
            self.frame += 0.1
            if self.frame > 4:
                self.frame -= 4
            self.image = pygame.image.load(f"sprites/player/run{int(self.frame)}.png")
        self.rect.x += x
        self.rect.y += y


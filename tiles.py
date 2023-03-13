import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size) -> None:
        super().__init__()
        self.image  = pygame.surface.Surface((size, size)).convert_alpha()
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift) -> None:
        self.rect.x += x_shift
        
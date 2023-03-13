import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.surface.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16


    def update(self) -> None:
        self.get_input()
        # self.rect.x += self.direction.x * self.speed
        # self.rect.y += self.direction.y * self.speed
        # self.apply_gravity()


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed


    def get_input(self):
        keys = pygame.key.get_pressed()
        print(keys.type)

        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
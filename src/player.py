import pygame
import os
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations.get('idle')[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        


    def import_character_assets(self):
        character_path  = r'graphics\character'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            self.animations[animation] = import_folder(full_path)
        
    
    def animate(self):
        animation = self.animations.get('run')

        # loop over frame index
        
        pass


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

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1

        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
import pygame
from os import walk
import os

def import_folder(path):
    surface_list = []
    for _, __, img_file_list in walk(path):
        for image_file in img_file_list:
            image_path = os.path.join(path, image_file)
            image_surface = pygame.image.load(image_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list
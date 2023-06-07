import pygame

class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        file_path = "./lib/assets/basic_alien.png"
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.value = 10

    def update(self, direction):
        self.rect.x += direction
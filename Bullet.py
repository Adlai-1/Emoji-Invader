#All configurations relating to our Bullet can be 
#found and adjusted here in this file.
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,screen,ship):
        super(Bullet,self).__init__()

        self.screen = screen
        self.image = pygame.image.load('Images/fireball.bmp')
        self.rect = self.image.get_rect()

        #Setting bullet position to be directly on top
        #of our ship to make it look as if the bullets
        #are coming from the ship.
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
    
        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= 1
        self.rect.y = self.y
    
    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)


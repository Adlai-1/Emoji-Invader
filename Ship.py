#All configurations relating to our ship can be 
#found and adjusted here in this file.
import pygame
class Ship():

    def __init__(self,screen) -> None:

        #rect = rectangle
        self.screen = screen
        self.image = pygame.image.load('Images/Rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Where a ship must appear anytime the game starts.
        #a.k.a ship coordinates.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement flag...to ensure continuous movement.
        #Both left and right.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    #This function draws our ship at the specified location.
    def draw(self):
        self.screen.blit(self.image,self.rect)

    #This function makes updates to move our ship.
    #continuously to the left or right
    #within the bounded area of the game screen.
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        elif self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
    
    def centre_ship(self):
        self.center = self.screen_rect.centerx
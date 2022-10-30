import sys
import pygame
from Bullet import Bullet
from Alien import Alien

def check_events(screen,ship,bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        
        elif event.type == pygame.KEYDOWN:
            #Piloting the ship to moving in
            #Up, down, left and right motions.
            #Only when the right key is pressed.
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            #End...

            #Key press for shooting fireballs...
            elif event.key == pygame.K_SPACE:
                nbullet = Bullet(screen,ship)
                bullet.add(nbullet)

        
        elif event.type == pygame.KEYUP:
            #Grounding the ship to a halt 
            #Only when the keys are not pressed
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
            #End... 

def create_fleet(screen,aliens,ship):
    alien = Alien(screen)
    alien_width = alien.rect.width

    alien_height = alien.rect.height
    ship_height = ship.rect.height


    space_x = 1000-2 * alien_width
    num_alien = int(space_x/(2*alien_width))

    space_y = 500 -3 * (alien_height-ship_height)

    num_rows = int(space_y/(2*alien_height))

    for a in range(num_rows-1):
        for num in range(num_alien):
            alien = Alien(screen)
            alien.x = alien_width + 2 * alien_width * num
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * a
            aliens.add(alien)


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            alien.rect.y += 5
            alien.ad *= -1


def update_bullet(screen,aliens,bullet,ship):

    collisions = pygame.sprite.groupcollide(bullet,aliens,True,True)

    if len(aliens) == 0:
        create_fleet(screen,aliens,ship)
        

def check_aliens_bottom(screen,alien,ship):
    screen_rect = screen.get_rect()

    for ali in alien.sprites():
        if ali.rect.bottom >= screen_rect.bottom:
            create_fleet(screen,alien,ship)
            ship.centre_ship()
            
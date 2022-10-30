from Ship import Ship
import pygame
import Game_functions as gf
from pygame.sprite import Group
from Alien import Alien

# The Home file contains all the screen configuration
# and Details.

# It's on this file where we can make changes to
# how the game looks like from width n height to
# background colour etc.

# This initializes our game.
pygame.init()

# Width and height of our display screen is set here.
screen = pygame.display.set_mode((1000, 500))

# Display name for our screen window.
pygame.display.set_caption("Space Keepers")

# Object from our class Ship
ship = Ship(screen)

bullets = Group()

aliens = Group()

alien = Alien(screen)

gf.create_fleet(screen, aliens,ship)

# A continious loop listening for events to
# trigger an action whenever a key is pressed.
while True:

    gf.check_events(screen, ship, bullets)

    ship.update()

    bullets.update()

    gf.check_fleet_edges(aliens)
    aliens.update()
    
    gf.update_bullet(screen,aliens,bullets,ship)

    # Loop to ensure that each bullet from a group
    # is created on the screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Loop that ensures that bullets are
    # constantly deleted anything it leaves
    # the confines of the game screen to prevent
    # game lagging.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    ship.draw()

    aliens.draw(screen)

    pygame.display.flip()

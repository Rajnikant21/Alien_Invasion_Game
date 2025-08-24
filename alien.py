import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to manage the ship"""
    """The image may need some edits which can be easily done using Paint app, or you can use Photoshop or Canva 
        for more detailed working"""
    def __init__(self, ai_game):
        """Initialise the ship and set its starting Position"""
        super().__init__()
        self.screen = ai_game.screen
        """As i reused the code from "Ship" module commented unused code"""
        self.settings = ai_game.settings
        # self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #self.rect.topleft = self.screen_rect.topleft

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left. """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Retuurn True if alien is at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
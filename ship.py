import pygame


class Ship:
    """A class to manage the ship"""
    """The image may need some edits which can be easily done using Paint app, or you can use Photoshop or Canva 
        for more detailed working"""
    def __init__(self, ai_game):
        """Initialise the ship and set its starting Position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('player_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's x value, not  the rect.
        # Take this as plotting a 2 dimensional graph to all four sides and the movement of ship can be figured out.
        """This was my personal win!"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """"Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

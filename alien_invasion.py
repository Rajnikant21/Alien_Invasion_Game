import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Over all class to manage game assets and behaviour - The main() of this program"""

    def __init__(self):
        """Initialise the game, and create game resources"""

        pygame.init()

        self.settings = Settings()
        """for full screen"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        """for custom screen size """
        # self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # creating an attribute for class Ship for easy accessibility

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            # Move the ship down
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            # Move the ship up
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullets(self):
        """Create a new bullet and add it to bullets group"""

        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets"""

        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens. """
        # Create an Alien and find the number of aliens in a row.
        # Spacing between each alien is equal to on alien width.
        alien = Alien(self)
        alien_width = alien.rect.width
        # available_space_x = self.settings.screen_width-(2 * alien_width)   -  with this the length of alien row is
        # screen width specified in settings module. Will update it to fullscreen setup
        available_space_x = self.screen.get_rect().width - (2 * alien_width)
        number_alien_x = available_space_x//(2 * alien_width)

        # Create the first row of aliens.
        for alien_number in range(number_alien_x):
            # create an alien and place it in the row.
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _update_screen(self):
        """Update images on the screen,and flip to the new screen"""

        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Set the background color - Now it is moved to "Settings class in settings Module"
        # self.bg_color = (230,230,230)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

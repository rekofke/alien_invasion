import sys
import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')  # Fixed assignment
        self.rect = self.image.get_rect()                  # Fixed assignment

        # Start each new ship the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag: start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):  # Fixed method name
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect)

class AlienInvasion:
    def __init__(self):
        """Initialize game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)

    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = false
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    # Move ship to the right.
                    self.ship.rect.x += 1
            
    def _update_screen(self):
        """Update images on the screen and flip to a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # Use correct method name
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

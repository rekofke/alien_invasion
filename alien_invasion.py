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

        # Start at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

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
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Update screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # Use correct method name
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

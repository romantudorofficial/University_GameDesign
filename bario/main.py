import pygame
import sys



# Initialize Pygame.
pygame.init()


# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bario")
CLOCK = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Gravity
GRAVITY = 0.5



class Player (pygame.sprite.Sprite):

    def __init__ (self, x, y):

        super().__init__()

        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.jump_strength = 12
        self.on_ground = False


    def update (self, platforms):

        # Move horizontally.
        keys = pygame.key.get_pressed()
        self.velocity_x = 0  # Reset horizontal velocity each frame
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed

        # Jump.
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -self.jump_strength
            self.on_ground = False

        # Apply gravity.
        self.velocity_y += GRAVITY

        # Update position.
        self.rect.x += self.velocity_x
        self.handle_horizontal_collisions(platforms)
        self.rect.y += self.velocity_y
        self.handle_vertical_collisions(platforms)


    def handle_horizontal_collisions (self, platforms):

        # Check for collisions in the horizontal direction
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_x > 0:  # Moving right; hit the left side of the platform
                    self.rect.right = platform.rect.left
                elif self.velocity_x < 0:  # Moving left; hit the right side of the platform
                    self.rect.left = platform.rect.right

    def handle_vertical_collisions (self, platforms):

        # Check for collisions in the vertical direction
        self.on_ground = False  # Will be set to True if colliding with a platform below
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling; hit the top of the platform
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # Jumping; hit the bottom of the platform
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0



class Platform (pygame.sprite.Sprite):

    def __init__ (self, x, y, width, height):

        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))



def main ():

    '''
        Runs the game.
    '''

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    platforms = []

    # Create the player.
    player = Player(100, SCREEN_HEIGHT - 150)
    all_sprites.add(player)

    # Create the ground platform.
    ground = Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
    platforms.append(ground)
    all_sprites.add(ground)

    # Create floating platforms.
    platform1 = Platform(200, 400, 150, 20)
    platforms.append(platform1)
    all_sprites.add(platform1)

    platform2 = Platform(450, 300, 150, 20)
    platforms.append(platform2)
    all_sprites.add(platform2)

    # Run the game.
    running = True

    while running:

        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        player.update(platforms)

        # Draw
        SCREEN.fill(WHITE)
        all_sprites.draw(SCREEN)
        pygame.display.flip()

    # Exit the game.
    pygame.quit()
    sys.exit()



if __name__ == "__main__":

    '''
        Runs the game.
    '''

    main()
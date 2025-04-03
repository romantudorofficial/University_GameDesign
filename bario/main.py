import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Platformer Prototype")
CLOCK = pygame.time.Clock()
FPS = 60

# Colors
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
BLUE    = (50, 100, 255)
GREEN   = (0, 255, 0)
RED     = (255, 50, 50)
YELLOW  = (255, 255, 0)
PURPLE  = (128, 0, 128)

# Gravity setting
GRAVITY = 0.5

# Fonts for UI
FONT = pygame.font.SysFont('Arial', 24)
MESSAGE_FONT = pygame.font.SysFont('Arial', 48)

# Game parameters
TOTAL_NORMAL_COLLECTIBLES = 5
GAME_TIME_LIMIT = 30  # seconds

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 30
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.jump_strength = 12
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        self.velocity_x = 0  # reset horizontal velocity
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -self.jump_strength
            self.on_ground = False

        # Apply gravity and update position
        self.velocity_y += GRAVITY
        self.rect.x += self.velocity_x
        self.handle_horizontal_collisions(platforms)
        self.rect.y += self.velocity_y
        self.handle_vertical_collisions(platforms)

    def handle_horizontal_collisions(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_x > 0:
                    self.rect.right = platform.rect.left
                elif self.velocity_x < 0:
                    self.rect.left = platform.rect.right

    def handle_vertical_collisions(self, platforms):
        self.on_ground = False  # reset flag
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=GREEN):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, size=20, color=YELLOW):
        super().__init__()
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

class SpecialCollectible(Collectible):
    def __init__(self, x, y):
        # Special collectible is a bit larger and purple.
        super().__init__(x, y, size=25, color=PURPLE)

def restart_game():
    main()  # Restart the game by calling main() again.

def main():
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    safe_platforms = pygame.sprite.Group()  # Platforms that are safe to stand on
    collectible_group = pygame.sprite.Group()
    special_group = pygame.sprite.Group()

    # Create the lava base platform (red)
    lava_platform = Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40, color=RED)
    # Note: Lava is not added to safe_platforms.
    all_sprites.add(lava_platform)

    # Create safe platforms (closer in height and width)
    # Six platforms arranged in a diagonal (closer together horizontally and vertically)
    platforms_data = [
        (100, 650, 150, 20),
        (260, 640, 150, 20),
        (420, 630, 150, 20),
        (580, 620, 150, 20),
        (740, 610, 150, 20),
        (900, 600, 150, 20)
    ]
    safe_platforms_list = []
    for data in platforms_data:
        plat = Platform(*data)
        safe_platforms.add(plat)
        all_sprites.add(plat)
        safe_platforms_list.append(plat)

    # Place normal collectibles on the first five platforms
    for plat in safe_platforms_list[:5]:
        center_x = plat.rect.x + plat.rect.width // 2
        center_y = plat.rect.y - 15  # Slightly above the platform
        collectible = Collectible(center_x, center_y)
        collectible_group.add(collectible)
        all_sprites.add(collectible)

    # Place the special collectible on the sixth platform
    sp_plat = safe_platforms_list[5]
    center_x = sp_plat.rect.x + sp_plat.rect.width // 2
    center_y = sp_plat.rect.y - 15
    special_item = SpecialCollectible(center_x, center_y)
    special_group.add(special_item)
    all_sprites.add(special_item)

    # Create the player on the first platform
    player = Player(110, safe_platforms_list[0].rect.y - 30)
    all_sprites.add(player)

    collected_normal = 0
    special_collected = False
    win = False
    lose = False

    # Timer
    start_ticks = pygame.time.get_ticks()

    running = True
    while running:
        CLOCK.tick(FPS)
        current_ticks = pygame.time.get_ticks()
        elapsed_seconds = (current_ticks - start_ticks) / 1000
        time_left = max(0, GAME_TIME_LIMIT - elapsed_seconds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if win or lose:
                    mouse_pos = pygame.mouse.get_pos()
                    restart_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 60, 150, 40)
                    if restart_button_rect.collidepoint(mouse_pos):
                        restart_game()

        if not win and not lose:
            player.update(safe_platforms.sprites())

            # If player touches the lava, lose the game.
            if player.rect.colliderect(lava_platform.rect):
                lose = True

            # Check for normal collectible collisions
            collected = pygame.sprite.spritecollide(player, collectible_group, True)
            if collected:
                collected_normal += len(collected)

            # Check for special collectible collision (only count if all normal ones have been collected)
            if collected_normal == TOTAL_NORMAL_COLLECTIBLES:
                if pygame.sprite.spritecollide(player, special_group, True):
                    special_collected = True

            # Win condition: all normal collectibles and the special collectible are collected
            if collected_normal >= TOTAL_NORMAL_COLLECTIBLES and special_collected:
                win = True

            # Lose condition: timer runs out
            if time_left <= 0:
                lose = True

        # Drawing
        if win or lose:
            # Clear all game elements by filling the screen white.
            SCREEN.fill(WHITE)
            if win:
                message = "You Win!"
                message_color = BLUE
            else:
                message = "Game Over!"
                message_color = RED
            text_surface = MESSAGE_FONT.render(message, True, message_color)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            SCREEN.blit(text_surface, text_rect)

            # Draw restart button
            restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 60, 150, 40)
            pygame.draw.rect(SCREEN, BLUE, restart_button)
            restart_text = FONT.render("Restart", True, WHITE)
            restart_text_rect = restart_text.get_rect(center=restart_button.center)
            SCREEN.blit(restart_text, restart_text_rect)
        else:
            SCREEN.fill(WHITE)
            all_sprites.draw(SCREEN)
            # Draw timer and collectible counter
            timer_text = FONT.render(f"Time Left: {int(time_left)}", True, BLACK)
            SCREEN.blit(timer_text, (SCREEN_WIDTH - 170, 10))
            counter_text = FONT.render(
                f"Collectibles: {collected_normal}/{TOTAL_NORMAL_COLLECTIBLES}  Special: {'Yes' if special_collected else 'No'}",
                True, BLACK)
            SCREEN.blit(counter_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

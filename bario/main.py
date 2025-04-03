import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multi-Level Platformer")
CLOCK = pygame.time.Clock()
FPS = 60

# Default Colors
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
BLUE    = (50, 100, 255)
GREEN   = (0, 255, 0)
RED     = (255, 50, 50)
YELLOW  = (255, 255, 0)
PURPLE  = (128, 0, 128)

# Border thickness (in pixels)
BORDER_THICKNESS = 5

# Gravity setting
GRAVITY = 0.5

# Fonts for UI
FONT = pygame.font.SysFont('Arial', 24)
MESSAGE_FONT = pygame.font.SysFont('Arial', 48)

# Level configuration data.
# Each level now defines custom colors (optional) and:
#   - "platforms": list of tuples (x, y, width, height)
#   - "collectibles": list of tuples (x, y) for normal collectibles.
#   - "special_collectible": a tuple (x, y) for the special collectible.
#   - "timer": time limit in seconds.
levels = [
    {
        "platforms": [
            (100, 650, 150, 20),
            (260, 640, 150, 20),
            (420, 630, 150, 20),
            (580, 620, 150, 20),
            (740, 610, 150, 20),
            (900, 600, 150, 20)
        ],
        "collectibles": [
            (175, 635),  # centered above first platform (100+75, 650-15)
            (335, 625),  # second platform
            (495, 615),  # third platform
            (655, 605),  # fourth platform
            (815, 595)   # fifth platform
        ],
        "special_collectible": (975, 585),  # on sixth platform
        "timer": 30,
        "background_color": WHITE,
        "platform_color": GREEN,
        "collectible_color": YELLOW,
        "special_collectible_color": PURPLE,
        "lava_color": RED
    },
    {
        "platforms": [
            (100, 700, 150, 20),
            (300, 660, 150, 20),
            (500, 620, 150, 20),
            (700, 580, 150, 20),
            (900, 540, 150, 20),
            (750, 500, 150, 20)
        ],
        "collectibles": [
            (175, 685),  # first platform
            (375, 645),  # second platform
            (575, 605),  # third platform
            (775, 565),  # fourth platform
            (975, 525)   # fifth platform
        ],
        "special_collectible": (825, 485),  # on sixth platform
        "timer": 25,
        "background_color": (230, 230, 255),  # a light blueish background
        "platform_color": (0, 200, 0),          # a darker green
        "collectible_color": (255, 200, 0),       # an orange-yellow
        "special_collectible_color": (200, 0, 200), # a magenta-ish purple
        "lava_color": (200, 0, 0)               # a darker red for lava
    }
]

def total_normal_collectibles(level_config):
    return len(level_config["collectibles"])

# --- Sprite Classes ---

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
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -self.jump_strength
            self.on_ground = False

        self.velocity_y += GRAVITY

        # Horizontal movement and collisions
        self.rect.x += self.velocity_x
        self.handle_horizontal_collisions(platforms)
        # Vertical movement and collisions
        self.rect.y += self.velocity_y
        self.handle_vertical_collisions(platforms)
        
        # Clamp player to playable area (inside border)
        playable_rect = pygame.Rect(BORDER_THICKNESS, BORDER_THICKNESS, 
                                    SCREEN_WIDTH - 2 * BORDER_THICKNESS, 
                                    SCREEN_HEIGHT - 2 * BORDER_THICKNESS)
        self.rect.clamp_ip(playable_rect)

    def handle_horizontal_collisions(self, platforms):
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if self.velocity_x > 0:
                    self.rect.right = plat.rect.left
                elif self.velocity_x < 0:
                    self.rect.left = plat.rect.right

    def handle_vertical_collisions(self, platforms):
        self.on_ground = False
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if self.velocity_y > 0:
                    self.rect.bottom = plat.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    self.rect.top = plat.rect.bottom
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
    def __init__(self, x, y, color=PURPLE):
        super().__init__(x, y, size=25, color=color)

# --- Level Runner Function ---
def run_level(level_config, level_number):
    # Retrieve custom colors from the level config (or use defaults)
    bg_color       = level_config.get("background_color", WHITE)
    plat_color     = level_config.get("platform_color", GREEN)
    coll_color     = level_config.get("collectible_color", YELLOW)
    spec_coll_color= level_config.get("special_collectible_color", PURPLE)
    lava_color     = level_config.get("lava_color", RED)
    
    # Create groups for this level
    all_sprites = pygame.sprite.Group()
    safe_platforms = pygame.sprite.Group()  # platforms where the player can stand
    collectible_group = pygame.sprite.Group()
    special_group = pygame.sprite.Group()

    # Create lava base platform (red) inside the border
    lava_platform = Platform(BORDER_THICKNESS, SCREEN_HEIGHT - 40 - BORDER_THICKNESS,
                             SCREEN_WIDTH - 2 * BORDER_THICKNESS, 40, color=lava_color)
    all_sprites.add(lava_platform)

    # Create safe platforms from level data using custom platform color
    platform_list = []
    for plat_data in level_config["platforms"]:
        plat = Platform(*plat_data, color=plat_color)
        safe_platforms.add(plat)
        all_sprites.add(plat)
        platform_list.append(plat)

    # Create normal collectibles using explicit positions and custom color
    for pos in level_config["collectibles"]:
        collectible = Collectible(*pos, color=coll_color)
        collectible_group.add(collectible)
        all_sprites.add(collectible)

    # Create the special collectible using its explicit position and custom color
    special_item = SpecialCollectible(*level_config["special_collectible"], color=spec_coll_color)
    special_group.add(special_item)
    all_sprites.add(special_item)

    # Place the player on the first safe platform
    start_plat = platform_list[0]
    player = Player(start_plat.rect.x + 10, start_plat.rect.y - 30)
    all_sprites.add(player)

    # Level parameters
    level_timer = level_config["timer"]
    total_normals = total_normal_collectibles(level_config)
    collected_normal = 0
    special_collected = False

    # Timer
    start_ticks = pygame.time.get_ticks()

    # Level game loop
    level_running = True
    level_win = False
    level_lose = False

    while level_running:
        CLOCK.tick(FPS)
        current_ticks = pygame.time.get_ticks()
        elapsed_seconds = (current_ticks - start_ticks) / 1000
        time_left = max(0, level_timer - elapsed_seconds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        if not level_win and not level_lose:
            player.update(safe_platforms.sprites())

            # Lose if player touches lava
            if player.rect.colliderect(lava_platform.rect):
                level_lose = True

            # Check for normal collectible collisions
            collected = pygame.sprite.spritecollide(player, collectible_group, True)
            if collected:
                collected_normal += len(collected)

            # Check for special collectible collision (only valid if all normal ones are collected)
            if collected_normal == total_normals and pygame.sprite.spritecollide(player, special_group, True):
                special_collected = True

            # Win condition: all collectibles (normal and special) collected
            if collected_normal >= total_normals and special_collected:
                level_win = True

            # Lose condition: timer runs out
            if time_left <= 0:
                level_lose = True

        # --- Drawing ---
        if level_win or level_lose:
            # Clear screen to background color and draw border
            SCREEN.fill(bg_color)
            pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
            if level_win:
                win_text = MESSAGE_FONT.render(f"Level {level_number} Complete!", True, BLUE)
                text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                SCREEN.blit(win_text, text_rect)
                pygame.display.flip()
                pygame.time.delay(1500)
                return "win"
            else:
                over_text = MESSAGE_FONT.render("Game Over!", True, RED)
                text_rect = over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                SCREEN.blit(over_text, text_rect)
                restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 60, 150, 40)
                pygame.draw.rect(SCREEN, BLUE, restart_button)
                restart_text = FONT.render("Restart", True, WHITE)
                restart_text_rect = restart_text.get_rect(center=restart_button.center)
                SCREEN.blit(restart_text, restart_text_rect)
                pygame.display.flip()

                waiting = True
                while waiting:
                    CLOCK.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if restart_button.collidepoint(pygame.mouse.get_pos()):
                                return "lose"
        else:
            SCREEN.fill(bg_color)
            all_sprites.draw(SCREEN)
            # UI elements: timer, collectibles counter, level number.
            timer_text = FONT.render(f"Time Left: {int(time_left)}", True, BLACK)
            SCREEN.blit(timer_text, (SCREEN_WIDTH - 180, 10))
            counter_text = FONT.render(
                f"Collectibles: {collected_normal}/{total_normals}  Special: {'Yes' if special_collected else 'No'}",
                True, BLACK)
            SCREEN.blit(counter_text, (10, 10))
            level_text = FONT.render(f"Level: {level_number}", True, BLACK)
            SCREEN.blit(level_text, (10, 40))
            # Draw border
            pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
            pygame.display.flip()

    return "lose"

# --- Main Game Loop ---
def main():
    current_level_index = 0
    while True:
        result = run_level(levels[current_level_index], current_level_index + 1)
        if result == "win":
            # If final level is complete, show final win screen with restart button.
            if current_level_index == len(levels) - 1:
                finished = False
                while not finished:
                    SCREEN.fill(WHITE)
                    pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
                    final_text = MESSAGE_FONT.render("You Win the Game!", True, BLUE)
                    text_rect = final_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                    SCREEN.blit(final_text, text_rect)
                    restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 60, 150, 40)
                    pygame.draw.rect(SCREEN, BLUE, restart_button)
                    restart_text = FONT.render("Restart", True, WHITE)
                    restart_text_rect = restart_text.get_rect(center=restart_button.center)
                    SCREEN.blit(restart_text, restart_text_rect)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if restart_button.collidepoint(pygame.mouse.get_pos()):
                                finished = True
                                current_level_index = 0  # Restart from level 1
            else:
                current_level_index += 1
        elif result == "lose":
            current_level_index = 0

if __name__ == "__main__":
    main()

import pygame
import sys



# Initialize pygame.
pygame.init()



# Set the screen settings.
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 900
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bario")
CLOCK = pygame.time.Clock()
FPS = 60



# Set the default colors.
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
BLUE    = (50, 100, 255)
GREEN   = (0, 255, 0)
RED     = (255, 50, 50)
YELLOW  = (255, 255, 0)
PURPLE  = (128, 0, 128)

ALICE_BLUE      = (240, 248, 255)
HONEYDEW        = (240, 255, 240)
LAVENDER_BLUSH  = (255, 240, 245)
BEIGE           = (245, 245, 220)
FOREST_GREEN    = (34, 139, 34)
STEEL_BLUE      = (70, 130, 180)
DARK_SLATE_GRAY = (47, 79, 79)
SADDLE_BROWN    = (139, 69, 19)

MIDNIGHT_BLUE    = (25, 25, 112)
CORNFLOWER_BLUE  = (100, 149, 237)
MEDIUM_PURPLE    = (147, 112, 219)
LIGHT_CORAL      = (240, 128, 128)
ORANGE_RED       = (255, 69, 0)

DARK_ORCHID      = (153, 50, 204)

SLATE_GRAY       = (112, 128, 144)
SLATE_BLUE       = (106, 90, 205)
GOLD             = (255, 215, 0)
DEEP_SKY_BLUE    = (0, 191, 255)

LIGHT_SKY_BLUE   = (135, 206, 250)
MEDIUM_SEA_GREEN = (60, 179, 113)
PALE_GOLDENROD   = (238, 232, 170)
MEDIUM_TURQUOISE = (72, 209, 204)

DIM_GRAY         = (105, 105, 105)
LIGHT_SLATE_GRAY = (119, 136, 153)
CHARTREUSE       = (127, 255, 0)
FUCHSIA          = (255, 0, 255)

DARK_BROWN     = (101, 67, 33)     # A deep brown for the background.
CHOCOLATE      = (123, 63, 0)      # A medium–dark brown for the platforms.
GOLDENROD      = (218, 165, 32)    # A warm mustard yellow for the collectibles.
DARK_ORANGE    = (255, 140, 0)     # A deep, rich orange for the special collectible.
FIREBRICK      = (178, 34, 34)     # A dark red–brown for the lava.
COOL_RED = (200, 0, 0)


# Set the border thickness.
BORDER_THICKNESS = 5



# Set the gravity factor.
GRAVITY = 0.5



# Set the fonts.
FONT = pygame.font.SysFont('Arial', 24)
MESSAGE_FONT = pygame.font.SysFont('Arial', 48)



levels = [

    # Level 1
    {
        "platforms": [
            (100, 600, 1600, 20),
        ],
        "collectibles": [
            (200, 580),
            (300, 580),
            (400, 580),
            (500, 580),
            (600, 580),
            (700, 580),
            (800, 580),
            (900, 580),
            (1000, 580),
            (1100, 580),
            (1200, 580),
            (1300, 580),
            (1400, 580),
            (1500, 580)
        ],
        "special_collectible": (1600, 580),
        "timer": 7,
        "gravity": 0.6,
        "background_color": PALE_GOLDENROD,
        "platform_color": DARK_SLATE_GRAY,
        "collectible_color": DARK_BROWN,
        "special_collectible_color": DARK_ORANGE,
        "lava_color": COOL_RED
    },

    # Level 2
    {
        "platforms": [
            (100, 800, 150, 20),
            (300, 700, 150, 20),
            (500, 600, 150, 20),
            (700, 500, 150, 20),
            (900, 400, 150, 20),
            (1100, 300, 150, 20),
            (1300, 200, 150, 20),
            (1500, 100, 150, 20)
        ],
        "collectibles": [
            (175, 785),
            (375, 685),
            (575, 585),
            (775, 485),
            (975, 385),
            (1175, 285),
            (1375, 185)
        ],
        "special_collectible": (1575, 80),
        "timer": 8,
        "gravity": 0.6,
        "background_color": (230, 230, 255),
        "platform_color": (0, 200, 0),
        "collectible_color": (255, 200, 0),
        "special_collectible_color": (200, 0, 200),
        "lava_color": (200, 0, 0)
    },

    # Level 3
    {
        "platforms": [
            (100, 800, 150, 20),
            (300, 700, 150, 20),
            (500, 600, 150, 20),
            (700, 500, 150, 20),
            (900, 400, 150, 20),
            (1100, 300, 150, 20),
            (1300, 200, 150, 20),
            (1500, 100, 150, 20),
            (1600, 800, 150, 20),
            (1400, 700, 150, 20),
            (1200, 600, 150, 20),
            (1000, 500, 150, 20),
            (600, 300, 150, 20),
            (400, 200, 150, 20),
            (200, 100, 150, 20)
        ],
        "collectibles": [
            (175, 785),
            (375, 685),
            (575, 585),
            (775, 485),
            (975, 385),
            (1175, 285),
            (1375, 185),
            (1575, 85),
            (1675, 785),
            (1475, 685),
            (1275, 585),
            (1075, 485),
            (675, 285),
            (475, 185)
        ],
        "special_collectible": (275, 85),
        "timer": 17,
        "gravity": 0.5,
        "background_color": (200, 255, 200),  # light green
        "platform_color": FOREST_GREEN,
        "collectible_color": (255, 215, 0),     # gold
        "special_collectible_color": (138, 43, 226),  # blue violet
        "lava_color": (255, 69, 0)              # orange red
    },

    # Level 4
    {
        "platforms": [
            (200, 800, 130, 20),
            (400, 750, 130, 20),
            (600, 700, 130, 20),
            (800, 650, 130, 20),
            (1000, 600, 130, 20),
            (1200, 550, 130, 20),
            (1400, 500, 130, 20),
            (1600, 450, 130, 20),
            (1800, 400, 130, 20)
        ],
        "collectibles": [
            (265, 685),
            (465, 645),
            (665, 605),
            (865, 565),
            (1065, 525)
        ],
        "special_collectible": (1265, 485),
        "timer": 18,
        "gravity": 0.5,
        "background_color": (240, 230, 140),  # khaki
        "platform_color": (139, 69, 19),        # saddlebrown
        "collectible_color": (255, 140, 0),       # dark orange
        "special_collectible_color": (75, 0, 130),# indigo
        "lava_color": (178, 34, 34)             # firebrick
    },

    # Level 5
    {
        "platforms": [
            (150, 720, 120, 20),
            (320, 680, 120, 20),
            (490, 640, 120, 20),
            (660, 600, 120, 20),
            (830, 560, 120, 20),
            (1000, 520, 120, 20)
        ],
        "collectibles": [
            (210, 705),
            (370, 665),
            (540, 625),
            (710, 585),
            (880, 545)
        ],
        "special_collectible": (1050, 505),
        "timer": 16,
        "gravity": 0.5,
        "background_color": (255, 228, 225),  # misty rose
        "platform_color": (205, 92, 92),        # indian red
        "collectible_color": (255, 160, 122),     # light salmon
        "special_collectible_color": (199, 21, 133),  # medium violet red
        "lava_color": (220, 20, 60)             # crimson
    },
    {
        "platforms": [
            (200, 730, 110, 20),
            (370, 690, 110, 20),
            (540, 650, 110, 20),
            (710, 610, 110, 20),
            (880, 570, 110, 20),
            (1050, 530, 110, 20)
        ],
        "collectibles": [
            (265, 715),
            (435, 675),
            (605, 635),
            (775, 595),
            (945, 555)
        ],
        "special_collectible": (1115, 515),
        "timer": 14,
        "gravity": 0.5,
        "background_color": (224, 255, 255),  # light cyan
        "platform_color": (32, 178, 170),       # light sea green
        "collectible_color": (0, 206, 209),       # turquoise
        "special_collectible_color": (72, 61, 139), # dark slate blue
        "lava_color": (139, 0, 0)               # dark red
    },
    {
        "platforms": [
            (250, 740, 100, 20),
            (400, 700, 100, 20),
            (550, 660, 100, 20),
            (700, 620, 100, 20),
            (850, 580, 100, 20),
            (1000, 540, 100, 20)
        ],
        "collectibles": [
            (300, 725),
            (450, 685),
            (600, 645),
            (750, 605),
            (900, 565)
        ],
        "special_collectible": (1050, 525),
        "timer": 12,
        "gravity": 0.5,
        "background_color": HONEYDEW,
        "platform_color": (60, 179, 113),  # medium sea green
        "collectible_color": (173, 255, 47),  # green yellow
        "special_collectible_color": (138, 43, 226),  # blue violet (reuse or change as desired)
        "lava_color": (165, 42, 42)           # brown
    },
    {
        "platforms": [
            (300, 750, 90, 20),
            (450, 700, 90, 20),
            (600, 650, 90, 20),
            (750, 600, 90, 20),
            (900, 550, 90, 20),
            (1050, 500, 90, 20)
        ],
        "collectibles": [
            (345, 735),
            (495, 685),
            (645, 635),
            (795, 585),
            (945, 535)
        ],
        "special_collectible": (1105, 465),
        "timer": 18,
        "gravity": 0.5,
        "background_color": LAVENDER_BLUSH,
        "platform_color": (218, 112, 214),  # orchid
        "collectible_color": (255, 182, 193),  # light pink
        "special_collectible_color": (199, 21, 133),  # medium violet red
        "lava_color": (255, 99, 71)           # tomato
    },
    {
        "platforms": [
            (350, 760, 80, 20),
            (500, 710, 80, 20),
            (650, 660, 80, 20),
            (800, 610, 80, 20),
            (950, 560, 80, 20),
            (1100, 510, 80, 20)
        ],
        "collectibles": [
            (390, 745),
            (540, 695),
            (690, 645),
            (840, 595),
            (990, 545)
        ],
        "special_collectible": (1150, 485),
        "timer": 18,
        "gravity": 0.5,
        "background_color": ALICE_BLUE,
        "platform_color": STEEL_BLUE,
        "collectible_color": (255, 215, 0),  # gold
        "special_collectible_color": (75, 0, 130),  # indigo
        "lava_color": SADDLE_BROWN
    },
    {
        "platforms": [
            (400, 770, 70, 20),
            (540, 720, 70, 20),
            (680, 670, 70, 20),
            (820, 620, 70, 20),
            (960, 570, 70, 20),
            (1100, 520, 70, 20)
        ],
        "collectibles": [
            (435, 755),
            (575, 705),
            (715, 655),
            (855, 605),
            (995, 555)
        ],
        "special_collectible": (1155, 505),
        "timer": 16,
        "gravity": 0.5,
        "background_color": BEIGE,
        "platform_color": DARK_SLATE_GRAY,
        "collectible_color": (255, 105, 180),  # hot pink
        "special_collectible_color": (138, 43, 226),  # blue violet
        "lava_color": (128, 0, 0)             # maroon
    },
    {
        "platforms": [
            (100, 800, 100, 20),
            (350, 750, 100, 20),
            (600, 700, 100, 20),
            (850, 650, 100, 20),
            (1100, 600, 100, 20),
            (1350, 550, 100, 20)
        ],
        "collectibles": [
            (150, 785),
            (400, 735),
            (650, 685),
            (900, 635),
            (1150, 585)
        ],
        "special_collectible": (1400, 535),
        "timer": 15,
        "gravity": 0.5,
        "background_color": MIDNIGHT_BLUE,
        "platform_color": CORNFLOWER_BLUE,
        "collectible_color": LIGHT_CORAL,
        "special_collectible_color": MEDIUM_PURPLE,
        "lava_color": ORANGE_RED
    },
    # Level 12
    {
        "platforms": [
            (150, 780, 90, 20),
            (400, 730, 90, 20),
            (650, 680, 90, 20),
            (900, 630, 90, 20),
            (1150, 580, 90, 20),
            (1400, 530, 90, 20)
        ],
        "collectibles": [
            (195, 765),
            (445, 715),
            (695, 665),
            (945, 615),
            (1195, 565)
        ],
        "special_collectible": (1450, 485),
        "timer": 14,
        "gravity": 0.5,
        "background_color": DARK_ORCHID,
        "platform_color": (218, 112, 214),  # Orchid
        "collectible_color": (255, 182, 193), # Light Pink
        "special_collectible_color": (199, 21, 133),  # Medium Violet Red
        "lava_color": (139, 0, 0)  # Dark Red
    },
    # Level 13
    {
        "platforms": [
            (200, 760, 80, 20),
            (370, 710, 80, 20),
            (540, 660, 80, 20),
            (710, 610, 80, 20),
            (880, 560, 80, 20),
            (1050, 510, 80, 20)
        ],
        "collectibles": [
            (240, 745),
            (410, 700),
            (580, 655),
            (750, 605),
            (920, 555)
        ],
        "special_collectible": (1090, 465),
        "timer": 13,
        "gravity": 0.5,
        "background_color": SLATE_GRAY,
        "platform_color": SLATE_BLUE,
        "collectible_color": GOLD,
        "special_collectible_color": DEEP_SKY_BLUE,
        "lava_color": (220, 20, 60)  # Crimson
    },
    # Level 14
    {
        "platforms": [
            (250, 750, 70, 20),
            (400, 700, 70, 20),
            (550, 650, 70, 20),
            (700, 600, 70, 20),
            (850, 550, 70, 20),
            (1000, 500, 70, 20)
        ],
        "collectibles": [
            (285, 735),
            (435, 685),
            (585, 635),
            (735, 585),
            (885, 535)
        ],
        "special_collectible": (1050, 465),
        "timer": 12,
        "gravity": 0.5,
        "background_color": LIGHT_SKY_BLUE,
        "platform_color": MEDIUM_SEA_GREEN,
        "collectible_color": PALE_GOLDENROD,
        "special_collectible_color": MEDIUM_TURQUOISE,
        "lava_color": (178, 34, 34)  # Firebrick
    },
    # Level 15
    {
        "platforms": [
            (300, 740, 60, 20),
            (430, 690, 60, 20),
            (560, 640, 60, 20),
            (690, 590, 60, 20),
            (820, 540, 60, 20),
            (950, 490, 60, 20)
        ],
        "collectibles": [
            (330, 725),
            (460, 675),
            (590, 625),
            (720, 575),
            (850, 525)
        ],
        "special_collectible": (1010, 455),
        "timer": 12,
        "gravity": 0.5,
        "background_color": DIM_GRAY,
        "platform_color": LIGHT_SLATE_GRAY,
        "collectible_color": CHARTREUSE,
        "special_collectible_color": FUCHSIA,
        "lava_color": (139, 0, 0)  # Dark Red
    }
]



def total_normal_collectibles (level_config):
    
    return len(level_config["collectibles"])



class Player (pygame.sprite.Sprite):

    def __init__ (self, x, y, gravity=0.5):

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
        self.gravity = gravity  # Store gravity for this instance


    def update(self, platforms):
        
        keys = pygame.key.get_pressed()
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.velocity_y = -self.jump_strength
            self.on_ground = False

        # Use the instance's gravity rather than a global constant.
        self.velocity_y += self.gravity

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


    def handle_horizontal_collisions (self, platforms):

        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if self.velocity_x > 0:
                    self.rect.right = plat.rect.left
                elif self.velocity_x < 0:
                    self.rect.left = plat.rect.right


    def handle_vertical_collisions (self, platforms):

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



class Platform (pygame.sprite.Sprite):

    def __init__ (self, x, y, width, height, color = GREEN):

        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))



class Collectible (pygame.sprite.Sprite):

    def __init__ (self, x, y, size = 20, color = YELLOW):

        super().__init__()
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))



class SpecialCollectible (Collectible):

    def __init__ (self, x, y, color = PURPLE):

        super().__init__(x, y, size = 25, color = color)



def wait_for_key_release():
    # Wait until no key is pressed.
    waiting = True
    while waiting:
        pygame.event.pump()  # update the internal state
        keys = pygame.key.get_pressed()
        if not any(keys):  # if no key is pressed
            waiting = False
        CLOCK.tick(FPS)




def run_level(level_config, level_number):
    # Retrieve custom colors from the level config (or use defaults)
    bg_color       = level_config.get("background_color", WHITE)
    plat_color     = level_config.get("platform_color", GREEN)
    coll_color     = level_config.get("collectible_color", YELLOW)
    spec_coll_color= level_config.get("special_collectible_color", PURPLE)
    lava_color     = level_config.get("lava_color", RED)
    
    # Create groups for this level
    all_sprites = pygame.sprite.Group()
    safe_platforms = pygame.sprite.Group()
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
    # Create the player and set gravity from level_config.
    player = Player(start_plat.rect.x + 10, start_plat.rect.y - 30, gravity=level_config.get("gravity", GRAVITY))
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
                
                # Create two buttons: one for restarting the same level and one for restarting the game from level 1.
                restart_level_button = pygame.Rect(SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 + 60, 150, 40)
                restart_game_button = pygame.Rect(SCREEN_WIDTH//2 + 50, SCREEN_HEIGHT//2 + 60, 150, 40)
                pygame.draw.rect(SCREEN, BLUE, restart_level_button)
                pygame.draw.rect(SCREEN, BLUE, restart_game_button)
                
                restart_level_text = FONT.render("Restart Level", True, WHITE)
                restart_game_text = FONT.render("Restart Game", True, WHITE)
                SCREEN.blit(restart_level_text, restart_level_text.get_rect(center=restart_level_button.center))
                SCREEN.blit(restart_game_text, restart_game_text.get_rect(center=restart_game_button.center))
                
                pygame.display.flip()

                waiting = True
                while waiting:
                    CLOCK.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if restart_level_button.collidepoint(mouse_pos):
                                wait_for_key_release()
                                return "restart_level"
                            if restart_game_button.collidepoint(mouse_pos):
                                wait_for_key_release()
                                return "lose"
                        if event.type == pygame.KEYDOWN:
                            # SPACE => restart current level.
                            if event.key == pygame.K_SPACE:
                                wait_for_key_release()
                                return "restart_level"
                            # ENTER => restart game (from level 1).
                            elif event.key == pygame.K_RETURN:
                                wait_for_key_release()
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


def main_menu():
    """
    Displays the main menu with two buttons: "Play Normal" and "Level Select".
    Returns:
      - "normal" if "Play Normal" is selected.
      - "select" if "Level Select" is selected.
    """
    while True:
        SCREEN.fill(WHITE)
        pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
        
        title_text = MESSAGE_FONT.render("Bario", True, BLUE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 150))
        SCREEN.blit(title_text, title_rect)
        
        # Define buttons
        play_button = pygame.Rect(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 - 50, 300, 50)
        select_button = pygame.Rect(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 + 20, 300, 50)
        
        pygame.draw.rect(SCREEN, BLUE, play_button)
        pygame.draw.rect(SCREEN, BLUE, select_button)
        
        play_text = FONT.render("Play Normal", True, WHITE)
        select_text = FONT.render("Level Select", True, WHITE)
        
        SCREEN.blit(play_text, play_text.get_rect(center=play_button.center))
        SCREEN.blit(select_text, select_text.get_rect(center=select_button.center))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    wait_for_key_release()
                    return "normal"
                if select_button.collidepoint(mouse_pos):
                    wait_for_key_release()
                    return "select"
            if event.type == pygame.KEYDOWN:
                # Optionally, you could choose keys for menu selection
                if event.key == pygame.K_n:
                    wait_for_key_release()
                    return "normal"
                elif event.key == pygame.K_s:
                    wait_for_key_release()
                    return "select"
        CLOCK.tick(FPS)

def level_select_menu():
    """
    Displays 15 buttons (or however many levels are in the levels variable).
    Returns the selected level index (0-indexed).
    """
    num_levels = len(levels)  # Assuming your global levels variable contains 15 levels.
    # For layout, we display buttons in a grid – for instance, 5 per row.
    buttons_per_row = 5
    button_width = 150
    button_height = 50
    margin = 20
    
    while True:
        SCREEN.fill(WHITE)
        pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
        
        header_text = MESSAGE_FONT.render("Select Level", True, BLUE)
        header_rect = header_text.get_rect(center=(SCREEN_WIDTH//2, 80))
        SCREEN.blit(header_text, header_rect)
        
        level_buttons = []
        for i in range(num_levels):
            row = i // buttons_per_row
            col = i % buttons_per_row
            # Calculate button positions centered on screen.
            total_width = buttons_per_row * button_width + (buttons_per_row - 1) * margin
            start_x = (SCREEN_WIDTH - total_width) // 2
            x = start_x + col * (button_width + margin)
            y = 150 + row * (button_height + margin)
            btn_rect = pygame.Rect(x, y, button_width, button_height)
            level_buttons.append(btn_rect)
            pygame.draw.rect(SCREEN, BLUE, btn_rect)
            level_text = FONT.render(f"Level {i+1}", True, WHITE)
            SCREEN.blit(level_text, level_text.get_rect(center=btn_rect.center))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, btn in enumerate(level_buttons):
                    if btn.collidepoint(mouse_pos):
                        wait_for_key_release()
                        return i  # Return level index (0-indexed)
            if event.type == pygame.KEYDOWN:
                # Optional: allow key selection for levels 1-9 via number keys, etc.
                pass
        
        CLOCK.tick(FPS)


def main():
    # Show main menu first.
    menu_choice = main_menu()
    if menu_choice == "normal":
        current_level_index = 0
    else:  # "select"
        # Open level select menu.
        current_level_index = level_select_menu()
    
    while True:
        result = run_level(levels[current_level_index], current_level_index + 1)
        if result == "win":
            if current_level_index == len(levels) - 1:
                finished = False
                while not finished:
                    SCREEN.fill(WHITE)
                    pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
                    final_text = MESSAGE_FONT.render("You Win the Game!", True, BLUE)
                    text_rect = final_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
                    SCREEN.blit(final_text, text_rect)
                    
                    # Final win screen buttons.
                    restart_game_button  = pygame.Rect(SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 + 60, 150, 40)
                    restart_level_button = pygame.Rect(SCREEN_WIDTH//2 + 50, SCREEN_HEIGHT//2 + 60, 150, 40)
                    pygame.draw.rect(SCREEN, BLUE, restart_game_button)
                    pygame.draw.rect(SCREEN, BLUE, restart_level_button)
                    restart_game_text  = FONT.render("Restart Game", True, WHITE)
                    restart_level_text = FONT.render("Replay Last", True, WHITE)
                    SCREEN.blit(restart_game_text, restart_game_text.get_rect(center=restart_game_button.center))
                    SCREEN.blit(restart_level_text, restart_level_text.get_rect(center=restart_level_button.center))
                    pygame.display.flip()
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if restart_game_button.collidepoint(mouse_pos):
                                wait_for_key_release()
                                finished = True
                                current_level_index = 0
                            elif restart_level_button.collidepoint(mouse_pos):
                                wait_for_key_release()
                                finished = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                wait_for_key_release()
                                finished = True
                                current_level_index = 0
                            elif event.key == pygame.K_SPACE:
                                wait_for_key_release()
                                finished = True
                # After final win, show the main menu again.
                main()
                return
            else:
                current_level_index += 1
        elif result == "lose":
            current_level_index = 0
        elif result == "restart_level":
            continue



if __name__ == "__main__":

    # Run the game.
    main()
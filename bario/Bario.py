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

DARK_BROWN     = (101, 67, 33)
CHOCOLATE      = (123, 63, 0)
GOLDENROD      = (218, 165, 32)
DARK_ORANGE    = (255, 140, 0)
FIREBRICK      = (178, 34, 34)
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
        "background_color": (200, 255, 200),
        "platform_color": FOREST_GREEN,
        "collectible_color": (255, 215, 0),
        "special_collectible_color": (138, 43, 226),
        "lava_color": (255, 69, 0) 
    },

    # Level 4
    {
        "platforms": [
            (200, 200, 130, 20),
            (400, 400, 130, 20),
            (600, 800, 130, 20),
            (400, 600, 130, 20),
            (800, 800, 130, 20),
            (900, 700, 130, 20),
            (1100, 600, 130, 20),
            (1200, 700, 130, 20),
            (1570, 700, 130, 20)
        ],
        "collectibles": [
            (280, 180),
            (480, 380),
            (680, 780),
            (480, 580),
            (880, 780),
            (980, 680),
            (1180, 580),
            (1280, 680)
        ],
        "special_collectible": (1680, 680),
        "timer": 13,
        "gravity": 0.5,
        "background_color": (240, 230, 140),
        "platform_color": (139, 69, 19),
        "collectible_color": (255, 140, 0),
        "special_collectible_color": (75, 0, 130),
        "lava_color": (178, 34, 34)
    },

    # Level 5
    {
        "platforms": [
            (100, 720, 120, 20),
            (350, 680, 120, 20),
            (600, 640, 120, 20),
            (850, 600, 120, 20),
            (1100, 560, 120, 20),
            (1350, 520, 120, 20),
            (1600, 480, 120, 20)
        ],
        "collectibles": [
            (170, 700),
            (420, 660),
            (670, 620),
            (920, 580),
            (1170, 540),
            (1420, 500)
        ],
        "special_collectible": (1670, 460),
        "timer": 8,
        "gravity": 0.8,
        "background_color": (255, 228, 225),
        "platform_color": (205, 92, 92),
        "collectible_color": (255, 160, 122),
        "special_collectible_color": (199, 21, 133),
        "lava_color": (220, 20, 60)
    },

    # Level 6
    {
        "platforms": [
            (100, 100, 110, 20),
            (200, 200, 110, 20),
            (300, 300, 110, 20),
            (400, 400, 110, 20),
            (500, 500, 110, 20),
            (600, 600, 110, 20),
            (700, 700, 110, 20),
            (800, 800, 110, 20),
            (900, 900, 110, 20),
            (1000, 800, 110, 20),
            (1100, 700, 110, 20),
            (1200, 600, 110, 20),
            (1300, 500, 110, 20),
            (1400, 400, 110, 20),
            (1500, 300, 110, 20),
            (1500, 200, 110, 20),
            (1300, 300, 110, 20),
            (1100, 400, 110, 20),
            (900, 500, 110, 20),
            (700, 600, 110, 20),
            (500, 700, 110, 20),
            (300, 800, 110, 20),
            (100, 900, 110, 20)
        ],
        "collectibles": [
            (160, 80),
            (260, 180),
            (360, 280),
            (460, 380),
            (560, 480),
            (660, 580),
            (760, 680),
            (860, 780),
            (1060, 780),
            (1160, 680),
            (1260, 580),
            (1360, 480),
            (1460, 380),
        ],
        "special_collectible": (1115, 515),
        "timer": 17,
        "gravity": 0.5,
        "background_color": (224, 255, 255),
        "platform_color": (32, 178, 170),
        "collectible_color": (0, 206, 209),
        "special_collectible_color": (72, 61, 139),
        "lava_color": (139, 0, 0)
    },

    # Level 7
    {
        "platforms": [
            (100, 740, 200, 20),
            (400, 700, 100, 20),
            (550, 660, 100, 20),
            (700, 620, 100, 20),
            (850, 580, 100, 20),
            (1000, 540, 100, 20),
            (1150, 500, 100, 20),
            (1300, 460, 100, 20)
        ],
        "collectibles": [
            (260, 725),
            (450, 685),
            (600, 645),
            (750, 605),
            (900, 565),
            (1050, 525),
            (1200, 485),
            (1350, 445)
        ],
        "special_collectible": (200, 725),
        "timer": 9,
        "gravity": 0.1,
        "background_color": HONEYDEW,
        "platform_color": (60, 179, 113),
        "collectible_color": (173, 255, 47),
        "special_collectible_color": (138, 43, 226),
        "lava_color": (165, 42, 42)
    },

    # Level 8
    {
        "platforms": [
            (1600, 650, 90, 20),
            (1500, 700, 90, 20),
            (1400, 650, 90, 20),
            (1300, 700, 90, 20),
            (1200, 650, 90, 20),
            (1100, 700, 90, 20),
            (1000, 650, 90, 20),
            (900, 700, 90, 20),
            (800, 650, 90, 20),
            (700, 700, 90, 20),
            (600, 650, 90, 20),
            (500, 700, 90, 20),
            (400, 650, 90, 20),
            (300, 700, 90, 20)
        ],
        "collectibles": [
            (1660, 630),
            (1560, 680),
            (1460, 630),
            (1360, 680),
            (1260, 630),
            (1160, 680),
            (1060, 630),
            (960, 680),
            (860, 630),
            (760, 680),
            (660, 630),
            (560, 680),
            (460, 630),
            (360, 680)
        ],
        "special_collectible": (120, 800),
        "timer": 10,
        "gravity": 0.9,
        "background_color": LAVENDER_BLUSH,
        "platform_color": (218, 112, 214),
        "collectible_color": (255, 182, 193),
        "special_collectible_color": (199, 21, 133),
        "lava_color": (255, 99, 71)
    },

    # Level 9
    {
        "platforms": [
            (400, 800, 100, 20)
        ],
        "collectibles": [
            (480, 780),
            (440, 720),
            (500, 660),
            (560, 600),
            (620, 540),
            (640, 480),
            (620, 420),
            (780, 360),
            (760, 300),
            (720, 240),
            (880, 180),
            (840, 120)
        ],
        "special_collectible": (650, 780),
        "timer": 18,
        "gravity": 0.1,
        "background_color": ALICE_BLUE,
        "platform_color": STEEL_BLUE,
        "collectible_color": (255, 215, 0),
        "special_collectible_color": (75, 0, 130),
        "lava_color": SADDLE_BROWN
    },

    # Level 10
    {
        "platforms": [
            (100, 800, 100, 20),
            (250, 750, 90, 20),
            (400, 700, 80, 20),
            (550, 650, 70, 20),
            (700, 600, 60, 20),
            (850, 550, 50, 20),
            (1000, 500, 40, 20),
            (1150, 450, 30, 20),
            (1300, 400, 20, 20),
            (1450, 350, 10, 20),
            (1600, 300, 1, 20),
            (1650, 800, 5, 20)
        ],
        "collectibles": [
            (170, 780),
            (310, 730),
            (450, 680),
            (590, 630),
            (730, 580),
            (870, 530),
            (1015, 480),
            (1160, 430),
            (1305, 380),
            (1452, 330),
            (1596, 280)
        ],
        "special_collectible": (1660, 780),
        "timer": 14,
        "gravity": 0.7,
        "background_color": BEIGE,
        "platform_color": DARK_SLATE_GRAY,
        "collectible_color": (255, 105, 180),
        "special_collectible_color": (138, 43, 226),
        "lava_color": (128, 0, 0)
    },

    # Level 11
    {
        "platforms": [
            (100, 800, 100, 20),
            (100, 700, 100, 20),
            (100, 600, 100, 20),
            (100, 500, 100, 20),
            (100, 400, 100, 20),
            (100, 300, 100, 20),
            (100, 200, 100, 20),
            (100, 100, 100, 20),
            (300, 800, 100, 20),
            (300, 700, 100, 20),
            (300, 600, 100, 20),
            (300, 500, 100, 20),
            (300, 400, 100, 20),
            (300, 300, 100, 20),
            (300, 200, 100, 20),
            (300, 100, 100, 20),
            (500, 800, 100, 20),
            (500, 700, 100, 20),
            (500, 600, 100, 20),
            (500, 500, 100, 20),
            (500, 400, 100, 20),
            (500, 300, 100, 20),
            (500, 200, 100, 20),
            (500, 100, 100, 20),
            (700, 800, 100, 20),
            (700, 700, 100, 20),
            (700, 600, 100, 20),
            (700, 500, 100, 20),
            (700, 400, 100, 20),
            (700, 300, 100, 20),
            (700, 200, 100, 20),
            (700, 100, 100, 20),
            (900, 800, 100, 20),
            (900, 700, 100, 20),
            (900, 600, 100, 20),
            (900, 500, 100, 20),
            (900, 400, 100, 20),
            (900, 300, 100, 20),
            (900, 200, 100, 20),
            (900, 100, 100, 20),
            (1100, 800, 100, 20),
            (1100, 700, 100, 20),
            (1100, 600, 100, 20),
            (1100, 500, 100, 20),
            (1100, 400, 100, 20),
            (1100, 300, 100, 20),
            (1100, 200, 100, 20),
            (1100, 100, 100, 20),
            (1300, 800, 100, 20),
            (1300, 700, 100, 20),
            (1300, 600, 100, 20),
            (1300, 500, 100, 20),
            (1300, 400, 100, 20),
            (1300, 300, 100, 20),
            (1300, 200, 100, 20),
            (1300, 100, 100, 20),
            (1500, 800, 100, 20),
            (1500, 700, 100, 20),
            (1500, 600, 100, 20),
            (1500, 500, 100, 20),
            (1500, 400, 100, 20),
            (1500, 300, 100, 20),
            (1500, 200, 100, 20),
            (1500, 100, 100, 20)
        ],
        "collectibles": [
            (150, 780),
            (150, 680),
            (150, 580),
            (150, 480),
            (150, 380),
            (150, 280),
            (150, 180),
            (150, 80),
            (350, 780),
            (350, 680),
            (350, 580),
            (350, 480),
            (350, 380),
            (350, 280),
            (350, 180),
            (350, 80),
            (550, 780),
            (550, 680),
            (550, 580),
            (550, 480),
            (550, 380),
            (550, 280),
            (550, 180),
            (550, 80),
            (750, 780),
            (750, 680),
            (750, 580),
            (750, 480),
            (750, 380),
            (750, 280),
            (750, 180),
            (750, 80),
            (950, 780),
            (950, 680),
            (950, 580),
            (950, 480),
            (950, 380),
            (950, 280),
            (950, 180),
            (950, 80),
            (1150, 780),
            (1150, 680),
            (1150, 580),
            (1150, 480),
            (1150, 380),
            (1150, 280),
            (1150, 180),
            (1150, 80),
            (1350, 780),
            (1350, 680),
            (1350, 580),
            (1350, 480),
            (1350, 380),
            (1350, 280),
            (1350, 180),
            (1350, 80),
            (1550, 780),
            (1550, 680),
            (1550, 580),
            (1550, 480),
            (1550, 380),
            (1550, 280),
            (1550, 180)
        ],
        "special_collectible": (1550, 80),
        "timer": 180,
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
            (100, 250, 30, 20),
            (300, 250, 30, 20),
            (500, 250, 30, 20),
            (700, 250, 30, 20),
            (900, 250, 30, 20),
            (1100, 250, 30, 20),
            (1300, 250, 30, 20),
            (1500, 250, 30, 20)
        ],
        "collectibles": [
            (130, 230),
            (330, 230),
            (530, 230),
            (730, 230),
            (930, 230),
            (1130, 230),
            (1330, 230),
            (1530, 230)
        ],
        "special_collectible": (200, 400),
        "timer": 18,
        "gravity": 0.6,
        "background_color": DARK_ORCHID,
        "platform_color": (218, 112, 214),
        "collectible_color": (255, 182, 193),
        "special_collectible_color": (199, 21, 133),
        "lava_color": (139, 0, 0)
    },

    # Level 13
    {
        "platforms": [
            (100, 100, 80, 20),
            (300, 200, 80, 20),
            (500, 300, 80, 20),
            (700, 400, 80, 20),
            (900, 500, 80, 20),
            (1100, 600, 80, 20),
            (1300, 700, 80, 20),
            (1500, 800, 80, 20)
        ],
        "collectibles": [
            (120, 80),
            (320, 180),
            (520, 280),
            (720, 380),
            (920, 480),
            (1120, 580),
            (1320, 680)
        ],
        "special_collectible": (1520, 780),
        "timer": 13,
        "gravity": 0.7,
        "background_color": SLATE_GRAY,
        "platform_color": SLATE_BLUE,
        "collectible_color": GOLD,
        "special_collectible_color": DEEP_SKY_BLUE,
        "lava_color": (220, 20, 60)
    },

    # Level 14
    {
        "platforms": [
            (250, 750, 70, 20)
        ],
        "collectibles": [
            (600, 200)
        ],
        "special_collectible": (1000, 800),
        "timer": 12,
        "gravity": 0.1,
        "background_color": LIGHT_SKY_BLUE,
        "platform_color": MEDIUM_SEA_GREEN,
        "collectible_color": PALE_GOLDENROD,
        "special_collectible_color": MEDIUM_TURQUOISE,
        "lava_color": (178, 34, 34) 
    },

    # Level 15
    {
        "platforms": [
            (100, 800, 50, 20),
            (200, 700, 1, 20),
            (300, 600, 1, 20),
            (400, 500, 1, 20),
            (500, 400, 1, 20),
            (600, 300, 1, 20),
            (700, 200, 1, 20),
            (800, 100, 1, 20),
            (900, 200, 1, 20),
            (1000, 300, 1, 20),
            (1100, 400, 1, 20),
            (1200, 500, 1, 20),
            (1300, 600, 1, 20),
            (1400, 700, 1, 20),
            (1500, 800, 1, 20)
        ],
        "collectibles": [
            (150, 780),
            (200, 680),
            (300, 580),
            (400, 480),
            (500, 380),
            (600, 280),
            (700, 180),
            (800, 80),
            (900, 180),
            (1000, 280),
            (1100, 380),
            (1200, 480),
            (1300, 580),
            (1400, 680),
            (1500, 780)
        ],
        "special_collectible": (1100, 700),
        "timer": 17,
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

    def __init__ (self, x, y, gravity = 0.5):

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
        self.gravity = gravity


    def update (self, platforms):
        
        keys = pygame.key.get_pressed()
        self.velocity_x = 0

        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.velocity_y = -self.jump_strength
            self.on_ground = False

        self.velocity_y += self.gravity

        # Horizontal movement and collisions.
        self.rect.x += self.velocity_x
        self.handle_horizontal_collisions(platforms)

        # Vertical movement and collisions.
        self.rect.y += self.velocity_y
        self.handle_vertical_collisions(platforms)
        
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
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if not any(keys):
            waiting = False
        CLOCK.tick(FPS)



def run_level (level_config, level_number):

    bg_color       = level_config.get("background_color", WHITE)
    plat_color     = level_config.get("platform_color", GREEN)
    coll_color     = level_config.get("collectible_color", YELLOW)
    spec_coll_color= level_config.get("special_collectible_color", PURPLE)
    lava_color     = level_config.get("lava_color", RED)
    
    all_sprites = pygame.sprite.Group()
    safe_platforms = pygame.sprite.Group()
    collectible_group = pygame.sprite.Group()
    special_group = pygame.sprite.Group()

    lava_platform = Platform(BORDER_THICKNESS, SCREEN_HEIGHT - 40 - BORDER_THICKNESS,
                             SCREEN_WIDTH - 2 * BORDER_THICKNESS, 40, color=lava_color)
    
    all_sprites.add(lava_platform)

    platform_list = []

    for plat_data in level_config["platforms"]:
        plat = Platform(*plat_data, color=plat_color)
        safe_platforms.add(plat)
        all_sprites.add(plat)
        platform_list.append(plat)

    for pos in level_config["collectibles"]:
        collectible = Collectible(*pos, color=coll_color)
        collectible_group.add(collectible)
        all_sprites.add(collectible)

    special_item = SpecialCollectible(*level_config["special_collectible"], color=spec_coll_color)
    special_group.add(special_item)
    all_sprites.add(special_item)

    # Place the player on the first safe platform.
    start_plat = platform_list[0]

    player = Player(start_plat.rect.x + 10, start_plat.rect.y - 30, gravity=level_config.get("gravity", GRAVITY))
    all_sprites.add(player)

    level_timer = level_config["timer"]
    total_normals = total_normal_collectibles(level_config)
    collected_normal = 0
    special_collected = False

    start_ticks = pygame.time.get_ticks()

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

            # Lose if player touches lava.
            if player.rect.colliderect(lava_platform.rect):
                level_lose = True

            # Check for normal collectible collisions.
            collected = pygame.sprite.spritecollide(player, collectible_group, True)
            if collected:
                collected_normal += len(collected)

            # Check for special collectible collision (only valid if all normal ones are collected).
            if collected_normal == total_normals and pygame.sprite.spritecollide(player, special_group, True):
                special_collected = True

            # Win condition: all collectibles (normal and special) collected.
            if collected_normal >= total_normals and special_collected:
                level_win = True

            # Lose condition: timer runs out.
            if time_left <= 0:
                level_lose = True

        if level_win or level_lose:

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

            timer_text = FONT.render(f"Time Left: {int(time_left)}", True, BLACK)
            SCREEN.blit(timer_text, (SCREEN_WIDTH - 180, 10))

            counter_text = FONT.render(
                f"Collectibles: {collected_normal}/{total_normals}  Special: {'Yes' if special_collected else 'No'}",
                True, BLACK)
            
            SCREEN.blit(counter_text, (10, 10))
            level_text = FONT.render(f"Level: {level_number}", True, BLACK)
            SCREEN.blit(level_text, (10, 40))

            pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
            pygame.display.flip()

    return "lose"



def main_menu ():

    while True:

        SCREEN.fill(WHITE)
        pygame.draw.rect(SCREEN, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), BORDER_THICKNESS)
        
        title_text = MESSAGE_FONT.render("Bario", True, BLUE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 150))
        SCREEN.blit(title_text, title_rect)
        
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
                if event.key == pygame.K_n:
                    wait_for_key_release()
                    return "normal"
                elif event.key == pygame.K_s:
                    wait_for_key_release()
                    return "select"
                
        CLOCK.tick(FPS)



def level_select_menu ():

    num_levels = len(levels)
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
                        return i
            if event.type == pygame.KEYDOWN:
                pass
        
        CLOCK.tick(FPS)


def main ():

    menu_choice = main_menu()

    if menu_choice == "normal":
        current_level_index = 0
    else:
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
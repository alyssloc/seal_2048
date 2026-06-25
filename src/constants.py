import pygame

# dimensions and colors
WIDTH: int = 720
HEIGHT: int  = 1280
GRID_SIZE: int = 4
CELL_SIZE: int = 120
FPS: int = 60
BACKGROUND_COLOR = (70, 30, 180)
CELL_BG_COLOR = (240, 240, 240)
DARK_BLUE = (11, 11, 69)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 218, 3)
CUSTOM_FONT = "fonts/clear-sans.bold.ttf"

# mapping 2048 numbers to corresponding seal images (most -> least common species)
TILE_IMAGES = {
    0: WHITE,
    2: pygame.transform.scale(pygame.image.load("pics/harp_2.png"), (CELL_SIZE, CELL_SIZE)),
    4: pygame.transform.scale(pygame.image.load("pics/ringed_4.png"), (CELL_SIZE, CELL_SIZE)),
    8: pygame.transform.scale(pygame.image.load("pics/north_fur_8.png"), (CELL_SIZE, CELL_SIZE)),
    16: pygame.transform.scale(pygame.image.load("pics/spotted_16.png"), (CELL_SIZE, CELL_SIZE)),
    32: pygame.transform.scale(pygame.image.load("pics/hooded_32.png"), (CELL_SIZE, CELL_SIZE)),
    64: pygame.transform.scale(pygame.image.load("pics/gray_64.png"), (CELL_SIZE, CELL_SIZE)),
    128: pygame.transform.scale(pygame.image.load("pics/bearded_128.png"), (CELL_SIZE, CELL_SIZE)),
    256: pygame.transform.scale(pygame.image.load("pics/harbor_256.png"), (CELL_SIZE, CELL_SIZE)),
    512: pygame.transform.scale(pygame.image.load("pics/cal_512.png"), (CELL_SIZE, CELL_SIZE)),
    1024: pygame.transform.scale(pygame.image.load("pics/ribbon_1024.png"), (CELL_SIZE, CELL_SIZE)),
    2048: pygame.transform.scale(pygame.image.load("pics/elephant_2048.png"), (CELL_SIZE, CELL_SIZE)),
    4096: pygame.transform.scale(pygame.image.load("pics/steller_4096.png"), (CELL_SIZE, CELL_SIZE)),
    8192: pygame.transform.scale(pygame.image.load("pics/guadalupe_8192.png"), (CELL_SIZE, CELL_SIZE)),
    16384: pygame.transform.scale(pygame.image.load("pics/med_16384.png"), (CELL_SIZE, CELL_SIZE)),
    32768: pygame.transform.scale(pygame.image.load("pics/hawiian_32768.png"), (CELL_SIZE, CELL_SIZE)),
}

# mapping for seal names for key in display
SEAL_NAMES = {
    2: "Harp Seal",
    4: "Ringed Seal",
    8: "Northern Fur Seal",
    16: "Spotted Seal",
    32: "Hooded Seal",
    64: "Gray Seal",
    128: "Bearded Seal",
    256: "Harbor Seal",
    512: "California Sea Lion",
    1024: "Ribbon Seal",
    2048: "Elephant Seal",
    4096: "Steller Sea Lion",
    8192: "Guadalupe Fur Seal",
    16384: "Mediterranean Monk Seal",
    32768: "Hawaiian Monk Seal"
}

# creating a background color for each different seal
SEAL_BACKGROUND_COLORS = {
    0: WHITE,
    2: (182, 208, 226),  
    4: (135, 206, 235),    
    8: (135, 206, 250),    
    16: (176, 224, 230),    
    32: (65, 105, 225),    #
    64: (153, 221, 255),     
    128: (224, 255, 255),
    256: (175, 238, 238),   
    512: (64, 181, 173),   
    1024: (8, 143, 143),  
    2048: (100, 149, 237),  
    4096: (111, 143, 175),   
    8192: (167, 199, 231), 
    16384: (204, 204, 255),    
    32768: (150, 222, 209),
}

#font
pygame.font.init()
try:
    # using Clear Sans
    FONT           = pygame.font.Font(CUSTOM_FONT, 40)
    GAME_OVER_FONT = pygame.font.Font(CUSTOM_FONT, 64)
    SCORE_FONT     = pygame.font.Font(CUSTOM_FONT, 25)
    KEY_FONT       = pygame.font.Font(CUSTOM_FONT, 16)
except FileNotFoundError:
    # fallback if font does not load
    FONT           = pygame.font.Font(None, 40)
    GAME_OVER_FONT = pygame.font.Font(None, 64)
    SCORE_FONT     = pygame.font.Font(None, 25)
    KEY_FONT       = pygame.font.Font(None, 16)

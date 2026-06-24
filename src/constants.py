import pygame

# dimensions and colors
WIDTH: int = 400
HEIGHT: int  = 500
GRID_SIZE: int = 4
CELL_SIZE: int = 100
FPS: int = 60
BACKGROUND_COLOR = (70, 30, 180)
EMPTY_CELL_COLOR = (173, 216, 230)
DARK_BLUE = (11, 11, 69)
WHITE = (255, 255, 255)

# mapping 2048 numbers to corresponding seal images (most -> least common species)
TILE_IMAGES = {
    0: EMPTY_CELL_COLOR,
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

#font
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 40, bold=True)
GAME_OVER_FONT = pygame.font.SysFont("Arial", 64, bold=True)
SCORE_FONT = pygame.font.SysFont('Arial', 25)
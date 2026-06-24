import pygame

# dimensions and colors
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 4
FPS = 60
BACKGROUND_COLOR = (70, 30, 180)
EMPTY_CELL_COLOR = (173, 216, 230)

# mapping 2048 numbers to corresponding seal images (most -> least common species)
TILE_IMAGES = {
    2: pygame.transform.scale(pygame.image.load("pics/harp_2.png"), (100, 100)),
    4: pygame.transform.scale(pygame.image.load("pics/ringed_4.png"), (100, 100)),
    8: pygame.transform.scale(pygame.image.load("pics/north_fur_8.png"), (100, 100)),
    16: pygame.transform.scale(pygame.image.load("pics/spotted_16.png"), (100, 100)),
    32: pygame.transform.scale(pygame.image.load("pics/hooded_32.png"), (100, 100)),
    64: pygame.transform.scale(pygame.image.load("pics/gray_64.png"), (100, 100)),
    128: pygame.transform.scale(pygame.image.load("pics/bearded_128.png"), (100, 100)),
    256: pygame.transform.scale(pygame.image.load("pics/harbor_256.png"), (100, 100)),
    512: pygame.transform.scale(pygame.image.load("pics/cal_512.png"), (100, 100)),
    1024: pygame.transform.scale(pygame.image.load("pics/ribbon_1024.png"), (100, 100)),
    2048: pygame.transform.scale(pygame.image.load("pics/elephant_2048.png"), (100, 100)),
    4096: pygame.transform.scale(pygame.image.load("pics/steller_4096.png"), (100, 100)),
    8192: pygame.transform.scale(pygame.image.load("pics/guadalupe_8192.png"), (100, 100)),
    16384: pygame.transform.scale(pygame.image.load("pics/med_16384.png"), (100, 100)),
    32768: pygame.transform.scale(pygame.image.load("pics/hawiian_32768.png"), (100, 100)),
}

#font
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 40, bold=True)
SCORE_FONT = pygame.font.SysFont('Arial', 25)
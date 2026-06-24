# 2 = harbor-seal; 4 = harp-seal; 8 = northern-fur-seal; 16 = spotted-seal; 
# 32 = ringed-seal; 64 = stellar-sea-lion; 128 = bearded-seal;
# 256 = hooded-seal; 512 = hawaiian-monk-seal; 1024 = guadalupe-fur-seal
# 2048 = gray-seal; 4096 = northern-elephant-seal; 8192 = mediterranean-monk-seal
# 16384 = california-seal-lion; 32768 = ribbon-seal

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
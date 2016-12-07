import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#Opening and setting the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        screen.blit(background_image, [0, 0])

        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]

        # Copy image to screen:
        screen.blit(player_image, [x, y])

        pygame.display.flip()





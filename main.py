# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # Space after colon
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a Clock object to control frame rate
    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    running = True
    while running:
        # Check for player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the game world (we'll add this later)

        # Draw the game to the screen
        screen.fill((0, 0, 0))  # Fill the screen with black color
        pygame.display.flip()   # Refresh the screen

        # Control frame rate
        dt = clock.tick(60) / 1000  # Update delta time

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()

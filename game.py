# --------------------------------------
# Title: game.py
# Purpose: Main game script for NPA Game
# Author: Sarah Herzog
# Date: 07/03/2022
# --------------------------------------


# --------------------------------------
# Import Libraries
# --------------------------------------
import pygame
# --------------------------------------


# --------------------------------------
# Initialisation and Setup
# --------------------------------------
# Initialize python so we can use it
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Set up some variables to use later in our game
running = True
# --------------------------------------


# --------------------------------------
# Game Loop
# --------------------------------------
# Run over and over until the user asks to quit
while running:
    
    # ----------------------------------
    # Input
    # ----------------------------------
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ----------------------------------

    
    # ----------------------------------
    # Update
    # ----------------------------------
    
    # ----------------------------------

    
    # ----------------------------------
    # Draw
    # ----------------------------------
    # Fill the background with a colour
    screen.fill((255, 255, 255))

    # Draw a circle
    pygame.draw.circle(screen, (0, 0, 255), (250,250), 75)

    # Flip the display
    pygame.display.flip()
    # ----------------------------------
    

# END of Game Loop
# --------------------------------------


# --------------------------------------
# Program Exit
# --------------------------------------
pygame.quit()
# --------------------------------------




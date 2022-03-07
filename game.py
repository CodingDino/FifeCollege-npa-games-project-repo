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

# Set up player
playerImg = pygame.image.load('assets/graphics/chicken.png')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 0, 0
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerRect.centerx -= 10
            if event.key == pygame.K_RIGHT:
                playerRect.centerx += 10
            if event.key == pygame.K_UP:
                playerRect.centery -= 10
            if event.key == pygame.K_DOWN:
                playerRect.centery += 10
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

    # Draw Everything
    screen.blit(playerImg, playerRect)
    

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




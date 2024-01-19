import pygame
import math
pygame.init()

"""
Setting the initial window display here

"""
WIDTH , HEIGHT = 800, 800 #in Capitals because they are constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

#we need a loop to keep the program running 

def main():
    run = True

    while run:
        for event in pygame.event.get(): #this keeps track and grabs a list of the events (clicks...) that happen in pygame
           if event.type == pygame.QUIT:
               run = False  
    pygame.quit()


main()





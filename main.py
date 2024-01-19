import pygame
import math
pygame.init()

"""
Setting the initial window display here

"""
WIDTH , HEIGHT = 800, 800 #in Capitals because they are constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
WHITE = (255, 255, 255) #r,g,b value

#we need a loop to keep the program running 

def main():
    run = True
    """
    CLock helps for the framerate of the game not going past a certain value.
    If a clock is not implemented (or some way of synchronisng the game) the simulation 
    would run at the speed of the computer.

    """
    clock = pygame.time.Clock()
    while run:
        clock.tick(60) #the loop will run a maximum of 60 times per sec

        WIN.fill(WHITE) #fills the whole screen 
        pygame.display.update() #kinda self explanatory (updates the drawings added)
        for event in pygame.event.get(): #this keeps track and grabs a list of the events (clicks...) that happen in pygame
           if event.type == pygame.QUIT:
               run = False  
    pygame.quit()


main()





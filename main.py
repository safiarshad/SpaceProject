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
YELLOW = (255, 255, 0)


class Planet:
    AU = 149.6e6 * 1000 #astronomical units and it is approx = dis of earth to sun by meter (hence the 1000x)
    G = 6.67428e-11
    SCALE = 250/AU  #scaling the orbits within the 800x800 frame pixels 1AU = 100pixels
    TIMESTEP = 3600*24 #1day of timelapse


    def __init__(self, x, y, radius, color, mass): #x & y are the positions on the screen
        self.x = x
        self.y = y 
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = [] #to keep tracks of all of the points the planet has traveled along the orbit
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win): #to draw planet
        x = self.x * self.SCALE + WIDTH / 2 #for the center cuz 00 is top left croner in pygame
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y) , self.radius)




 #we need a loop to keep the program running 
def main():
    run = True
    """
    CLock helps for the framerate of the game not going past a certain value.
    If a clock is not implemented (or some way of synchronisng the game) the simulation 
    would run at the speed of the computer.

    """
    clock = pygame.time.Clock()

    sun = Planet(0, 0 , 30, YELLOW, 1.98892 * 10**30) 
    sun.sun = True 

    planets = [sun]

    while run:
        clock.tick(60) #the loop will run a maximum of 60 times per sec

        #WIN.fill(WHITE) #fills the whole screen 
        #pygame.display.update() #kinda self explanatory (updates the drawings added)

        for event in pygame.event.get(): #this keeps track and grabs a list of the events (clicks...) that happen in pygame
           if event.type == pygame.QUIT:
               run = False  

        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()


main()





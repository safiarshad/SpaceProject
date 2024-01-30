import pygame
import math
pygame.init()

"""
Setting the initial window display here

"""
WIDTH , HEIGHT = 1000, 800 #in Capitals because they are constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255) #r,g,b value
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237) # 0,0,255 for a regular nice dark blue 
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
BLACK = (0,0,0)

FONT = pygame.font.SysFont("comicsans", 18)


class Planet:
    AU = 149.6e6 * 1000 #astronomical units and it is approx => dis of earth to sun by meter (hence the 1000x)
    G = 6.67428e-11 
    SCALE = 250 / AU  # 1AU = 100 pixels #scaling the orbits within the 800x800 frame pixels 1AU = 100pixels
    TIMESTEP = 3600*24 # 1 day


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

    def draw(self, win): 
        x = self.x * self.SCALE + WIDTH / 2 #for the center cuz 00 is top left croner in pygame
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)#False is for end point and 2 for thikness (2 px)
        

        pygame.draw.circle(win, self.color, (x, y) , self.radius)
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)} km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))



    def attraction(self, other): #other is the other planet
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x** 2 + distance_y** 2) #this is the pythagoras part

        if other.sun:
            self.distance_to_sun = distance


        force = self.G * self.mass * other.mass / distance**2 
        theta = math.atan2(distance_y, distance_x) #atan2 is the arc tan of y/x in 
    
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx / self.mass * self.TIMESTEP #  a = f/m * total 24 hours not going faster just chaning directions in time
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y +=  self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

 #we need a loop to keep the program running 
def main():
    run = True
    """
    CLock helps for the framerate of the game not going past a certain value.
    If a clock is not implemented (or some way of synchronisng the game) the simulation 
    would run at the speed of the computer.

    """
    clock = pygame.time.Clock()

    sun = Planet(0, 0 , 40, YELLOW, 1.98892 * 10**30) 
    sun.sun = True 

    earth = Planet(-1 * Planet.AU, 0, 22, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000 

    mars = Planet(-1.524 * Planet.AU, 0, 18, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 14, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 20, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60) #the loop will run a maximum of 60 times per sec
        WIN.fill((0, 0, 0))

        #WIN.fill(WHITE) #fills the whole screen 
        #pygame.display.update() #kinda self explanatory (updates the drawings added)

        for event in pygame.event.get(): #this keeps track and grabs a list of the events that happen in pygame
           if event.type == pygame.QUIT:
               run = False  

        for planet in planets:
            planet.update_position(planets)

            planet.draw(WIN) #the argument is the Window that we wanna draw on

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()




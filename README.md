# SpaceProject
Planet simulation using Python.
Please check the coding section of README file for better understanding.

"""
Mass(float): is going is to be in kgs and it will be used to calculate the attraction or gravity between the 
different planets. Which would help in generating a more precise orbit for the planets.


vel(float): Velocity in both x and y direction since the planet is moving in a circular motion 
Those Vel are determined by the force of attraction of the force of gravity between the planets.

F = Mass/Acceleration 
A = F / Mass used to find the Velocity of the planet

F = G * Mm/r**2  (r is the distance between the two objects in this case) but this formula gives us a sraight line force
it has to be broken downt to x and y components. Pythagores THeorem would be used to calculate 'r'.
{
              .
           .  . 
    F    .    . 
       .      . y and Fy(force component)
     .        .   
   .          .
. ). . . . .  .       Theta is that angle = T which will be used in the calculation
       x and Fx
}
tanT = Opp/Adj == y/x

tan**-1 (y/x) = T ==>> Value of the angel Theta 

SOH
CAH
TOA

SinT = Fy/F ==> Fy = SinT * F

CosT = Fx/F ==> Fx= CosT * F


the x and y are in meters



"""


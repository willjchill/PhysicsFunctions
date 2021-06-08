# Physics Calculations 

import math

# Lists and Functions
# This program will get a list of particles
# each of with their own point mass and x-y coordinates.
# (assume x-y coordinates are positive)

# returns gravitational net force experienced by selected object
# given all the neighboring masses as described in the objects list 
# ===> Fnet = G * (m1 * m2) / r^2 newtons
def netForce(myObject, objects):
  G = 1; # gravitational constant
  force = 0;
  for o in objects:
    r = getMagnitude(abs(myObject[1] - o[1]), abs(myObject[2] - o[2]))
    # do not consider masses in the same point
    if(r != 0):
      force += G * (myObject[0] * o[0]) / (r * r)
  return force 

# returns magnitude of 2D vector
def getMagnitude(x, y):
  mag = math.sqrt(x * x + y * y)
  return mag 

# returns time it takes for a point mass to get to ground level on Earth (y = 0m)
# ===> Assume gravitaional acceleration = g  m/s^2
#      Assume initial velocity (v0) = 0 m/s 
#      t = sqrt(2 * g * y)
def timeToFall(myObject):
  g = 9.81
  time = math.sqrt(2 * g * myObject[2])
  return time 

# UPDATE:
# Adds the freeFall function. 
# Sequencing: looks at netForce (assume object on Earth), then proceeds to change position 
# Selection: if object hits grounds, set netforce to 0 and stop object from moving
# Iteration: updates position as the object falls the ground level (y >= 0) 
# freeFall functions returns position of the object for every second it falls up until it collides with the ground
def freeFall(myObject): 
  g = 9.81 
  t = 0 
  newPosition = myObject[2] # intial position
  while(newPosition >= 0):
    newPosition = -1/2*g*t*t + myObject[2] # change position 
    if(newPosition >= 0): # check if object collides with ground 
      print("Position at (t =", t, "sec): ", newPosition)
    else:
      print("Position at (t =", t, "sec): COLLISION!")
    t += 1 # increment second 
  

# LISTING OUT THE POINT MASSES
# [mass, x, y]
objects = [[1, 0, 0], [2, 0, 100]]

# output list on console as follows: 
# object x
#   mass value
#   coordinates value (IN METERS)
print("NOTE: Position is in meters.")
i = 1
for o in objects: 
  print("Object", i, ":")
  print("\tm =", o[0])
  print("\t(%d, %d)" % (o[1], o[2]))
  i += 1  

# asks user what function it would like to call 
print("\nFunction (1): Net Force of Selected Object")
print("Function (2): Time for Selected Object to Fall on Earth")
print("NEW ALGORITHM - Function (3): Check Position of an Object Each Second of Free Fall on Earth")
print("\nType 1, 2, or 3 to choose a function.")
c = input("Input the function you would like to call: ")
if(c == '1'):
  z = input("\nSelect an object: ")
  print(netForce(objects[int(z)-1], objects), "newtons")
elif(c == '2'):
  z = input("\nSelect an object: ")
  print(timeToFall(objects[int(z)-1]), "seconds")
elif(c == '3'):
  z = input("\nSelect an object: ")
  freeFall(objects[int(z)-1]) 
else:
  print("Invalid input.")
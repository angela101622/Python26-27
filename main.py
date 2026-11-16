#Spirl of the planets

from MyFunctions import *
from random import *
turtle.tracer(0)
turtle.colormode(255)
turtle.bgcolor(20, 18, 31)

#stars
for times in range( 300 ):
  r = randint(255, 255)
  g = randint(255, 255)
  b = randint(255, 255)
  border = "white"
  fill = (r,g,b)
  x = randint(-500, 500)
  y = randint(-500, 500)
  radius = randint(1, 3)
  circle(radius, border, fill )
  jump(x,y)
  
#spiral
bob.color ("yellow")
bob.penup()
bob.goto(0,0)
bob.pendown()

r = 5
for times in range(500):
    bob.circle(r + times, 45)

#planets
for times in range( 9 ):
  r = randint(5, 255)
  g = randint(35, 255)
  b = randint(155, 255)
  border = "black"
  fill = (r,g,b)
  x = randint(-400, 500)
  y = randint(-400, 350)
  radius = randint(30, 50)
  circle(radius, border, fill )
  jump(x,y)


from turtle import *


#we want to build the house

#step one draw a square

width(7)
color("blue")

forward(200)        
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(66)
left(90)

#drawing a door
color("yellow")

forward(110)
right(90)

forward(70)
right(90)

forward(110)
left(90)

penup()
goto(200, 200)
pendown()

color("red")

left(150)
forward(120)

left(60)
forward(120)

exitonclick()
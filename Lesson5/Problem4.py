from turtle import *

Squirtle = Turtle()
screen = Screen()

Squirtle.color("blue")
Squirtle.pensize(5)
Squirtle.speed(6)
Squirtle.turtlesize(1,1,1)
Squirtle.shape("turtle")
screen.bgcolor("black")


for x in range(5):
	Squirtle.forward(50)
	Squirtle.left(144)
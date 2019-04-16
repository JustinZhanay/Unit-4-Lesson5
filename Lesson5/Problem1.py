from turtle import*
import random

Squirtle = Turtle()
Squirtle.color("Black")
Squirtle.pensize(3)
Squirtle.shape("turtle")
Squirtle.speed(2)

for x in range(3):
	Squirtle.forward(60)
	Squirtle.left(120)
mainloop()
from turtle import *

Squirtle = Turtle()
screen = Screen()

Squirtle.color("blue")
Squirtle.pensize(5)
Squirtle.speed(6)
Squirtle.turtlesize(1,1,1)
Squirtle.shape("turtle")
screen.bgcolor("red")

def row():
	def drawStar():
		for x in range(5):
			Squirtle.forward(75)
			Squirtle.left(144)

	Squirtle.penup()
	Squirtle.goto(-200,0)
	Squirtle.pendown()		
	drawStar()
		
	
	Squirtle.penup()
	Squirtle.goto(0,0)
	Squirtle.pendown()		
	drawStar()
	
	Squirtle.penup()
	Squirtle.goto(200,0)
	Squirtle.pendown()		
	drawStar()




row()

mainloop()
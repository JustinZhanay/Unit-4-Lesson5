from turtle import*

Squirtle = Turtle()
screen = Screen()

Squirtle.color("turquoise")
Squirtle.pensize(5)
Squirtle.speed(6)
Squirtle.turtlesize(1,1,1)
Squirtle.shape("turtle")
screen.bgcolor("black")


def drawHex(side):
	for x in range(6):
		Squirtle.forward(side)
		Squirtle.left(60)
drawHex(30)
drawHex(50)
drawHex(70)
drawHex(90)
drawHex(110)
drawHex(130)
drawHex(150)
drawHex(170)
drawHex(190)


mainloop()
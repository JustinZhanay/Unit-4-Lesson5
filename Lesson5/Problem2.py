from turtle import*

Squirtle = Turtle()
Squirtle.color("black")
Squirtle.pensize(3)
Squirtle.shape("turtle")

def drawTriangle():
	for x in range(3):
		Squirtle.forward(100)
		Squirtle.left(120)
def drawwheel():
	for x in range(12):
		drawTriangle()
		Squirtle.left(30)
drawwheel()
mainloop()
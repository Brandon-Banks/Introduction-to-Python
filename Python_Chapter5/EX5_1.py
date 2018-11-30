from turtle import *
t = Turtle()
screen = t.getscreen()

def main():

	x = 0

	while x<3:

		t.fillcolor("black")
		t.begin_fill()
		t.circle(20)
		t.end_fill()
		t.penup()
		t.forward(120)
		t.pendown()
		t.begin_fill()
		t.circle(20)
		t.end_fill()
		t.penup()
		t.left(90)
		t.forward(40)
		t.right(90)
		t.forward(30)
		t.right(180)
		t.pendown()
		t.fillcolor("yellow")
		t.begin_fill()
		t.forward(180)
		t.right(90)
		t.forward(30)
		t.right(90)
		t.forward(90)
		t.left(90)
		t.forward(30)
		t.right(90)
		t.forward(30)
		t.right(45)
		t.forward(43)
		t.left(45)
		t.forward(30)
		t.right(90)
		t.forward(30)
		t.end_fill()
		t.ht()
		x = x+1		

#		screen.exitonclick()

if __name__ == "__main__":
	main()
	screen.exitonclick()

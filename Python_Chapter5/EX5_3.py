import turtle

def main():

	number_of_sides = int(input("How many sides does your shape have?"))
	angles = 360 / number_of_sides

	for i in range(number_of_sides):
		turtle.forward(50)
		turtle.left(angles)

	turtle.exitonclick()

if __name__ == "__main__":
	main()

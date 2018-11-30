p = float(input("Please enter your percentage achieved in the class: "))

if p > 100:
	print("That is not a real grade.")

elif p > 93.99:
	print("You earned an A in the class.")

elif p >89.99:
	print("You earned an A- in the class.")

elif p > 86.99:
	print("You earned a B+ in the class.")

elif p > 82.99:
	print("You earned a B in the class.")

elif p > 79.99:
	print("You earned a B- in the class.")

elif p > 76.99:
        print("You earned a C+ in the class.")

elif p > 72.99:
        print("You earned a C in the class.")

elif p > 69.99:
        print("You earned a C- in the class.")

elif p > 66.99:
        print("You earned a D+ in the class.")

elif p > 62.99:
        print("You earned a D in the class.")

elif p > 59.99:
        print("You earned a D- in the class.")

else:
	print("You earned a F in the class.")


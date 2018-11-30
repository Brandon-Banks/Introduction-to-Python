#example3.10

print("This program computes your GPA.")
print("Please enter your completed courses.")
print("Terminate your entry by entering 0 credits.")

credits = 1
creditsSum = 0
gradeSum = 0
grade = 1

while credits != 0:
	creditsSum += credits
	credits = float(input("Credits?"))
	if credits != 0:
		gradeSum += grade
		grade = float(input("Grade?"))
		grade = grade*credits

GPA = gradeSum/creditsSum
print("Your GPA is", GPA)	

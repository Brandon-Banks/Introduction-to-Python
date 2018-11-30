#Phonebook

phonebook = open("addressbook.txt", "r")
numEntries = 0

print("1) Look up a person by last name")
print("2) Add a person to the address book")
print("3) Quit\n")

choice = int(input("Please enter your choice:"))

if choice == 1:
	print("Please enter the last name to look up:")
elif choice == 2:
	print("Add the information for the new contact:")
else:
	print("Goodbye!")

lastName = phonebook.readline().rstrip()
while lastName != "":
	firstName = phonebook.readline().rstrip()
	street = phonebook.readline().rstrip()
	citystatezip = phonebook.readline().rstrip()
	homephone = phonebook.readline().rstrip()
	mobilephone = phonebook.readline().rstrip()

	numEntries = numEntries + 1
	
	lastName = phonebook.readline().rstrip()

print ("You have", numEntries, "entries in your address book.")

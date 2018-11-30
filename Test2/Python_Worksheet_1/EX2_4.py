cost = float(input("How much did the item cost: "))

payment = float(input("How much did the person give you: "))

change = payment - cost

print("The person's change is $", change)

twenty = change // 20
ten = change % 20 // 10
one = change % 20 % 10 // 1
quarter = change % 20 % 10 % 1 // .25
dime = change % 20 % 10 % 1 % .25 // .10
penny = change % 20 % 10 % 1 % .25 % .10 // .01

print("The bills or the change should be: ")
print(twenty, "twenties")
print(ten, "tens")
print(one, "ones")
print(quarter, "quarters")
print(dime, "dimes")
print(penny, "pennies")

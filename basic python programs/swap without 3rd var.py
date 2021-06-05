#14.	WRITE A PROGRAM TO SWAP 2 NUMBERS WITHOUT TAKING THIRD VARIABLE.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a = a * b
b = a / b
a = a / b
print("Swapped numbers of number1 is %d & number2 is %d" %(a,b))
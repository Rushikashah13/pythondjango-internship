#12.	TAKE 3 NUMBERS AND FIND GREATEST NUMBER USING NESTED IF….ELSE STATEMENT.

num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
 greatest = num2
else:
 greatest = num3
print("The greatest number is",greatest )

#
n1 = int(input("enter n1:"))
n2 = int(input("enter n2:"))
n3 = int(input("enter n3:"))

min = (n1 if (n1 > n2 and n1 > n3) else (n2 if (n2 > n1 and n2 > n3) else n3))

# We also can use
# min=(n1>n2) and n1 or n2
# concatenating integers with string
print("Largest number among " + str(n1) +" , " + str(n2) +" and " + str(n3) +" is " + str(min))


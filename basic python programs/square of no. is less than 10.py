#10.	TAKE A NUMBER TO PRINT THE SQUARE OF A NUMBER IF IT IS LESS THAN 10.


number = float(input(" Please Enter any numeric Value : "))

square = number * number
if number<=10:
    print("The Square of a Given Number {0}  = {1}".format(number, square))
else:
    print("number is grater than 10")
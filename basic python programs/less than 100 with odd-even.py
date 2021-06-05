#9.	TAKE A NUMBER CHECK IF A NUMBER IS LESS THAN 100 OR NOT. IF IT IS LESS THAN 100 THEN CHECK IF IT IS ODD OR EVEN.


for num in range(0,100):
    num = int(input("Enter a number: "))
    print(num,"is less than 100")
    break
if (num % 2) == 0:
        print("{0} is Even".format(num))
else:
        print("{0} is Odd".format(num))

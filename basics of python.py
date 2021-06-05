print("Hello, World!")

#variables
x = 5
y = "John"
print(x)
print(y)

x1 = 4
x1= "Sally" # value of x changes
print(x1)

#type of variable
x2= 5
y2 = "John"
print(type(x2))
print(type(y2))

x4 = 1    # int
y4= 2.8  # float
z4= 1j   # complex
print(type(x4))
print(type(y4))
print(type(z4))


#assigning multiple values
x3, y3, z3 = "Orange", "Banana", "Cherry"
print(x3)
print(y3)
print(z3)

#concatenation
x5 = "awesome"
print("Python is " + x5)

#slicing string
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])

#lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

#dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))





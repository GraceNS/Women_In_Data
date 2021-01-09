x = int(input("Choose a number: "))
y = int(input("Choose another number: "))

operator = input("Enter 'a' to add the values, 'b' to subtract, 'c' to multiply, 'd' to divide, or 'e' to make your second number an index. ")

if operator == "a":
    print(x+y)
if operator == "b":
    print(x-y)
if operator == "c":
    print(x*y)
if operator == "d":
    print(x/y)
if operator == "e":
    print(x**y)
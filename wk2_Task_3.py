def multiply(a,b):
    print(a*b)

def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def divide(a,b):
    print(a/b)

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
operator = input("Choose 1 to add, 2 to subtract, 3 to multiply or 4 to divide. ")
if operator == "1":
    add(x,y)
elif operator == "2":
    subtract(x,y)
elif operator == "3":
    multiply(x,y)
elif operator == "4":
    divide(x,y)
else:
    print("I don't understand.")
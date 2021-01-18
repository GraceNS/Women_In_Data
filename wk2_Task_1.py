def order():
    choice = input("What would you like to order? ")
    meal = input("Is that a meal? ")
    if meal == "yes":
        choice = choice + " + fries + drink"
    
    return "You have ordered " + choice + "."

print("Welcome.")
ordermsg = order()
print(ordermsg)
extra = input("Is that everything? ")
if extra == "yes":
    print("Thank you!")
elif extra == "no":
    order2 = order()
    print(order2)
else:
    print("I'm sorry, I didn't get that.")
    
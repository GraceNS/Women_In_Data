num = int(input("Pick a number between 1-100: "))

if num < 13:
    print("I got into a fight with 1, 3, 5, 7 and 9... the odds were against me.")
elif num == 13:
    print("The number 13? Not on my watch.")
elif num > 13 and num<40:
    print("How do you turn the roman numeral IX (9) into a six? Add the S.")
elif num >= 40 and num<65:
    print("Why was 4 not impressed when 5 won a prize for 6? Because 511472.")
else:
    print("You know what's odd? Every other number.")
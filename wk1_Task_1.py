import random

name = input("Please enter your name: ")

number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congrats, " + name + ", you guessed correctly!")
else:
    print("Unlucky, the number was " + str(number) + ".")
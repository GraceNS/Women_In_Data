my_file = open("numbers.txt", "w")
my_file.write("3, 45, 83, 21")
my_file.close()

with open("numbers.txt", "r") as my_file:
    data = my_file.read().replace("3", "2")
my_file.close()

print(data)

my_file = open("numbers.txt", "a")
my_file.write(", 52, 73")
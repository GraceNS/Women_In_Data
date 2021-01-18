value = 2000

def depreciate(value):
    print("Current value is £", value)

while value>1000:   
    depreciate(value)
    value = 0.9*value
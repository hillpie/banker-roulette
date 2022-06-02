import random
name_string = input("Give everbody's name, seperated by a comma.")
names = name_string.split(", ")
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
payee = names[random_choice]
print (payee + " is going to buy the meal today.")
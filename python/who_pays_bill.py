import random
names_list = input("Type all the names here, separated by a comma.")
names = names_list.split(", ")
name_length = len(names)
random_name = random.randint(0, name_length - 1)
person = names[random_name]
print(person + " is going to pay bill.")
# print
print("Hi Jitu! Welcome to Python World")

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print()

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

for i in range(5):
    print(i)

#String
String1 = "TeamIndia"
print(String1)
print(String1[2:7])
print(String1[3:-2])

# String Formatting
String1 = "{} {} {}".format('Physics', 'Math', 'Chemistry')
print(String1)

#positional formatting
String1 = "{1} {0} {2}".format('Physics', 'Math', 'Chemistry')
print(String1)

# Keyword Formatting
String1 = "{p} {c} {m}".format(p='Physics', m='Math', c='Chemistry')
print(String1)

# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1) 

# List
a = [11, 21, 13, 4, 54, 36]
for items in sorted(a):
    print(items)

for index, value in enumerate(a):
    print(str(index) + " = " + str(value))

names = ['Tanu', 'Jitu', 'Pooja']
hobbies = ['Dance', 'Cricket', 'Studying']
ages = [27, 28, 25]

for person, age, hobby in zip(names, ages, hobbies):
    print(person + " is " + str(age) + "  years old and his/her hobby is " + hobby)

b = ["hello", "python", "world"]
b.extend(["hi", "java"])
print(b)
print(len(b))

c = ["hey", "you", 1, 2, 3, "go"]
print(c)

# Tuple
a = (1, 2, 3, 4)
print(a)

b = ("hello", 1, 2, 3, "go")
print(b)

# concatenation
c = a + b
print(c)

words = ["jitu", "tanu", "kittu", "sonu", "puja"]

for word in words:
    if word == "sonu":
        break;
    print(word)

# Dictionary
a = {1: "jitu", 2: "tanu"}
a['cricketers'] = 'msd', 'virat', 'bumrah'
print(a)

b = {'a': 10, 'b': 8}
b.update(a)
print(b)

dict = [{'a': 1}, {'b': 2}, {'c': 3}]

# code to flatten list of dictionary
out = {k: v for d in dict for k, v in d.items()}
print("flatten dictionary", str(out))

# Set
set = set()
set.add(1)
set.add((2, 3, 4, 5, 1))

print(set)

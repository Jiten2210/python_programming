# print
print("Hi Jitu! Welcome to Python World")

players = 15
players_can_play = 11
print("There are", players, "players available.")
print("Only", players_can_play, "players can play.")

print("There are %d types of people." % 10)
binary = "binary"
do_not = "don't"
print("Those who know %s and those who %s." % (binary, do_not))


#loop
for i in range(5):
    print(i)

listOne = [123, 345, 456, 23]
print("Using enumerate")
for index, element in enumerate(listOne):
    print("Index [", index,"]", "Value", element)


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

listNumbers = [20, 22, 24, 26, 28, 28, 20, 30, 24]
print("Original= ", listNumbers)

listNumbers = list(set(listNumbers))
print("After removing duplicate= ", listNumbers)

set1 = set(['Scott', 'Eric', 'Kelly', 'Emma', 'Smith'])
set2 = set(['Scott', 'Eric', 'Kelly'])

list3 = list(set1.symmetric_difference(set2))
print(list3)

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

# reverse a list
aList = [10, 20, 30, 40, 50]
aList = aList[::-1]
print(aList)

# palindrome check
x = "madam"
print(x == x[::-1])

# set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))

# Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ji"]
list2 = ["y", "me", "s", "tu"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

# square of each elements
list4 = [1, 2, 3, 4, 5, 6, 7]
list4 = [x * x for x in list4]
print(list4)

# find and replace element a list
list5 = [1, 2, 3, 11, 5]
index = list5.index(11)
list5[index] = 4
print(list5)

# lowercase letter first

inputStr = "PyThoN"
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print(sortedString)

# string count

input = "gaya went gaya"
target = "gaya"
temp = input.lower()
count = temp.count(target.lower())
print("gaya occured", count, "times")

# count occurence of all character

input1 = "indiaisagreatnation"
dict = dict()
for char in input1:
    count = input1.count(char)
    dict[char] = count
print(dict)

#  Access the value of key ‘history’
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

# Create new dictionary with given key

inputDict = {
    "name": "MSD",
    "age": 39,
    "city": "Ranchi"}

keys = ["name", "city"]

newDict = {k: inputDict[k] for k in keys}
print(newDict)

# swap numbers

x = 10
y = 20
x, y = y, x
print(x)
print(y)

# check it all elements are same

tuple1 = (1, 1, 1, 1)
print(all(i == tuple1[0] for i in tuple1))


# variable arguments

def func(*args):
    for i in args:
        print(i)


func(20, 40, 60)
func(80, 100)


# default param
def getEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)


getEmployee("X", 80000)
getEmployee("Y")

# even numbers between 1 and 20

print(list(range(0, 20, 2)))

# sort words alphabetically

str = "India is a great nation"
words = str.split()

words.sort()
for word in words:
    print(word)

# count number of vowels
# method 1
vowels = 'aeiou'
str = str.casefold()
count = {}.fromkeys(vowels, 0)

for c in str:
    if c in count:
        count[c] += 1
print(count)

# method 2
print({x: sum([1 for char in str if char == x]) for x in vowels})


# factorial

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


print(factorial(5))


# fibonacci

def fibonacci(n):
    a = 0
    b = 1
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(7))

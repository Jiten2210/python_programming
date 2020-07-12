# reverse a list
list = [10, 20, 30, 40, 50]
list = list[::-1]
print(list)

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

#lowercase letter first

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
  dict[char]=count
print(dict)

#  Access the value of key ‘history’
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict['class']['student']['marks']['history'])

# Create new dictionary with given key

inputDict = {
  "name": "MSD",
  "age":39,
  "city": "Ranchi" }

keys = ["name", "city"]

newDict = {k: inputDict[k] for k in keys}
print(newDict)

# swap numbers

x=10
y=20
x,y = y,x
print(x)
print(y)



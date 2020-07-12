from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

print("is two list are b equal", Counter(one) == Counter(two))
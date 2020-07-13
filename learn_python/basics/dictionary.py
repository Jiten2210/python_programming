import collections
from collections import OrderedDict

print("Dictionary:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for k, v in d.items():
    print(k, v)

print("\n Ordered Dictionary:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for k, v in od.items():
    print(k, v)

od.pop('c')
for k, v in od.items():
    print(k, v)

print("\nAfter re-inserting:\n")
od['c'] = 3
for k, v in od.items():
    print(k, v)

# initializing dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap using maps
print(chain.maps)

# printing keys using keys()
print(list(chain.keys()))

# printing keys using keys()
print(list(chain.values()))

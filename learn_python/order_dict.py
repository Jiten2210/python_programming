from  collections import OrderedDict

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
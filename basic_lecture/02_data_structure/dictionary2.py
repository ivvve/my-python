d = {'x': 10, 'y': 20}

print(d.keys())
print(d.values())

##

d2 = {'x': 1000, 'z': 500}
print(d2)


d.update(d2) # d2로 덮어써라
print('d', d)
print('d2', d2)

print(d.get('z'))
print(d.get('a'))
print(type(d.get('a')))

print(d.pop('x'), d)
del d['y']
print(d)
d.clear()
print(d)
print('a' in d)
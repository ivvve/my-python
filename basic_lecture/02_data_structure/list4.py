i = [1, 2, 3, 4, 5]
j = i
print(id(i))
print(id(j)) # 같다

print('i = ', i)
print('j = ', j)

j[0] = 100

print('i = ', i)
print('j = ', j)

##

i = [1, 2, 3, 4, 5]
j = i.copy()
# j = i[:]
print(id(i))
print(id(j)) # 다르다

j[0] = 100

print('i = ', i)
print('j = ', j)

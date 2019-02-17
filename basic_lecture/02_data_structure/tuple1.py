t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))

print(t[0])
print(t[-1])
print(t[2:5])

print(t.index(2, 2))

##

# t[0] = 3 # 값을 변경할 수 없다.

t = ([1, 2, 3], [4, 5, 6])
# t[0] = [10, 11, 12]
t[0][0] = 2
print(t)
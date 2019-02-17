num_tuple = (10, 20)
print(num_tuple)

# unpacking
x, y = num_tuple
print(x, y)
a, b = (10, 20)
a, b = 10, 20 # 자동으로 튜플로 인식
print(a, b)

##

i = 10
j = 20
temp = i
i = j
j = temp
print(i, j)

i = 10
j = 20
i, j = j, i
print(i, j)


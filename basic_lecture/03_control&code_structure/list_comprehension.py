t = (1, 2, 3, 4, 5)

r = []
for i in t:
    r.append(i)
print(r)

print('##########')

r = [i for i in t]
r = [i for i in t if i % 2 == 0]
print(r)

print('##########')

t1 = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)
r = []

for i in t1:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t1 for j in t2]
print(r)
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)

s[0] = 'X'
print(s)
s[2:5] = ['Q', 'W', 'E']
print(s)
s[2:5] = [] # 해당 elements 지우기
print(s)
s[:] = [] # 전부 지우기
print(s)

##

n =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n)
n.insert(0, -1)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
del n[0]
print(n)
n.remove(2) # index가 아닌 해당 element를 삭제한다.
print(n)
# n.remove(2) # 없는데 없애려고 하면 error가 뜸

##

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = a + b
print(c)
a += b
print(a)

c.sort()
print(c)

x = [1,2,3]
y = [4,5,6]
z = x.extend(y)
print(z)
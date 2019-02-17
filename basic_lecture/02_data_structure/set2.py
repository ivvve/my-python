s = {1, 2, 3, 4, 5}

# print(s[0]) # 집합엔 순서가 없다
s.add(6)
print(s)
s.add(6)
print(s)

s.remove(6)
print(s)
# s.remove(6) # error

s.clear()
print(s) # set임을 알려주기 위해 set()이 나온다.

print(help(set))

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 5)) # 2를 5번째 인덱스 부터 검색

print(r.count(3))

if 5 in r:
    print('exists')

##

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse() # 현재의 역순으로 정렬
print(r)

##

s = 'My name is Chris'
to_split = s.rsplit(' ')
print(to_split)

x = '####'.join(to_split)
print(x)


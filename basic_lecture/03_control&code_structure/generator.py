# 반복처리를 할 때 하나를 꺼내 생성하는 역할
l = ['Hello', 'Bye', 'See you']

for i in l:
    print(i)

print('##############')

def greeting():
    yield 'Hello'
    yield 'Bye'
    yield 'See you'

g = greeting()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

print('###############')

def counter(num=10):
    for i in range(1, num + 1):
        yield i

c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print('#############')

# 다음 yield를 위해 중간 처리가 필요한 작업
def greeting():
    yield 'Hello'
    for _ in range(10):
        print(' ')
    yield 'Bye'
    for _ in range(10):
        print(' ')
    yield 'See you'

g = greeting()
print(next(g))
print(next(g))
print(next(g))

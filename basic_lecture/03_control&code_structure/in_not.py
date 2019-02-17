y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

if not a == b:
    print('not equal')
# 하지만 != 를 더 추천
# 숫자에는 not 쓰는걸 추천하지 않는다.

##

# False, 0, 0.0, '', [], (), {}, set()

# is_ok = True
is_ok = 'hello' # True
is_ok = [] # False

# 이런식으로 not을 쓴다.
if not is_ok:
    print('hello')
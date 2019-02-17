# print(help((None)))
is_empty = None

# 파이썬에서는 None을 판별할 때는 ==, != 가 아닌
# is, is not 을 사용한다.
if is_empty is None:
    print("hello")
else:
    print("world")

##
print(1 == True) # 값 비교
print(1 is True) # object 끼리 비교

l = [1, 2]
l2 = [1, 2]

print(l == l2) # True
print(l is l2) # False



num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

##

num = name
print(num, type(num))

num = 1
str = '1'

print(int(str), type(int(str)))

##

# 3 버전부터 형 선언을 할 수 있다. (주로 사용하지 않는다)
num: int = 1
name: str = '1'
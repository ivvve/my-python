def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')
print(r)

# 함수를 실행 전, 후에 어떤 기능을 추가하고 싶을 경우
# => decorator!

print('##')

def print_info(func):

    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper

f = print_info(add_num)
print(f(10, 20))

print('##')

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

print('##')

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_info
@print_more # decorator 순서 확인!
def add_num(a, b):
    return a + b

# f = print_info(print_more(add_num()))
r = add_num(10, 20)
print(r)
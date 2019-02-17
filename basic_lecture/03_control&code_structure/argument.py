# default argument
def menu(entree='pork', drink='wine', dessert='cake'):
    print(entree)
    print(drink)
    print(dessert)

menu(drink='coke')

print('##')

def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(y)

r = test_func(100)
print(r)
r = test_func(100)
print(r) # bug가 될 가능성이 높다.

# list는 default로 사용해선 안된다.
# default list를 그때 그때 만드는게 아니라
# 하나 만들어놓고 그걸 계속 사용한다.

# 그때 그때 새로 생성하고 싶다면 아래처럼 None을 default로 지정
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)
r = test_func(100)
print(r)

print('##')

def say(word, *args): # 파라미터들을 tuple에 담아준다
    print('word :', word)
    for i in args:
        print(i)

say('Hello', 'my', 'name', 'pyson')

t = ('devson', 'pyson')
say('Hi', *t);

print('##')

def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='port')

def menu(**kwargs): # keyword args : dictionary 형으로 받는다.
    print(kwargs)

menu(entree='port')

d = {
    'entree': 'beef',
    'drink': 'iced coffee',
    'dessert': 'ice'
}

menu(**d)

print('##')

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', *('hello', 'world'), **{'key': 'k', 'value': 'v'})
menu('banana', 'hello', 'world', key='k', value='v')

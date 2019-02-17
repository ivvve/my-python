# def: define
def say_hi():
    print('hi')

# hoisting이 없어 정의 전에 함수사용을 할 수 없다
say_hi()
print(type(say_hi()))

##

def say_hi():
    return 'hi'

result = say_hi()
print(result)

##

def greeting(name):
    print('hello', name)

greeting('devson')

##

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'tomato':
        return 'green pepper'
    else:
        return "I don't know"

print(what_is_this('red'))
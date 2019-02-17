animal = 'cat'

def f():
    global animal
    animal = 'dog'
    print('local:', animal)
    print('locals:', locals())

f()
print(animal)
print('global:', globals())
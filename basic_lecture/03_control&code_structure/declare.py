num: int = 10

def add_num(a: int, b: int) -> int:
    return a + b

add_num('e', 'n') # 에러는 나지 않는다.

##

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

# 이렇게 하면 순서에 까다롭게된다.
# menu('beef', 'beer', 'ice')

menu(entree='beef', dessert='ice', drink='beer')

# 이렇게 되면 ice가 어디로 들어가야하는지 판단을 할 수 없어 에러가 난다.
# menu(entree='beef', 'ice', drink='beer')



# 공통점을 찾고 싶을 때 사용할 수 있다
my_friends = {'KIM', 'JASON', 'AMY'}
his_friends = {'BRIAN', 'KIM', 'CHRIS'}
print(my_friends & his_friends)

# 리스트에서 유니크한 값을 찾을 때도 사용
cart = ['apple', 'banana', 'apple', 'banana']
kind = set(cart)
print(kind)
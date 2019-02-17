def outer(a, b):

    def inner():
        return a + b

    return inner

inner = outer(1, 2)
print(type(inner))
print(inner)
print(inner()) # 1, 2(a, b)는 살아있다.

print('##')

def circle_area_func(pi):

    def circle_area(radius):
        return pi * (radius ** 2)

    return circle_area


ca1 = circle_area_func(3.14) # rough한 원넓이
ca2 = circle_area_func(3.141592) # detail한 원넓이

print(ca1(10))
print(ca2(10))

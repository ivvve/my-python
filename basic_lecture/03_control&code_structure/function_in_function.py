# 함수내에서만 쓰는 함수를 정의할 때 아래와 같이 쓸 수 있다.
def outer(a, b):

    def plus(c, d):
        return a + b

    print(plus(a, b))

outer(1, 2)
# function은 설명을 안에다 적는다.
def func(param1, param2):
    """
    Example Function
    :param param1:
    :param param2:
    :return:
    """
    print(param1)
    print(param2)
    return True

# docstring 출력
help(func)
print(func.__doc__)
# Vasya - Clerk


def tickets(people):
    total = 0

    for money in people:
        if money == 25:
            total += money
        else:
            total -= (money - 25)

        if (total < 0):
            return "NO"

    return "YES"

# 348597 => [7,9,5,8,4,3]

def digitize(n):
    reversed_list = []
    while n > 0:
        reversed_list.append(n % 10)
        n //= 10

    return reversed_list

### better solution

def digitize(n):
    return map(int, str(n)[::-1])
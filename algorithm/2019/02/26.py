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

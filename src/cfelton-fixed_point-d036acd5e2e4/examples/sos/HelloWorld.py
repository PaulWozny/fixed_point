from fixed_point import fixed

def addfixed(x, y):
    a = fixed(x)
    b = fixed(y)

    c = a + b

    return c

print(addfixed(2, 22))



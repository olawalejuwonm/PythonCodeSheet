def product(a: list):
    result = 0
    for indx, t in enumerate(a):
        if indx > 0:
            result *= t
        else:
            result += t
    return result
print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10]))
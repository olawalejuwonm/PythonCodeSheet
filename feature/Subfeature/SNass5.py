def factors(a: int):
    result = []
    b = a + 1
    for t in range(1,b,1):
        if a%t == 0:
            result.append(t)
        else:
            continue
    return result
print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))
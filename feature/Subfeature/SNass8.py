def factorial(a: int):
    if a == 0:
        return a + 1
    return a * factorial(a - 1)
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5)) 

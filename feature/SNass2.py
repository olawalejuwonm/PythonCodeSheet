def destroy_element(a: list, b: list):
    final = [t for t in a if t not in b]
    return final
print(destroy_element([1, 2, 3], [1, 2]))
print(destroy_element([1, 2, 3], [1, 2, 3]))
print(destroy_element([1, 2, 3], [4, 5]))
def same_index_values(a: list, b: list):
    result = []
    for indx, t in enumerate(a):
        if t in b:
            mic = b.index(t)
            if indx == mic:
                result.append(indx)
            else:
                continue
        else:
            continue
    return result
print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))
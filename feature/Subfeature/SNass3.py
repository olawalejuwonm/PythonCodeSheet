def cleanup(a: list):
    result = []
    useless = []
    for indx, t in enumerate(a):
        if a[indx].isspace() == False and a[indx] != "":
            result.append(t)
        else:
            continue
    final = ", ".join(result).replace(", ", " ")
    return final
print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))
print(len(cleanup(["", "", " "])))
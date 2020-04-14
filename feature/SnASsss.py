def vowel_count(a: str):
    result = 0
    if "a" in a:
        for t in a:
            if t == "a":
                result += 1
            continue
    if "e" in a:
        for t in a:
            if t == "e":
                result += 1
    if "i" in a:
        for t in a:
            if t == "i":
                result += 1
    if "o" in a:
        for t in a:
            if t == "o":
                result += 1
    if "u" in a:
        for t in a:
            if t == "u":
                result += 1
    return result
print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("ssh"))
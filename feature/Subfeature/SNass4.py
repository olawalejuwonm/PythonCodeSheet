def encrypt_message(a: str):
    result = ""
    alphabet = ["a", "b", "c", "d", "e", "f","g",
    "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for indx, t in enumerate(a):
        if t in alphabet:
            mic = alphabet.index(t)
            index = mic - 24
            result += alphabet[index]  
        else:
            break
    return result
print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))


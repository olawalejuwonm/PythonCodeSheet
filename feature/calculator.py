creator = "Micheal"
calculator = "Mic"
PI = 3.14159
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def area(radius):
    return PI * radius * radius


# print(add(3, 4))
# print(__name__)
if __name__ == "__main__":
    print("This will run when calculator is being runned as a script")
    print(subtract(3, 5))
else:
    print("You are running another file in your script")
_year = 2020 #the _ before year tells python
#not to export the variable
print(calculator)
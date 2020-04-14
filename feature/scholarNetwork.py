# def output_text():
#     print("Welcome")
# output_text()
# def p(text):
#     print(text)
# p("Hello")
# def add(a, b, c):
#     print(a + b)
# add(3, 5)
# add(a = 4, b = 6)
# add(b = 3, a = 2)
# add(5, c = 5, b = 10)
# def add(a, b):
#     return a + b
#     print("This wont run")
# result = add(3, 5)
# print(result)
# a = None
# print(type(a))
# def subtract(a, b):
#     print(a)
# print(subtract(5, 3))
# def ggg(word: str, times: int) -> str: #just for documentation
#      return word * times
# print(ggg("dog", 5))
# print (ggg(10, 5))
# print(len("python<ld"))
# # print(len(3.14))
# print("Boris " + " Micheal")
# print("a" "b" "c")
# print("-----" * 30)
# lang = "Python"
# print(lang[0])
# print(type(lang))
# lang[2] = "B"
# print(len(lang))
# print(lang[100])
# topic = "programming"
# print(topic[-1])
# address = "FAAGDGDJD Street, Beverly Hills, CA 90210"
# print(address[0:3])
# print(address[9:32100])
# print("\n")
# print(address[1:-8])
# print("\n")
# print(address[2:])
# print(address[:])
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print(alphabet[0:10:2]) #0246
# print(alphabet[0:26:3])
# print(alphabet[::-1])
# print("This will \nprint on a \nnew line and \tindent")
# print("\'To be or not to be\'")
# print("Lets this be a blackslah\\")
# file_name = r"C:\news\travel"
# print(file_name)

# aaaaaaaaaaaaaaaaaaaaaaaaaaa = 2
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb = 3
# ccccccccccccccccccccc = 4
# final = aaaaaaaaaaaaaaaaaaaaaaaaaaa +\
#     bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb +\
#         ccccccccccccccccccccc
# print(final)
# print(aaaaaaaaaaaaaaaaaaaaaaaaaaa, 
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb,
# ccccccccccccccccccccc)
# announce = "the winners of the prize is Boris, andy, and adam"
# print("Boris" in announce)
# print("ste" in announce)
# print("ste" not in announce)
# browser ="Google Chrome"
# print(browser.find("C"))
# print(browser.find("Ch"))
# print(browser.find("o"))
# print(browser.find("z"))
# print(browser.find("c"))
# print(browser.find("o", 3))
# print(browser.index("C"))
# print(browser.index("z"))
# salutation = "Mr. Kermit the Frog"
# print(salutation.startswith("M"))
# print(salutation.startswith("m"))
# print(salutation.startswith("M"))
# print(salutation.startswith("Ker"))
# print(salutation.startswith("Ms"))

# print()

# print(salutation.endswith("og"))
# module 12
# word = "queueing"
# print(word.count("e"))
# print(word.count("q"))
# print(word.count("ing"))
# def product(a,b):
#     return a*b
# product(a = 5)
# print("motorbreath"[-6:])
# print("mendacious"[:10:4])
# print("genuflect"[::-1])
# "commando"[3:7]
# "misfortune"[9]
# story = "once upon a time"

# print(story.capitalize())
# print(story.title())
# print(story.upper())
# print("Hello".lower)
# print("AbCdE".swapcase())
# print("BENJAMIN FRANKLIN".lower().title())
# story = story.title()
# print(story)
# print("winter".islower())
# print("Winter".islower())
# print("SUMMER".isupper())

# print("The Four Seasons".istitle())
# print("The Four Seasons".isalpha())
# print("TheFourSeasons".isalpha())
# print("34".isnumeric())
# print("Area51".isalnum())
# print("Area 51".isalnum())
# print(" ".isspace())
# print(" k ".isspace())

# empty_space = "              content               "
# print(empty_space.rstrip())
# print(empty_space.)
# print(len(empty_space.rstrip()))

# print(empty_space.lstrip())
# print(len(empty_space.lstrip()))

# print(empty_space.strip())
# print(len(empty_space.strip()))
# website = "www.python.org"

# print(website.strip("w"))
# print(website.strip("org"))
# print(website.strip("worg."))

# phone_number = "5555 222222 3333 5333"
# print(phone_number.replace(" ", "-"))
# print(phone_number.replace("5", "g"))
# phone_number = phone_number.replace(" ", "-")
# mad_libs = "{} laughed at the {} {}."
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Bobby", "green", "alien","gsdhsg","shdfh"))
# mad_libs = "{0} laughed at the {2} {1}."
# print(mad_libs.format("Bobby", "green", "alien"))
# mad_libs = "{c} laughed at the {d} {a}."
# c = input("name")
# d = input("yeah:")
# a = input("noun:")
# # print(mad_libs.format(c = c, d = d, a = a))
# mad_libs = f"{c} laughed at the {d} {a}."
# print(mad_libs.format(c, d, a))
# handsome = True
# admin =False
# if 5 > 3:
#     print("Yup")
# if 3:
#     print("Hello")
# if 0:
#     print("Hell")
# if -1:
#     print("Will this print")
# if "hello":
#     print("yea")
# if "":
#     print("ok")
# print(bool(1))
# print(bool(0.0))
# print(bool(""))
# print(bool("alpha"))
# print(bool(" "))
# if 10 > 15:
#     print("That is true")
# else:
#     print("yeap")
# def asd(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     elif number == 0:
#         return "Neither! Its zero"
# print(asd(3))
# print(asd(-3))

# def calculator(operation,a,b):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         return a - b
#     else:
#         return "I dont know"
# print(calculator("add",3,2))
# print(calculator("adad",3,2))
# zip_code= "90323"

# if len(zip_code) == 5:
#     check = "Valid"
# else:
#     check = "Invalid"

# check ="Valid" if len(zip_code) == 5 else "Invalid"
# print(check)
# if True and True:
#     print("True")
# if "cat" == "cat" or "dog" == "donkey":
#     print("ok")
# print(not True)
# print(not False)
# if "H" in "Hello":
#     print("That dosent")
# if "H" not in "Hello":
#     print("That dosent")
# ing1 = "Oat"
# ing2= "meat"
# if ing1 == "Oat":
#     if ing2 == "meat":
#        print("I recommend making Oat and meat")
# else:
#     print("i have no recommendation")
# count = 0
# while count <= 5:
#     print(count)
#     count += 1
# print (count)
# invalid_number = True
# while invalid_number:
#     user_value = int(input("please enter number above 10:"))
#     if user_value > 10:
#         print(f"yup, {user_value} it is greater than 10")
#         break
#     else:
#         print("no")
# Recursion is when a function call itself
# def count_down_from(number):
#     start = number
#     while start > 0:
#         print(start)
#         start -=1 #start = start - 1
#     count_down_from(5)
# def count_down_from(number):
#     if number <= 0:
#         return 
#     print(number)
#     count_down_from(number - 1)
# count_down_from(5)
# def reverse(str):
#     a = len(str)
#     return str[:::]

# print(reverse("straw")) #warts
# I Love Thid
# def reverse(str):
#     a = 0
#     b = len(str) - 1
#     c = ""

#     while b >= a:
#         c += str[b]
#         b -= 1
#     return c
       
# def reverse(str):
#     if len(str) <= 1:
#         return str
#     return str[-1] + reverse(str[:-1])
# print(reverse("straw"))
# this is how the code runs
#straw
# w + reverse(stra)
# w + a + reverse(str)......

# print("straw"[-1])
# print("straw"[:-1])

# print("man".rfind("m"))
# print("mAn".swapcase())
# print("      man    ".strip())
# phone_number = "5555 222222 3333 5333"
# print(phone_number.replace(" ", "-"))
# print(" 11".isnumeric())
# ape = 5
# while ape>0:
#     print(ape)
#     ape -=1
# 5 > 3 and 6>3

#module 9
#list is an array
# empty = []
# empty = list() #each object in a list is called an element

# sodas = ["Coke", "Pepsi", 
# "Dr.Pepper"]
# print(len(sodas))
# quarterly_revenues = [15000, 12000, 9000, 20000]
# meals = ["breakfast", "lunch", "dinner"]
# print("lunch" in meals)
# print("Dinners" in meals) #case sensitive
# print("dinner" not in meals)
# if "rice" not in meals:
#     print("rice is not there")
# web_browsers = ["chrome", "firefox", "safari"]
# print(web_browsers[1])
# #print(web_browsers[10])
# element_index = web_browsers[2]
# print(element_index[3])
# print(web_browsers[2][3])
# print(web_browsers[-1])
# print("programming"[3:6])
# muscles = ["Biceps", "triceps", "Deltoid", "Sartorius"]
# print(muscles[1:3])
# print(muscles[2:])
# print(muscles[2:1000])
# print(muscles[-4:-2])
# print(muscles[::-1])
# print(muscles[::-2])
#module 10
# dinner = "Streak and Potatoes"
# for character in dinner:
#     print(character)
# numbers = [2, 3, 5, 7, 10]

# for aaa in numbers:
#     print(aaa * aaa)
# novelists = ["Fitzgerald", "Hemingway", "Steinbeck"]

# for novelist in novelists:
#     print(len(novelist))
# print(novelist)
# print(aaa)
# total = 0
# for number in numbers:
#     total = total + number
# print(total)
# values = [3, 6, 9, 12, 15, 18, 21, 24]
# other_values = [5, 10, 15, 20, 25, 30]
# def odds_sum(numbers):
#     total = 0
#     for number in numbers:
#         if number % 2 == 1:
#             total += number
#     return total



# print(odds_sum(values))
# print(odds_sum(other_values))
# def greatest_number(numbers):
#     greatest = numbers[0]
#     for num in numbers:
#         if num > greatest:
#             greatest = num
#     return greatest

# print(greatest_number([1,2,3]))
# print(greatest_number([3,2,1]))
# print(greatest_number([4,5,5]))
# print(greatest_number([-3,-2,-1]))
# print(greatest_number(values))
# the_simpsons = ["Home", "merge", "Bart", "Lisa", "Maggie"]
# for character in the_simpsons[::-1]:
#     print(f"{character} has a total {len(character)} of characters")
# print(reversed(the_simpsons))
# print(type(reversed(the_simpsons)))

# for character in reversed(the_simpsons):
#     print(f"{character} has a total {len(character)} of characters")
# errands = ["Go to gym", "Grab lunch", "Get promoted at work", "sleep"]

# print(enumerate(errands))
# print(type(enumerate(errands)))

# for index, errand in enumerate(errands):
#     print(f"{errand} is number {index + 1} on my list")
# for a, b in enumerate(errands, 1): # (errands, index)
#     print(f"{b} is number {a} on my list")
# print(range(5))
# for number in range(5):
#     print (number)
# for number in range(0, 5):
#     print (number)
# print(range(0,5))
# for number in range(10, 101, 10):
#     print (number)
# for number in range(99, -1, -11):
    # print (number)
#range is use for collection of numbers in sequence
# print(3 in [1,2,3,4,5])
# def contains(values, target):
#     found = False

#     for value in values:
#         if value == target:
#             found = True
#             break
#     return found
# print(contains([1,2,3,4,5],3))
# def sum_of_positive_numbers(values):
#     total = 0
#     for value in values:
#         if value > 0:
#             total += value

#     return total


# def sum_of_positive_numbers(values):
#     total = 0

#     for value in values:
#         if value < 0:
#             continue
#         total += value   
#     return total
# print(sum_of_positive_numbers([1, 2, -3, 4]))
# import sys 


# print(sys.argv)
# print(type(sys.argv))

# word_lengths = 0
# for arg in sys.argv[1:]:
#     word_lengths  += len(arg)

# print(f"The total length of all command line argument is {word_lengths}")

# module 11
# crayons = ["Macaroni and cheese", "Maximum Yellow Red", "Jazzberry Jan"]
# print(crayons)
# crayons[1]="Cotton Candy"
# print(crayons)
# crayons[-1] = "Aquamarine"
# print(crayons)
#crayons[3] = "Aztec Gold"
# coworkers = ["Micheal", "Jim", "Dwight", "Pam", "Creed", "Angela"]
# # coworkers[3:5] = ["Oscar", "Ryan"]
# # print(coworkers)
# #coworkers[3:5] = "Oscarr"
# print(coworkers)
# coworkers[3:5] = ["Oscar"]
# print(coworkers)
# coworkers[-3:5] =["mic"]
# print(coworkers)
# countries = ["USA", "Australia", "canada"]
# print(len(countries))
# countries.append("Japan")
# print(countries)
# print(len(countries))
# #list can be changed
# #error
# countries = countries.append("Belgium")
# print(countries)
# powerball_numbers = [4, 8, 15, 16, 23, 42]
# def squares(numbers):
#     squares = 0
#     for a in numbers:
#         squares = a*a
#         print(squares)
#     return squares
        
# def squares(numbers):
#     squares = []
#     for a in numbers:
#         square = a*a
#         squares.append(square)
#     return squares
        
#print(squares(powerball_numbers))

# def convert_to_floats(numbers):
#     floats = []
#     for number in numbers:
#         floats.append(float(number))
#     return floats
# print(convert_to_floats(powerball_numbers))

# def even_or_odd(numbers):
#     result = []
#     for number in numbers:
#         if number % 2 == 0:
#             result.append("True") or #True
#         else:
#             result.append("False") or #True
#     return result
# print(even_or_odd(powerball_numbers))
# mountains = ["Mount Everest", "K2"]
# # print(mountains)

# mountains.extend(["Kangchenjua", "Lhoste", "Mkalu"])
# aa = ["eeee", "ewfd"]
# mountains.extend(aa)
# # mountains.append(aa)
# print(mountains)



# steaks = ["Tenderloin", "New York strip"]
# more_steaks = ["T-Bone", "Ribeye"]

# my_meal = steaks + more_steaks
# print(my_meal)

# steaks += more_steaks #this can be used for append method
# steaks += steaks.append(steaks)
# print(steaks)

# plays = ["Hemlet", "Macbeth", "King Lear"]
# plays.insert(1, "Julius Ceesar")
# print(plays)
# plays.insert(10, "aa")
# print(plays)
# action_stars = ["Norris", "Senegal", "Van Damme", "Schwarzenger"]
# # action_stars.pop()
# # print(action_stars)
# # last_action_hero = action_stars.pop()
# # print(last_action_hero)
# # action_stars.pop(1)
# action_stars.pop(-2)
# print(action_stars)
# soups = ["French Onion", "Clam Chowder", "Chicken noodle","aaaa"]
# #del soups[1]
# #del soups[-1]
# #del soups[1:3]
# print(soups)
# aaa = del[1]
# print(aaa)
 
# fruit = ["mango", "Lemon"]
# fruit.clear()
# print(fruit)
# vitamins = ["A", "D","K"]
# vitamins.reverse()
# print(vitamins)
# print(vitamins.reverse())
# temperatures = [40, 28, 52, 66, 35]
# temperatures.sort()
# print(temperatures)
# temperatures.reverse()
# print(temperatures)
# coffes =["Latte", "Eppre", "Macchiato"]
# coffes.sort()
# print(coffes)
# coffes = ["Latte", "espresso", "macchiato", "Frappucino"]
# coffes.sort() # capital letter sorts first
# print(coffes)
# coffes = ["Latte", "Espresso", "Macchiato", "Frappucino"]
# print(sorted(coffes)) #new list
# print(coffes)
# car_lot = ["Ford", "Dodge", "Toyota", "Ford", "Toyota", "Chevrolet", "Ford"]
# print(car_lot.count("Dodge"))
# print(car_lot.count("Toyota"))
# print(car_lot.count("Ferrari"))
# print(car_lot.count("dodge"))
# hours_of_sleep = [7.3, 7.0, 8.0, 7.0]
# print(hours_of_sleep.count(7.3))
# print(hours_of_sleep.count(7.0))
# print(hours_of_sleep.count(7))
# pizzas = [
#     "Mushroom",
#     "Pepperoni",
#     "Sausage",
#     "Barbecue Chicken",
#     "Pepperoni",
#     "Sausage"
# ]
# print(pizzas.index("Barbecue Chicken"))
# print(pizzas.index("Pepperoni"))
# print(pizzas.index("Sausage"))
# # # if "Olives" in pizzas: 
# #     print(pizzas.index("Olives"))
# print(pizzas.index("Sausage", 3))
# print(pizzas.index("Sausage", 2))
# units = ["meter", "kilogram", "second", "ampere", "Kelvin", "candela", "mole"]
# more_units = units.copy()
# print(units)
# print(more_units)
# units.remove("Kelvin")
# print(units)
# even_more_units = units[:]
# print(even_more_units
#split conver a string to a list
# users = "Bob, Dave, John, Sue, Randy, Meg"
# # print(users.split(", "))
# print(users.split(", "))
# print(users.split(", ", 2))
# users.split()
# pri nt(users.split(", "), 3))
# sentence = "I am learning how to code"
# words = sentence.split(" ")
# print(words)
# words = sentence.split("")
# print(words)
#join method is opposite of split
# address = ["500 Fifth Avenue", "New York", "NY", "10036"]
# print(",".join(address))
# print(", ".join(address))
# print("".join(address))
# breakfasts = ["Eggs", "Cereal", "Banana"]
# lunches = ["Sushi", "Chicken Teriyaki", "Soup"]
# dinners = ["Steak", "Meatballs", "Pasta"]
# print(zip(breakfasts, lunches, dinners))
# print(type(zip(breakfasts, lunches, dinners)))
# print(list(zip(breakfasts, lunches, dinners)))
# for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
#     print(f"My meal for today was {breakfast} and {lunch} and {dinner}")
# bubble_tea_flavors = [
#     ["Honeydew", "Mango", "Passion Fruit"],
#     ["Peach", "Plum", "Strawberry", "Taro"],
#     ["Kiwi", "Chocolate"]
# ]
# # print(len(bubble_tea_flavors))
# # print(bubble_tea_flavors[0])
# # print(bubble_tea_flavors[-1])
# # print(len(bubble_tea_flavors[0]))
# # print(bubble_tea_flavors[1][2])
# # print(bubble_tea_flavors[0][0])
# all_flavors = []

# # for flavor in bubble_tea_flavors:
# #     print(flavor[0])
# #     print(flavor[1])

# for flavor_pack in bubble_tea_flavors:
#     for flavor in flavor_pack:
#         all_flavors.append(flavor)
# # print(all_flavors)
# numbers = [3, 4, 5, 6, 7]
# # squares = []
# # for number in numbers:
# #     squares.append(number ** 2)
# # print(squares)
# # print(number)
# squares = [number ** 2 for number in numbers]
# print(squares)
# # print(number)
# rivers = ["Amazon", "Nile", "Yangzte"]
# print([len(river) for river in rivers])
# expressions = ["lol", "rofl", "lld"]
# print([expression.upper() for expression in expressions])
# print(type(expression.upper() for expression in expressions))
# print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])
# print([number/ 2 for number in range(20)])

# donuts = [
#   "Bostom Cream",
#   "Jelly",
#   "Vanilla Cream",
#   "Glazed",
#   'Chocalate Cream'
# ]

# creamy_donuts = []

# for donut in donuts:
#     if "Cream" in donut:
#         creamy_donuts.append(donut)
# print(creamy_donuts)

# creamy_donuts = [donut for donut in donuts if "Cream" in donut]
# print(creamy_donuts)

# print([len(donut) for donut in donuts if "Cream" in donut])
# print([donut.split(" ")for donut in donuts if "Cream" in donut])
# print([donut.split(" ")[0]for donut in donuts if "Cream" in donut])
# ace = ["df","dfg"]
# print(ace[-1])
# print(range(0,10,1))
# aa = ["aaa", "vsv"]
# aa.append("aaaa","aaa")
# numbers = [1,4,5,7,9]
# for indx, number in enumerate(numbers):
#     if number > 1 and number < 7:
#       numbers[indx] = number + 1
      
# print(numbers)
# print(["mic","does"][-1 ])
# print(["organic"].index("q"))
# module 13
# help(len)
# help("len")
# help(print)
#class
# help(str)
# help(int)
# help(list)
#method
# help("Hello".replace)
# help("mystery".swapcase)
# help([1].extend)
# numbers = [4, 8, 15, 16, 23, 42]
# print([cube ** 3 for cube in numbers ])
# def cube(number):
#     return number ** 3
# print(map(cube, numbers))
# print(list(map(cube, numbers)))
# animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
# print(list(map(len, animals)))
# animals = ["elephant", "horse", "cat", "giraffe", "cheetah", "dog"]
# long_words = [animal for animal in animals if len(animal) > 5]
# print(long_words)
# def is_long_animal(animal):
#     return len(animal) > 5
# print(filter(is_long_animal, animals))
# print(list(filter(is_long_animal, animals)))
# lamda function is an anonymous function
# metals = ["gold", "silver", "platinum", "palladium"]
# print(filter(lambda metal: len(metal) > 5, metals))
# print(list(filter(lambda metal: len(metal) > 5, metals)))
# print(list(filter(lambda el: len(el) > 5, metals)))
# print(list(filter(lambda word: "p" in word, metals)))
# print(list(map(lambda word: word.count("l"), metals)))
# print(list(map(lambda val: val.replace("s", "$"), metals)))

# print([metal for metal in metals if len(metal) > 5])
# lambda mee: len(mee) > 5
# print()
#all return true if all list is truthy
# print(all([True]))
# print(all([True, True]))
# print(all([True, True, False]))
# print(all([1, 2, 3]))
# print()
# print(all([1, 2, 3, 0]))
# print(all(["a", "b"]))
# print(all(["a", "b"]))
# print(all(["a", "b", ""]))
# print(all([]))# all empty list is True
# print()
# #any at like or , it is opposite of all
# print(any([True, False]))
# print(any([False, False]))
# print(any([0, 1]))
# print(any([0]))
# print(any([" ", ""])) #true
# print(any([""])) #false
# print(any([])) # any empty list False
# print(max([3, 5, 7]))
# print(max(3, 5, 7, 9))
# print(min(3, 5, 7))

# print(max("D", "Z", "K"))
# print(max("D", "Z", "K"))
# print(min(["D", "Z", "K"])
# )
# print(sum([2, 3, 4]))
# print(sum([-2, 3, -4]))
# print(dir([])) #show all method for 
#donder double __  hidden method to be used
# print(dir("pasta"))
# print(len("pasta"))# python look for donder method
# print("pasta".__len__())
# print("st" in "pasta")
# print("pasta".__contains__("st"))

# print("pasta " + "and meatballs")
# print("pasta ".__add__("and meatballs"))
# number = 0.123456789
# print(format(number, "f")) #f- floating point
# print(type(format(number, "f")))
# print(format(number, ".2f")) #.(number after .)
# print(format(number, ".3f"))
# #format means to organize .format is a srting
# print(format(0.5, "f"))
# print(format(0.5, "%"))
# print(format(0.5, ".2%"))
# print(format(0.5, ""))
# print(format(8123456, ","))

#module 14
#Tuple is a fixed length immutable list,its a sibling to list
# foods = "Sushi", "Steak", "Gluacamole"
# foods = ("Sushi", "Steak", "Gluacamole")

# print(type(foods))
# print(foods[])

# empty = ()
# print(type(empty))

# mystery = (1)
# print(type(mystery))
# mystery = (1, ) #not parenthesis that makes a tuple it is comma
# mystery = 1,
# print(tuple("abc"))
# print(tuple(["abc"]))
# birthday = (4, 12, 2991)
# print(len(birthday))
# print(birthday[0])
# print(birthday[1])
# print(birthday[2])
# #you can aslo use negative indexing, if the index is not found it gives indexError
# # birthday[1] = 13
# #tuple can contain mutable element and d element can be modified
# addresses = (
#     ['Hudson Street', 'New York', 'NY'],
#     ["Franklin Street", 'San Francis', 'CA']
# )
# addresses[1][0] = "Polk Street" 
# print(addresses)
# # you can"t change position or element in tuple
# print(dir(birthday))
# employee = ("Bob", "Johnson", "Manager", 50)
# first_name = employee[0]
# last_name = employee[1]
# position = employee[2]
# age = employee[3]
# print(employee)

# first_name, last_name, position, age = employee

# print(first_name, last_name, position, age)

# subject, verb, adjectibe = ["Python", "is", "fun"]
# print(subject)
# first_name, last_name, title = employee
# first_name, last_name, positiom, age, salary = employee
# a = 5
# b = 10
# b, a = a, b
# print(a)
# print(b)
#left hand side of equal sign happens first
# first_name, last_name, *details = employee
# print(first_name)
# print(last_name)
# print(details)# will return a list
# *names, position, age = employee #reverse of assigning
# print(age)
# print(position)
# print(names)
# first_name, *details, age = employee
# print(first_name)

# print(age)
# print(details)
# first_name, last_name, position, *details = employee
# print(details)
# def acceot_stuff(*args): #you can cal the args anything
#     print(type(args))
#     print(args)
# acceot_stuff(1)
# acceot_stuff(1,3, 5)
# acceot_stuff()

# def my_max(nonesense, *numbers):
#     print(nonesense)
#     greatest = numbers[0]
#     for number in numbers:
#         if number > greatest:
#             greatest = number
#     return greatest
# print(my_max("Shazam", 1))
# print(my_max("oboy",2, 3, 4))
# print(my_max(1, 3))
# print(my_max(1, 3, 9, 6, 7, 8, -14))
# print()
# #This is different
# def my_max(*numbers, nonesense):
#     print(nonesense)
#     greatest = numbers[0]
#     for number in numbers:
#         if number > greatest:
#             greatest = number
#     return greatest
# # print(my_max(1,2, 3, 4, nonesense = "Shazam"))
# def product(a, b):
#     return a*b
# print(product(3, 5))
# numbers = [3, 5]
# numbers = (3, 5)
# print(product(numbers))
# print(product(*numbers)) # * is use for list and tuple
#object has a data type and a variable does not
# a = 3
# a = 10
# a = "hello"
# a = [1, 2, 3]
# #garbage collection is how objects are disposed
# a = [4, 5, 6] #[1, 2, 3] is garbaged out
# a = 3
# b = a
# a = 5
# print(a)
# print(b) #numbers are imutable
# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)
# b.append(5)
# print(a)#list are mutable anything you do to be happen to a
# print(b)
# students = ["Bob", "Sally", "Sue"]
# athletes = students
# nerds = ["Bob", "Sally", "Sue"]

# print(students == athletes)
# print(students == nerds)

# print(students is athletes)
# print(students is nerds) #they don't have same identity, that is they are of diifernt object because list are mutable

# a = 1
# b = 1
# print(a == 1)
# print(a is b)

# a = 3.14
# b = 3.14
# print(a == b)
# print(a is b)

# a = "hello"
# b= "hello"
# print(a == b)
# print(a is b)
#not all object that are equal will be identical
#shallow copy create a new list 
# a = [1, 2, 3]
# b = a[:]
# print(a == b)
# print(a is b)

# c = a.copy()
# print(a == c)
# print(a is c)
# print()
# import copy
# a = [1, 2, 3]
# b = a[:]
# print(a == b)
# print(a is b)

# c = a.copy()
# print(a == c)
# print(a is c)

# d = copy.copy(a) #shallow copy only copy external to new object but not internal
# print(a == d)
# print(a is d)
#still the same
# numbers = [2, 3, 4]
# a = [1, numbers, 5]

# b = a[:]
# b = a.copy()
# b = copy.copy(a) #all same
# print(a == b) # True
# print(a is b) #False
# print(a[1] is b[1]) #true

# a[1].append(100)
# print(b) #external list of a and b are different but the internal list of the object are the same
#Deep copy create a copy of all object from top to the nested.compared to shallow copy because deepcopy copy and assign to a new object
# b = copy.deepcopy(a)

# print(a == b) # True
# print(a is b) #False
# print(a[1] is b[1]) #False as compared to shallow copy because deepcopy copy and assign to a new object
# a[1].append(100)
# print(b)
# print(a)

# b[1].append(200)

# print(b)
# print(a)
# dir()
# help()
# web_dev = ["HTML", "CSS", "JAVASCRIPT"]
# frontend = web_dev
# web_ dev.append("React")
# print(frontend)
#module 16
#dictionary is an unorderd data structure for declaring relationships between object
#dict is a mutable data structure consisting of pair of keys and values
# key is an object that serves as a unique identifier for value
# value is any python object
#  keys are unique, values can be duplicates
#keys must be immutable types(string, integers, floats, tuples) values can be any data type(mutable or immutable)
# list and dictionary are mutable.A dictionary can have key-value pairs added,removed or modified
#unlike a list dict is not orderes. A dict is used for mappings while a list is used for order
#{} is a literal
# ice_cream_preferences = {
#     "Benjamin": "Chocolate",
#     "Sandy": "Vanilla",
#     "Mary": "Cookies & Creme",
#     "Julia": "Chocolate"
# }
# print(len(ice_cream_preferences))
# flight_prices = {
#     "Chicago": 199,
#     "San Francisco": 499,
#     "Denver": 295
# }
# print(flight_prices["Chicago"])
# print(flight_prices["Denver"])
# # print(flight_prices["chicago"])
# gym_membership_packages = {
#     29: ["Machines"],
#     49: ["Machines", "Vitamin Supplements"],
#     79: ["Machines", "Vitamin Supplements", "Sauna"]

# }
# print(gym_membership_packages[49])
# print(gym_membership_packages[79])
# print(gym_membership_packages.get(29, ["Basic Dumbells"]))
# print(gym_membership_packages.get(100, ["Basic Dumbells"]))
# print(gym_membership_packages.get(100))

# pokemon ={
#     "Fire": ["Charmander", "Charmelon", "Charizard"],
#     "Water": ["Squirtle", "Warturtle", "Blastoise"],
#     "Grass": ["Bulbasaur", "Venusaur", "Ivysaur"]
# }

# print("Fire" in pokemon)
# print("Grass" in pokemon)
# print("Electric" in pokemon)

# print()

# print("Electric" not in pokemon)
# sport_team_rosters = {
#     "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
#     "New York Giants": ["Eli Manning", "Odell Beckham"]
# }
# # print(sport_team_rosters["Piisburgh Steelers"])
# sport_team_rosters["Piisburgh Steelers"] = ["Ben Roethlisberger"]
# sport_team_rosters["New York Giants"] = ["Eli Manning"]
# print(sport_team_rosters["Piisburgh Steelers"])

# video_game_options = {}
# # video_game_options = dict()
# video_game_options["subtitles"] = True
# video_game_options["dificulty"] ="Medium"
# video_game_options["volume"] = 7
# print(video_game_options)
# video_game_options["volume"] = 10
# print(video_game_options)
# video_game_options["Volume"] = 10
# print(video_game_options)
# words =["danger", "beware", "danger", "beware", "beware"]
# def count_words(words):
#     counts = {}
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts
# print(count_words(words))
# film_dirextors = {
#     "The Godgather": "Francis Ford Coppola",
#     "The Rock": "Micheal Bay",
#     "Goodfellas": "Martin Scorsese"
# }

# print(film_dirextors.get("Goodfellas"))
# print(film_dirextors.get("Bad Boys"))
# print(film_dirextors.get("Bad Boys", "Michael Bay"))#dosent mutate the dictionary
# print(film_dirextors)
# print()
# #film_dirextors.setdefault("Bad Boys")#mutate the dictionary set to none if no value is provided
# print(film_dirextors)
# film_dirextors.setdefault("Bad Boys", "Micheal Bay")#mutate the dictionary
# print(film_dirextors)
# film_dirextors.setdefault("Bad Boys", "A good direxctor")#but not when it has been set already
# print(film_dirextors)
# release_dates ={
#     "Python": 1991,
#     "Ruby": 1995,
#     "Java": 1995,
#     "Go": 2007
# }
# year = release_dates.pop("Java")
# print(release_dates)
# print(year)
# release_dates.pop("Go")
# print(release_dates)
# release_dates.pop("C++", 2000)
# new_year = release_dates.pop("C++", 2000)
# print(new_year)
# new_year = release_dates.pop("Ruby", 2000)
# print(new_year)

# del release_dates["Java"]
# print(release_dates)
# websites = {
#     "Wikipedia": "Http//:wikipedia.com",
#     "Google": "Google.com"
# }

# websites.clear()
# print(websites)
# del websites 
# print(websites)
# employee_salaries = {
#     "Guido": 100000,
#     "James": 500000,
#     "Brandon": 900000
# }
# extra_employee_salaries = {
#     "Yukihiro":1000000,
#     "Guido": 333333
# }
# # employee_salaries.update(extra_employee_salaries)
# extra_employee_salaries.update(employee_salaries)
# print(employee_salaries)
# print(extra_employee_salaries)
# print(dict()) # {}
# employee_titles = [
#     ["Mary", "Senior Manager"],
#     ["Brian", "Vice President"]
    
# ]
# print(dict(employee_titles))
# tv_shows ={
#     "The X-files": {
#         "Season 1": {
#             "Episodes": ["Scary Monster", "Scary Alien"],
#             "Genre": "Science Fricyion",
#             "Year": 1993
#         },
#         "Season 2": {
#             "Episodes": ["Scary Consipiracy"],
#             "Genre": "Horror",
#             "Year": 1994
#         }
#     },
#         "Lost": {
#             "Season 1": {
#                 "Episodes": ["What The is Happening On Island"],
#                 "Genre": "Science Fiction",
#                 "Year": 2004
#             }
#         }
#     }
# print(tv_shows["The X-files"]["Season 1"]["Genre"])
# print(tv_shows["The X-files"]["Season 1"]["Episodes"][0])
#module 17
# chinese_food ={
#     "Seaseme Chicken":9.99,
#     "Boneless Spare Ribs": 7.99,
#     "Fried Rice": 1.99
# }
# for food in chinese_food:
#     print(f"The food is {food} and the price is {chinese_food[food]}")
# #Anti-pattern is a solution to a programming problem that is considered ineffective or counter productive

# pounds_to_kilograms = {
#     5: 2.26796,
#     10: 4.52592,
#     25: 11.3398
# }

# for p in pounds_to_kilograms:
#     print(f"{p} pounds is equal to {pounds_to_kilograms[p]} kilogram" )
# college_courses = {
#     "History": "Mr. Washington",
#     "Math": "Mr. Newton",
#     "Science": "Mr. Einstein"
# }

# for key, value in college_courses.items():
#     print(f"The course {key} is being taught by {value}.")
# for _, professor in college_courses.items():#_ is use to communicate to other developers
#     print(f"The next professor is {professor}")
# crypto = {
#     "Bitcoin": 4000000,
#     "Etereum": 7000,
#     "Litecoin": 10
# }
# print(crypto.keys())
# print(type(crypto.keys()))
# print(crypto.values())
# print(type(crypto.values()))
# for cur in crypto.keys():
#     print(f"The next {cur}")
# for pri in crypto.values():
#     print(f"The next price is {pri}")
# print("Bitcoin" in crypto.keys())
# print("ripple" in crypto.keys())
# print()
# print(10 in crypto.values())
# print("ripple" in crypto.values())

# print(len(crypto.keys()))
# print(len(crypto.values()))
# print(len(crypto))

# mi = ["a", "b", "c"]
# mic = mi.index("c")
# print(mic)
# mmmm = 2, 3, 4
# print(type(mmmm ))
# numbers = [4, 7, 2, 9]
# # print(sorted(numbers))#list is not mutated returns another object
# print(numbers)
# numbers.sort()#it modifies the list that it act upons
# print(numbers)
#sorted sort  key of dictionary
# salaries = {
#     "Executive Assistant": 20,
#     "CEO": 100
# }
# print(sorted(salaries))
# print(salaries)

# wheel_count = {
#     "truck": 2,
#     "car": 4,
#     "bus": 8
# }
# sorted(wheel_count.items())
# print(sorted(wheel_count.items()))
# for vehicle, count in sorted(wheel_count.items()):
#     print(f"The next vehicle is a{vehicle} and it has {count} wheels")
# concert_attendees = [
#     {"name": "Taylor", "section": 400, "price paid": 99.99},
#     {"name": "Christiana", "section": 200, "price paid": 149.99},
#     {"name": "Jeremy", "section": 100, "price paid": 0.0}

# ]
# for attendee in concert_attendees:
#     for key, value in attendee.items():
#         print(f"The {key} is {value}")
# def length(word):
#     return len(word)
# print(length("Hello"))
# print(length(word = "Hello"))
# # print(length(wof = "Hello"))
# def collect_keyword_arguments(**kwargs): #it dosent have to be kwargs permanently
#     print(kwargs)
#     print(type(kwargs))

#     for key, value in kwargs.items():
#         print(f"The key is {key} and the value is {value}")
# collect_keyword_arguments(a = 2, b = 3, c = 4)
# def args_and_kwargs(a, b, *args, **kwargs):
#     print(kwargs)
#     print(args)
# def args_and_kwargs(a, b, *args, **kwargs):
#     print(f"regular {a + b}")
#     print(f"args {sum(args)}")
# def args_and_kwargs(a, b, *args, **kwargs):
#     print(kwargs)
#     print(args)

#     dict_total = 0
#     for value in kwargs.values():
#         dict_total += value
#     print(f"Total value of kwargs dict is {dict_total}")
# args_and_kwargs(1, 2, 3, 4, 5, 6, x = 8, y = 9, z = 10)
#** is used for dict, *for tuples and/or list
# def height_to_meters(feet, inches):
#     total_inches = (feet * 12) + inches
#     return total_inches * 0.0254
# print(height_to_meters(5, 11))

# stats = {
#     "feet": 5 ,
#     "inches": 11
# }

# print(height_to_meters(**stats))

# stats = {
#     "feets": 5 ,
#     "inches": 11
# }

# print(height_to_meters(**stats))

# stats = {
#     "feet": 5 ,
#     "inches": 11,
#     "nonesense": 1
# }

# print(height_to_meters(**stats))
#dict comprehension create a dict from an object iteration
# languages = ["Python", "Javascript", "Ruby"]
# lengths = {language: len(language) for language in languages if "t" in language}
# print(lengths)
# word = "supercalifragilisticexpialidocious"
# letter_counts = {letter: word.count(letter) for letter in word if letter > "j"}
# print(letter_counts)

# capitals = {
#     "New York": "Albuny",
#     "California": "Sacremento",
#     "Texas": "Austin"
# }

# inverted = {capital: state for state, capital in capitals.items() if len(state) != len(capital) }
# print(inverted)
# print(capitals)
#module 18
#set is a  mutable, unordered data structur that prohibits duplicate values
#if you add duplicate value it will delete the former
#set only takes immutable objects like number, strings
# stocks = {"MSFT", "FB", "IBM", "FB"}
# print(stocks)
# prices = {1, 2, 3, 4, 5, 3, 4, 2}#no duplicate
# print(prices)
# lotter_numbers = {(1, 2, 3), (4, 5, 6), (1, 2, 3)}
# print(lotter_numbers)

# print(len(stocks))
# print(len(prices))
# print(len(lotter_numbers))

# print('MSFT' not in stocks)
# print('GOOG' not in stocks)

# # print(stocks[2]) # not order
# for number in lotter_numbers:
#     for num in number:
#         print(num)

# squares ={number ** 2 for number in  [-5, -4, -3, 3, 4, 5] } 
# print(squares)
# print(len(squares))
# print(set([1, 2, 3]))
# print(set([1, 2, 3, 3, 2, 1]))

# print(set((1, 2)))
# print(set((1, 2, 1, 2)))

# print(set("abc"))# this show set is unordered
# print(set("aaabcc"))

# print(set({"key": "value"})) #only returns  key 

# philosophers = ["Plato", "Socrates", "Aristotle", "Pythagoras", "Socrates", "Plato" ]
# philosophers_set = set(philosophers)
# list(philosophers_set)
# print(philosophers)
# disney_characters = {
#     "Mickey Mouse",
#     "Minnie Mouse",
#     "Elisa"

# }

# disney_characters.add("Ariel") #add is similar to append of list.add only accept string and expand set once
# print(disney_characters)

# disney_characters.add("Elisa")
# print(disney_characters)

# disney_characters.update(["Donald Duck", "Goofy"]) #update  is similar to extend of list. update can accept any data structure whether str,list...  expands multiple #update  expands multiple
# print(disney_characters)
# agents = {"Mulder", "Scully", "Dogget", "Reyes"}

# agents.remove("Dogget")
# print(agents)

# agents.remove("Skinner") #give an error
# agents.discard("Doggett")
# print(agents)

# agents.discard("Skinner") #raise no error
# print(agents)
#frozenst is an immutable set
# mr_freeze = frozenset([1, 2, 3, 2])
# print(mr_freeze)

# mr_freeze.add(4) #cannot be changed
# regular_set = {1, 2, 3}
# print({ regular_set: "some value"})
# print({mr_freeze: " Some value"})
# module 19
#module is a file to be run in another file while script is to be executed directly
#module is an object also
# import calculator
# print(calculator.creator)
# # print(calculator.creator)
# print(calculator.PI)
# print(calculator.add(3, 5))
#standard library is a collection of tools built into a 
#language to accelerate developer prroductivity
# import string
# import math
# import this  #zen of python

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.digits)
# # print(string.digits)
# print(string.capwords("hello there"))
# print(math.ceil(4)) #smallest integer greater than th arg
# print(math.floor(4.8)) #floor
# print(math.sqrt(9))
# print(math.sqrt(32))
# print(math.pi)


#your module and your script must be in same directory(folder)
# import math
# import calculator
#same as
# import math, calculator
# print(math.__name__)
# print(calculator.__name__)
# print(__name__)
# if a file is being run as a script donder name will evaluate to donder main
#but if a file is being used as a module  donder name will evaluate to the file name
# print(calculator.area(5))
# import calculator as calc
# import datetime as dt
# print(calc.add(3, 5))
# from calculator import creator, add, subtract
# from math import sqrt

# print(creator)
# print(add(2,3))
# print(subtract(10, 5))
# print(sqrt(49))
# from calculator import *

# print(creator)
# print(add(3, 5))
# print(year)
#A package is a directory module
#when __init__.py is present in a directory gf
#and other module in the directory is imported. python will firstly run the init donder
import feature
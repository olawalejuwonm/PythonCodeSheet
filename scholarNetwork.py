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
# print(gym_membership_packages)

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
#Python Standard Library is combination or collection of modules or tools built into python to improve(revamp) developer output. They are things built so
#  that developers don't have to build them again
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
# import feature.Snass9

# print(feature.Snass9.mic)
# import feature.Subfeature.calculator
# import feature.Snass9

# print(feature.Subfeature.calculator.subtract(10, 5))
# print(feature.Snass9.mic)
# from feature import Subfeature
# from feature.Subfeature import calculator
# from feature.Subfeature.calculator import subtract
# print(subtract(10,3))
# import feature.Subfeature.calculator
# print(feature.Subfeature.calculator.subtract(10, -1))
# import feature.Subfeature
# print(feature.Subfeature.subtract(10, -1))
#module 20
# r means read
#this is not best practices
# cupcakes_file = open("sream.txt", "r" )
# #faulty code
# cupcakes_file.close() #this close the file
#best practices
# with open("sream.txt", "r" ) as cupcakes_file:
#     print("The file has been opened")
#     print(cupcakes_file.read())
#     

# print("The file has been closed.we are outside the context block")

# # filename = input("What file would you like to open")
# with open(filename, "r") as file_object:
#     print(file_object.read())
# with open("sream.txt", "r" ) as cupcakes_file:
#     for line in cupcakes_file:
#         # print(line)
#         print(line.rstrip())
# file_name = "my_first_file.txt"
# with open(file_name, "w") as file_object: #w is write
#     file_object.write("Hello file!\n")
#     file_object.write("You are my favorite file")
#appending to a file
# with open("my_first_file.txt", "a") as file_objects: #a is append
#     file_objects.write("\nThird line is the best line!")
#using append mode when file dosent exist python will create the file
#continue to append to it
#but write will overwrite and continue to overwrite
#module 21
#decorator enhances a function with another features  without changing the functionality
#higher order function is a function that either accepts a function as an argument or returns a function as a return value
#function is an object
# def one():
#     return 1
# print(type(one)) #this is acting as higher order 

# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def calculate(func, a, b):
#     return func(a, b)
# print(calculate(add, 3, 5))
#Gallons to cups
#1 gallons = 4 quarts
#1 quart = 2 pints
#1 pint = 2 cups

# def convert_gallons_to_cups(gallons):
#     def gallons_to_quarts(gallons):
#         print(f"Coverting {gallons} gallons to quarts")
#         return gallons * 4
#     def quarts_to_pints(quarts):
#         print(f"Convering {quarts} quarts to pints")
#         return quarts *  2
#     def pints_to_cups(pints):
#         print(f"Convering {pints} pints to cups")
#         return pints * 2
#     quarts = gallons_to_quarts(gallons)
#     pints = quarts_to_pints(quarts)
#     cups = pints_to_cups(pints)
#     return cups
# print(convert_gallons_to_cups(1))
# print(convert_gallons_to_cups(3))

# print(pints_to_cups(1)) #this is not declare outside the block
# def calculator(operation):
#     def add(a, b):
#         return a + b
#     def subtract(a, b):
#         return a - b
#     if operation == "add":
#         return add
#     elif operation == "subtract":
#         return subtract
# print(calculator("add")(10, 4))
# print(calculator("subtract"))
# print(calculator("subtract")(7, 7))
# def calculator(a):
#     return a
# print(calculator("a")(1))
#my own demonstration
# def calculator(operation):
#     def addition(a, b):
#         return a + b
#     def subtraction(a, b):
#             return a - b
#     def add(nnn):
#         return addition
#     def subtract(mmm):
#         return subtraction
#     if operation == "add":
#         return add
#     elif operation == "subtract":
#         return subtract
# print(calculator("add")("hf")(10, 4))
# print(calculator("subtract")("ds")(7,7))
# print(calculator("subtract")(7, 7))
# def square(num):
#     return num ** 2
# def cube(num):
#     return num ** 3
# def times10(num):
#     return num * 10
# operations = [square, cube, times10]

# for func in operations:
#     print(func(5))
#scope is the location in a program in which a name can be used
# age = 28 #age is scoped to this file, its global scope
# #local scope is limited to the block it has been assigned
# age = 28
# def fancy_func():
#     age = 100 #age is a shadow variable because it shares same name with global variable
#     print(age)
# fancy_func()
# print(age)
#constant is a name for a value that does not change over the program's execution
# TAX_RATE = 0.08
# def calculate_tax(price):
#     return round(price * TAX_RATE, 2)
# def calculate_tip(price):
#     return round(price * (TAX_RATE * 3), 2)
# print(calculate_tax(10))
# print(calculate_tip(10))

#LEGB - Local/ Enclosing Functions/Global/Built-in
# x = 15
# def outer():
#     # x = 10
#     # Enclosing function
#     def inner():
#         # LOcal scope
#         # x = 5
#         # return x
#         return len
#     return inner()
# print(outer()("python"))
# closure is a programming pattern in which a scope retains acces to an enclosing scope's names
# def outer():
#     candy = "Snickers"

#     def inner():
#         return candy
#     return inner
# the_func = outer()
# print(the_func())
# x = 10

# def change_stuff():
#     global x # this make x that follow a global variable
#     x = 15
# # print(x)
# change_stuff()
# print(x)
#nonlocal keyword is used inside a body of nestef function
# def outer():
#     bubble_tea_flavor = "Black"
#     def inner():
#         nonlocal bubble_tea_flavor #nonlocal make it for enclosure variable
#         bubble_tea_flavor = "Taro"
#     inner() # the value of buble tea flavor for inner() is deleted after running
#     return bubble_tea_flavor
# print(outer())
#print(bubble_tea_flavor)
#decorator takes function as input and ouput function as an output
# def be_nice(fn):
#     def inner():
#         print("Nice to execute ur function")
#         fn()
#         print("Its good exectuting your function")
#     return inner
# @be_nice #must return a function, it works with any function that follows it.
#it takes the function that follows it as its own argument.i.e be_nice(complex_business_logic)() and calls it

# def complex_business_logic():
#     print("Something complex")
# # print(be_nice(complex_business_logic))

# @be_nice
# def another_fancy_function():
#     print("Goo goo gaga")
# # result = be_nice(complex_business_logic)
# # result()
# # be_nice(complex_business_logic)()
# #decorators decorate enhance function
# #@ syntactic makes things easy to express
# # complex_business_logic()
# another_fancy_function()
# def be_nice(fn):
#     def inner(*args, **kwargs):
#         print("Nice to execute ur function")
#         print(args)
#         print(kwargs)
#         # fn()
#         print("Its good exectuting your function")
#     return inner
# @be_nice
# def complex_business_logic(stakeholder):
#     print(f"Something complex for{stakeholder}!")
# # complex_business_logic("mic")
# complex_business_logic(stakeholder = "Boris", hello = True )
# complex_business_logic("mic")
# def be_nice(fn):
#     def inner(*args, **kwargs):
#         print("Nice to execute ur function")
#         print(args)
#         print(kwargs)
#         fn(*args, **kwargs)
#         print("Its good exectuting your function")
#     return inner
# @be_nice
# def complex_business_logic(stakeholder):
#     print(f"Something complex for {stakeholder}!")
# # complex_business_logic("mic")
# complex_business_logic("mic")
# print()
# complex_business_logic(stakeholder = "Mic")

# def be_nice(fn):
#     def inner(*args, **kwargs):
#         print("Nice to execute ur function")
#         print(args)
#         print(kwargs)
#         fn(*args, **kwargs)
#         print("Its good exectuting your function")
#     return inner
# @be_nice
# def complex_business_logic(stakeholder, position):
#     print(f"Something complex for our {position} {stakeholder}!")
# complex_business_logic("Mic", "CEO")
# print()
# complex_business_logic(stakeholder = "Mic", position = "Ceo")

# def be_nice(fn):
#     def inner(*args, **kwargs):
#         print("Nice to execute ur function")
#         print(args)
#         print(kwargs)
#         # return fn(*args, **kwargs) #this will quit execution
#         result = fn(*args, **kwargs)
#         print("Its good executing your function")
#         return result
#     return inner
# @be_nice
# def complex_business_sum(a, b):
#     return a + b # when it sees return , this one run last
# print(complex_business_sum(a = 3, b =5))

# import functools
# def be_nice(fn):
#     @functools.wraps(fn)
#     def inner(*args, **kwargs):
#         print("Nice to execute ur function")
#         print(args)
#         print(kwargs)
#         # return fn(*args, **kwargs) #this will quit execution
#         result = fn(*args, **kwargs)
#         print("Its good executing your function")
#         return result
#     return inner
# @be_nice
# def complex_business_sum(a, b):
#     "Adds two numbers together"
#     return a + b # when it sees return , this one run last
# print(complex_business_sum(a = 3, b =5))

# help(complex_business_sum) #do this without @benice when functools is not used
# print(dir({}))
# gdh = {2: "ee"}
# gdh.get()
#module 22
#object oriented programming is a paradigm for code organization and design that views a software program as acollection of objects that interact with each other
#an object is a container of data and behaviour
#Attributes define an objects state or internal dat
#attributes is viewed as variable belonging to an object
#method can be view as function belonging to an object
#method is a command or an instruction or a message to an object
#method can interact with and modify the objects attributes thus altering its state
#class is  a blueprint for defining object type in pyhon
#class definition describes attributes and methods that each made drom the class will have
#module cannot be used to create a container, its just a container calss can be use to create multiple object
#instance is an object created from a class
#act of creating instance is called instantaition
#objects of same class are independent of one another
# class Person(): #class we capitalise the first word
#     pass # the code block has no content

# class DatabaseConnection():
#     pass
# boris = Person()
# sally = Person()

# print(boris)
# # print(sally)


# # dc = DatabaseConnection()
# # print(dc)
# class Guitar():
#     def __init__(self, wood): #init require a parameter define
#         self.wood = wood
#         # print(f"A new guitar is being created.The object is {self}")
#         # self.wood = "Mahogany" #best practices

# acoustic = Guitar()
# # print(acoustic)
# electric = Guitar()
# acoustic = Guitar("Alder")
# # print(acoustic)
# electric = Guitar("Mahogany")
# #attribute is a piece of data stored on an object
# acoustic.wood = "Mahogany" 
# acoustic.strings = 6
# acoustic.year = 1990

# electric.nickname = "Sound Viking 3000"
# # print(wood)
# print(acoustic.wood)
# print(electric.wood)
# baritone = Guitar("Alder")
# print(baritone)
# print(electric.nickname)
# print(acoustic.year)
# print(electric.nickname)
# class Book():
#     def __init__(self, title, author, price = 14.99):
#         self.title = title
#         self.author = author
#         self.price = price
# animal_farm = Book("Animal Farm", "George Orwell", 14.99)
# gatsby = Book("The Great Gatsby", "F.scoot", 14.99)
# animal_farm = Book("Animal Farm", "George Orwell", 99.9)
# gatsby = Book("The Great Gatsby", "F.scoot")
# atlas = Book(title = "Atlas", author = "Ayn Rand")
# jude = Book(author = "Jude the obs", title ="clara")
# print(atlas.author)
# print(jude.price)
# print(animal_farm.price)
# print(gatsby.price)
#Instance method is a function that belongs to an object'
# class Pokemon():
#     def __init__(self, name, specialty, health = 100):
#         self.name = name
#         self.specialty = specialty
#         self.health = health
#     def roar(self): #all instance method must take self as their first parameter
#         print("Raaaaaaaarr!")
#     def describe(self):
#         print(f"I am {self.name}, I am a {self.specialty} Pokemon")
#     def take_damage(self, amount):
#         self.health -= amount
#         # return self.health

# squirtle = Pokemon("Squirtle", "Water")
# charmender = Pokemon("Charmender", specialty = "Fire", health = 110)
# squirtle.roar()
# squirtle.describe()
# charmender.describe()
# print(squirtle.health)
# #or 
# squirtle.health = 60
# print(squirtle.health)
# protected attribute are those that begins with _ they tell developers
#that the value cant be changed by assigning to another value but
#only by method
# class SmartPhone():
#     def __init__(self):
#         self._company = "Apple"
#         self._firmware = 10.0
#     def get_os_version(self):
#         return self._firmware
#     def update_firmware(self):
#         print("Reaching out to server for next version")
#         self._firmware += 1
# iphone = SmartPhone()
# print(iphone._company)
# print(iphone._firmware)
# print(iphone.update_firmware())
# print(iphone._firmware)
#Getter and setters are instance method that get/set atrributes value on an object
# class Height():
#     def __init__(self, feet):
#         self._inches = feet * 12
#     def _get_feet(self):
#        return  self._inches / 12
#     def _set_feet(self, feet):
#         if feet >= 0:
#             self._inches = feet * 12
#     feetm = property(_get_feet, _set_feet) #property act as attribute
# h = Height(5) #this set feet to  5
# print(h.feetm) #this is running property, and since we are getting,i.e printing the first attribute is run
# h.feetm = 6 #the second argument of property will run
# print(h.feetm)
# h.feetm = -10
# print(h.feetm)
#property and attribue must not be the same name because property act as attribute
# class Currency():
#     def __init__(self, dollars):
#         self._cents = dollars * 100
#     @property #another way to define property function, this define getter parameter
#     def dollars(self):
#         return self._cents / 100
#     @dollars.setter #this defind setter parameter(second argument)
#     def dollars(self, dollars):
#         if dollars >= 0:
#             self._cents = dollars * 100
# bank_account = Currency(50000)
# print(bank_account.dollars)
# bank_account.dollars = 100000
# print(bank_account.dollars)
# bank_account.dollars = - 100000
# print(bank_account.dollars)

# class Height():#just for practce
#     def __init__(self, feet):
#         self._inches = feet * 12
#     @property #when using this, the name of function define will be use to reference the getter
#     def _get_feet(self):
#        return  self._inches / 12
#     @_get_feet.setter  #when using this, the name of function define will be use to reference the setter
#     def _set_feet(self, feet):
#         if feet >= 0:
#             self._inches = feet * 12

# h = Height(5)
# print(h._get_feet)
# h._set_feet = 6
# print(h._get_feet)
# stats = {
#     "name": "BBQ Chicken",
#     "price": 19.99,
#     "size": "Extra Large",
#     "ingredients": ["Chicken", "Onions", "BBQ Sauce" ]

# }
# class Pizza():
#     def __init__(self, stats):
#         for key,value in stats.items():
#             setattr(self, key, value) #setattr accept three argument which are the object, the attribute name and lastly the value of the attribute
        

# bbq = Pizza(stats)
# print(bbq.size)
# # print(bbq.ingredients)
# # for attr in ["price", "name", "diameter", "disounted"]:
# #     print(getattr(bbq, attr, "Unknown" )) #getattr accept three arguments which are the object, the attribute to get, lastly the value to give if attr is not present
# #hasattr accept object and the attr
# #delattr acept object and attr
# stats_to_delete = ["size", "diameter", "spiceness", "ingredients"]
# for stat in stats_to_delete:
#     if hasattr(bbq, stat):
#         delattr(bbq, stat)
# print(bbq.size)
# class SushiPlatter():
#     def __init__(self, salmon, tuna, shrimp, squid):
#         self.salmon = salmon
#         self.tuna = tuna
#         self.shrimp = shrimp
#         self.squid = squid
#     @classmethod #define a class method instead instead of instance method
#     def lunch_special_A(cls): #cls can be anything
#         return cls(salmon = 2, tuna =2, shrimp = 2, squid = 0) #returns the class
#     @classmethod
#     def tuna_lover(cls):
#         return cls(salmon = 8, tuna = 10, shrimp = 0, squid = 10) #all rhe salmon assigned here will be for the class __init__ values automatically
# boris = SushiPlatter(salmon = 8, tuna = 4, shrimp = 5, squid = 10)
# print(boris.salmon)
# lunch_eater = SushiPlatter.lunch_special_A()
# print(lunch_eater.salmon)
# print(lunch_eater.squid)
# tuna_fan = SushiPlatter.tuna_lover()
# print(tuna_fan.tuna)
# class Counter():
#     count = 0 #this is a class attribute
#     def __init__(self):
#         Counter.count += 1
#     @classmethod
#     def create_two(cls):
#         two_counters = [cls(), cls()]
#         print(f"New number of counter objects created: {cls.count}")
#         return two_counters

    
# print(Counter.count)
# c1 = Counter()
# print(Counter.count)
# c2, c3 = Counter.create_two()
# print(Counter.count)

# #count(class attribute) cant be accesed by instances
#but the print value below returns 3 the class example defined below explains better
# print(c1.count)
# print(c2.count)
# print(c3.count)
# class Example():
#     data = "Class attribute!"
# e1 = Example()
# e2 = Example()
# print(e1.data) #this returns value of data which is class attribute
# #whereas there is no __init__ that define the instance method, since this is not found
# #it looks up to the class attribute
# print(e2.data)
# e1.data = "Instance attribute!"
# print(e1.data) #since attr of e1.data is defined it prints it
# print(e2.data)
# del e1.data
# print(e1.data) 
# print(e2.data)
# class WeatherForecast():
#     def __init__(self, temperatures):
#         self.temperatures = temperatures
#     @staticmethod #this will be available on instance and as class method
#     def convert_from_fahrenheit_to_celsius(fahr):
#         calculation = (5/9) * (fahr - 32)
#         return round(calculation, 2)


#     def in_celsius(self):
#         return [self.convert_from_fahrenheit_to_celsius(temp) for temp in self.temperatures]
# wf = WeatherForecast([100, 90, 80, 70, 60])
# print(wf.in_celsius())
# print(WeatherForecast.convert_from_fahrenheit_to_celsius(100))
#@static method is because it receives neither the instance(object) nor the class .they only recieve the argument you want to work on
#Hook is a procedure that intercepts a process at some point in its execution
#magic method is a hook and also a dunder
# print(3.3 + 4.4)
# print(3.3.__add__(4.4))
# print(len([1, 2, 3]))
# print([1, 2, 3])
# print([1, 2, 3].__len__())
# print("h" in "hello")
# print("hello".__contains__("h")) 
# print(["a", "b", "c"][2])
# print(["a", "b", "c"].__getitem__(2))
# class Card():
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#     # def __str__(self): #this(they are instance method) define what to return when instance is created
#     #     # return "Hello"
#     #     return f"{self.rank} of {self.suit}"
#     def __repr__(self):#if dunder str is not define pyhon use this
#         return f'Card("{self.rank}", "{self.suit}")'
# c = Card("Ace", "Spades")
# print(c)
# print(str(c))
# print(repr(c))
# print(c.__str__())
# print(c.__repr__())
# class Student():
#     def __init__(self, math, history, writing):
#         self.math = math
#         self.history = history
#         self.writing = writing
#     @property
#     def grades(self):
#         return self.math + self.history +self.writing
#     def __eq__(self, other_student):#equality
#         return self.grades == other_student.grades
#     def __gt__(self, other_student):#greater than
#         return self.grades > other_student.grades
#     #ge is greater than or equal to
#     def __le__(self, other_student):#less than or equal to
#         return self.grades <= other_student.grades
#     def __add__(self, other_student):
#         return self.grades + other_student.grades
#     def __sub__(self, other_student):
#         return self.grades - other_student.grades
    
# bob = Student(math = 90, history = 90, writing = 90)
# moe = Student(math = 100, history = 90, writing = 80)
# joe = Student(math = 40, history = 45, writing = 50)
# print(moe > joe)
# print(joe <= bob)
# print(bob + moe)
# print(moe - joe)
# print(bob.grades)
# print(moe.grades)

# print(bob == moe)
# print(moe == bob)
# print(bob == joe)
# print(moe == joe)

# print(bob != joe)
# print(joe != moe)
#Doc string is a regular python string that creates technical documentation for a piece of your program
# """
# A module related to joy of sushi.
# No fishy code here!

# """
# def fish():
#     """
#     Determines if fish is good
#     always return true
#     """
# class Salmon():
#     """
#     Blueprint for a salmon object
#     """
#     def __init__(self):
#         self.tastiness = 10
#     def bake(self):
#         """
#         Bake The Fish In an oVen
#         """
#         self.tastiness += 1
# class Emotion():
#     def __init__(self, positivity, negativity):
#         self.positivity = positivity
#         self.negativity = negativity
#     def __bool__(self):
#         return self.positivity > self.negativity
# my_emotional_state = Emotion(positivity = 50, negativity = 75)
# print(my_emotional_state.__bool__())
# if my_emotional_state:
#     print("This will not print")

# my_emotional_state.positivity = 100
# print(my_emotional_state.__bool__())
# if my_emotional_state:
#     print("This will print")
#namedtuple are immutable and are use to create instance with attributes with no methods
#e.g a user database
# import collections
# Book = collections.namedtuple("The_Book", ["title", "author"]) #we dont have to define class or dunder init
# # collections.namedtuple("Book", ["title", "author"])
# animal_farm = Book("Animal Farm", "George Orwell")
# gatsby = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald")
# # print(animal_farm)
# # print(gatsby)
# # print(animal_farm[0])
# # print(gatsby[1])
# # print(animal_farm.title)
# # print(gatsby.author)

# # word = "dynasty"
# # print(len(word))
# # print(word.__len__())


# class Library():
#     def __init__(self, *books):
#         self.books = books
#         self.librarians = []
#     def __len__(self):
#         return len(self.books)

# l1 = Library(animal_farm)
# l2 = Library(animal_farm, gatsby)
# print(len(l1))
# print(len(l2))
#dunder get and set method
# pillows = {
#     "soft": 79.99,
#     "hard": 99.99
# }

# print(pillows["soft"]) #this is running ger item
# print(pillows.__getitem__("Soft"))

# class CrayonBox():
#     def __init__(self):
#         self.crayons = []
#     def add(self, crayon):
#         self.crayons.append(crayon)
#     def __getitem__(self, index):
#         return self.crayons[index]
#     def __setitem__(self, index, value):
#         self.crayons[index] = value
# cb = CrayonBox()
# cb.add("Blue")
# cb.add("Red")
# print(cb.crayons[1])
# print(cb[0])

# cb[0] = "Yellow"
# print(cb[0])
# for crayon in cb:
#     print(crayon)
# for crayon in cb.crayons:
#     print(crayon)
# import time
# class Garbage():
#     def __del__(self): #is invoked when instance is no longer used about to be thrown out i.e it runs when your class is done running
#         print("This is my last breath!")
# g = Garbage()
# g = [1, 2, 3]
# time.sleep(5)
# print("Program done!")
#inheritance is a design pattern in which a class ingerits (or receives) attributes and methods from one or more classes
#inheritance helps to organize related classes and reduce duplication
#class being inherited is parent,super class or bare class
#the class that inherits is child,sub class, or derived class
#Public and protectected attribute beginning with single under score will be inherited
#private, beginning with double underscores are not inherited by sub class except dunder init
#subclass is a type of superclass e.g coffeshop is a type of store
# class Store():
#     def __init__(self):
#         self.owner = "Boris"
#     def exclaim(self):
#         return "Lots of stuuf to buy"
# class CoffeShop(Store):
#     pass

# starbucks = CoffeShop()
# print(starbucks.owner)
# print(starbucks.exclaim())
# class Employee():
#     def do_work(self):
#         print("I'm working")
# class Manager(Employee):
#     def waste_time(self):
#         print("Wow, this youtube video looks fun")
# class Director(Manager):
#     def fire_employee(self):
#         print("You're fired!")
# e = Employee()
# m = Manager()
# d = Director()

# e.do_work()
# # e.waste_time()

# m.do_work()
# m.waste_time()

# d.do_work()
# d.waste_time()
# d.fire_employee()
# class Teacher():
#     def teach_class(self):
#         print("Teaching stuff...")
#     def grab_lunch(self):
#         print("Yum yum yum")
#     def grade_tests(self):
#         print("F! F! F!")
# class CollegeProfessor(Teacher):
#     def publish_book(self):
#         print("Hooray, I'm an author")
#     def grade_tests(self):#this over ride method in the super class
#         print("A! A! A!")
    
# teacher = Teacher()
# professor = CollegeProfessor()

# teacher.teach_class()
# teacher.grab_lunch()

# professor.publish_book()
# professor.grade_tests()
# class Animal():
#     def __init__(self, name):
#         self.name = name
#     def eat(self, food):
#         return f"{self.name} is enjoying the {food}"
# class Dog(Animal):
#     pass

# watson = Dog() #error because Dog inherit Animal
# watson = Dog("Watson")
# print(watson.eat("food"))
# print(watson.name)

# class Animal():
#     def __init__(self, name):
#         self.name = name
#     def eat(self, food):
#         return f"{self.name} is enjoying the {food}"
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  #gives animal superclass it is same as Animal.__init__(name)
#         self.breed = breed
# # watson = Dog() #error because Dog inherit Animal
# watson = Dog("Watson", "Asasia")
# print(watson.name)
# print(watson.breed)
#polymorhism is different object transforming to differnt things e.g len method
# class Person():
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     def __len__(self):
#         return self.height


# values = [
#     "Boris",
#     [1, 2, 3],
#     [4, 5, 6 , 7],
#     {"a":1, "b":2},
#     Person("Boris", 71)
# ]

# for value in values:
#     print(len(value))
# import random
# class Player():
#     def __init__(self, games_played, victories):
#         self.games_played = games_played
#         self.victories = victories
#     @property
#     def win_ratio(self):
#         return self.victories / self.games_played
# class HumanPlayer(Player):
#     def make_move(self):
#         print("Let player make the decision!")
# class ComputerPlayer(Player):
#     def make_move(self):
#         print("Run algoruthm to calculate best move")
# hp = HumanPlayer(30, 15)
# cp = ComputerPlayer(1000, 999)
# print(hp.win_ratio)
# print(cp.win_ratio)

# game_players = [hp, cp]
# starting_player = random.choice(game_players)
# starting_player.make_move()
# class Nonesense():
#     def __init__(self):
#         self.__some_attribute = "Hello"
#     def __some_method(self):
#         print("This is coming from some_method")
# class SpecialNonsense(Nonesense):
#     pass

# n = Nonesense()
# sn = SpecialNonsense()
# print(n.__some_attribute) wont work because of __
# print(n.some_attribute)

# print(sn.__some_attribute)
# print(sn.__some_attribute)

# n.some_method()
# sn.__some_method()

#this will display it
# print(n._Nonesense__some_attribute)
# print(sn._Nonesense__some_attribute)
# n._Nonesense__some_method()
# n._Nonesense__some_method()
#multiple inheritance
# class FrozenFood():
#     def thaw(self, minutes):
#         print(f"Thawing for {minutes} minutes")
#     def store(self):
#         print("Putting in the freezer!")

# class Dessert():
#     def add_weight(self):
#         print("Putting on the pounds!")
#     def store(self):
#         print("Putting in d refrigerator")
# class IceCream(FrozenFood, Dessert):
#     pass

# ic = IceCream()
# ic.add_weight()
# ic.thaw(5)
# ic.store() #because frozen food is defined first python checks it firstly
# #mro is a class method that returns order of execution , MRO- METHOD RESOLUTION ORDER
# print(IceCream.mro())
# class Restaurant():
#     def make_reservation(self, party_size):
#         print(f"Booked a table for {party_size}")
# class Steakhouse(Restaurant):
#     pass
# class Bar():
#     def make_reservation(self, party_size):
#         print(f"Booked a lounge for {party_size}")
# class BarAndGrill(Steakhouse, Bar):
#     pass
# # print(BarAndGrill.mro())
# bag = BarAndGrill()
# bag.make_reservation(2) #by default python use depth for search
# class FilmMaker():
#     def give_interview(self):
#         print("I Love making movies!")
# class Director(FilmMaker):
#     pass
# class Screenwriter(FilmMaker):
#     def give_interview(self):
#         print("i love making scripts!")
# class JackOfAllTrades(Director, Screenwriter):
#     pass
# stallone = JackOfAllTrades()
# stallone.give_interview()
# print(JackOfAllTrades.mro()) #it still use the depth feature, but when python see two occurence of a class multiple times it deletes the earlier and keep the last one
# isinstance for checking if object is made from class
#issubclass for checking if class is a sub class of super class
#  
#     pass
# class Superhero(Person):
#     pass
# arnold = Person()
# boris = Superhero()

# print()
# print(isinstance(boris, Superhero))
# print(isinstance(boris, Person))

# print()

# print(isinstance(arnold, Person))
# print(isinstance(arnold, Superhero))
# print()
# print(issubclass(Superhero, Person))
# print(issubclass(Person, Superhero))
# # print(issubclass(Superhero, object))
# print(issubclass(Person, object))
#module 26
#exception handling is code that handle errors, code that runs when a program does not go as planned
#exception is a special object that python uses to mange errors during program execution
#traceback is a report of the execution that was raised
# def divide_five_by_number(n):
#     try:
#         calculation = 5 / n
#     except:#if the code in the try block did not run, this block will run
#         calculation = 5
#     return calculation

# print(divide_five_by_number(0))
# print(divide_five_by_number(10))
# print(divide_five_by_number("noff"))
# def divide_five_by_number(n):
#     try:
#         return 5 / n
#     except:#if the code in the try block did not run, this block will run
#         pass #this will return None

# print(divide_five_by_number(0))
# print(divide_five_by_number(10))
# print(divide_five_by_number("noff"))
# def divide_five_by_number(n):
#     try:
#         calculation = 5 / n
#     # except ZeroDivisionError:#if the code in the try block did not run, this block will run
#     #     return "You can't divide by zero"
#     # except TypeError as e:
#     #     return f"No dividing bt invalid objects! {e}"
#     except(ZeroDivisionError, TypeError) as e:
#         return f"Something Went wrong. The error was {e}"
    # return calculation

# print(divide_five_by_number(0))
# print(divide_five_by_number(10))
# print(divide_five_by_number("noff"))
#raise keyword is use to trigger specific exception
# def add_positive_numbers(a, b):
#     try:
#         if a <= 0 or b <= 0:
#             raise ValueError("one or both of the value is invalid")
#         return a + b
#     except ValueError as e:
#         return f"Caught the ValueError: {e}"

# print(add_positive_numbers(10, 5))
# print(add_positive_numbers(-2, 3))
# class NegativeNumbersError(Exception): #exception class is present in python
#     """One Or More Inputs are negative"""
#     pass
# def add_positive_numbers(a, b):
#     try:
#         if a <= 0 or b <= 0:
#             raise NegativeNumbersError
#     except NegativeNumbersError:
#         return f"Shame on you, not valid {NegativeNumbersError}"
# print(add_positive_numbers(-5, -2))
# class Mistake(Exception):
#     pass
# class StupidMistake(Mistake):
#     pass

# class SillyMistake(Mistake):
#     pass
# #stupidmistake and silly mistake are siblings of mistake
# try:
#     raise StupidMistake("Extra stupid mistake")
# except StupidMistake as g:
#     print(f"Caught the error: {g}")

# # try:
# #     raise StupidMistake("Extra Stupid Mistake")
# # except SillyMistake as e: #there will be error cause we didnt raise  
# #     print(f"Caught the error: {e}")
# try:
#     raise StupidMistake("Extra Stupid Mistake")
# except Mistake as e:  
#     print(f"Caught the error: {e}")
# try:
#     raise SillyMistake("Extra Silly Mistake")
# except Mistake as e:  
#     print(f"Caught the error: {e}")
# x = 10
# try:
#     print(x + 5)
# except NameError:
#     print("Some variable is not defined")
# else:#this will run when try runs i.e no exception
#     print("This will print if there is no error in the try")
# finally:#this will run no matter what
#     print("This will print with or without exception")
#date time module are immutable
# import datetime
# from datetime import date
# #date accept three argument year,month,day
# birthday = date(1991, 4, 12)
# print(birthday)
# print(type(birthday))
# moon_landing = date(year = 1969, month = 7, day = 20)
# print(moon_landing)
# # date(2025, 15, 10)
# print(birthday.year)
# # birthday.year = 2000 #this is not writeable
# today = date.today() #gives the present day date
# print(today)
# import datetime
# from datetime import time

# start = time()
# print(start)
# print(start.hour)
# print(start.minute)
# print(start.second)

# print(time(6))
# print(time(hour = 18))
# print(time(12, 25))
# print(time(hour = 12, minute = 25))

# #11:34:22pm
# print(time(23, 34, 22))
# print(time(hour = 23, minute = 34, second = 22))
# time(27)
# from datetime import datetime #import datetime is attribute from datetime module
# print(datetime(1999, 7, 24)) #for date and time
# print(1999, 7, 24, 14)
# print(1999, 7, 24, 14, 16)
# print(1999, 7, 24, 14, 16, 58)
# print(datetime(year = 1999, month = 7, day = 24, hour = 14, minute = 16, second = 58))
# today = datetime.today()
# print(today)
# print(datetime.now())
# print(today.now())
# print(today.second)
# print(today.weekday()) # it index from 0
# same_time_twenty_years_ago = today.replace(year = 1999)
# print(same_time_twenty_years_ago)

# same_time_in_january = today.replace(month = 1)
# print(same_time_in_january)
# from datetime import datetime
# today = datetime.today()
# print(today.strftime("%m")) #returns month as a tring
# print(type(today.strftime("m")))
# print(today.strftime("%m %d"))
# print(today.strftime("%m-%d-%Y"))
# print(today.strftime("%m %d"))
# print(today.strftime("%m %d"))
# print()
# print(today.strftime("%m/%d/%y"))
# print(today.strftime("%m-%d-%Y"))#y represent two digit number of year and Y rep 4 digit number

# print(today.strftime("%A")) #returns weekday name
# print(today.strftime("%B")) #returns month name
# from datetime import datetime, timedelta
# birthday = datetime(1991, 4, 12)
# today = datetime.now()
# my_life_span = today - birthday
# print(my_life_span)#is time delta object
# print(type(my_life_span)) 
# print(my_life_span.total_seconds()) #we are invoking on timedelta object
# five_hundred_days = timedelta(days = 500, hours = 12) #it dosent accept month or year
# print(five_hundred_days)
# print(five_hundred_days + five_hundred_days)
# print(today + five_hundred_days)
#module 28
#random module
# import random

# print(random.random()) #we have a random function within a random module
#it gives random number btw 0 and 1
# print(random.random() * 100 )
# print(random.randint(1, 5)) #random integer between 1 and 5(inclusive)
# print(random.randrange(0, 50, 10)) #0, 10 , 20, 40 #50 is exclusive
# import random
# print(random.choice(["Bob", "Moe", "Curly"])) #it will extract one value itself
# print(random.choice((1, 2, 3)))
# print(random.choice("elephant"))
# lottery_numbers = [random.randint(1, 50) for value in range(50)] 
# print(lottery_numbers)
# print(random.sample(lottery_numbers, 1))#takes iterable argument first, and number of value to return.it return a list
# print(random.sample(lottery_numbers, 6))
import random
import copy
#shuffle function accept mutable object
characters = ["Warrior", "Druid", "Hunter", "Rogue", "Mage"]
print(random.shuffle(characters)) #its return is none
print(characters) #it as shuffled the list
clone = characters[:]
clone = characters.copy()
clone = copy.copy(characters)
print(random.shuffle(clone)) #its return is none
print(clone)




# intro = "Hello World II"
# print(intro)
# intro = "Hello Python Instructor"
# print(intro)

# this line is to print out hello world
# print(len(intro)) # this line prints 
# print(intro)
# print(intro)
# print(intro)
# print(intro)


# age = input("Enter your age ")

# print("Your are currently " + age + " year old")


# score = input("Enter your score ")
# finalResult = float(score) + 20
# print("Your score plus your assessment is ")
# print(finalResult)


# fullText = "today is " + "Friday"
# # print(fullText)

# part1 = "I am coming"
# part2 = "today or tomorrow "
# part3 = 200

# fullSentence = part1 + " " + part2

# finalSen = fullSentence + str(part3)

# print(finalSen)

# print(part1 + part2)

# multiLineText = """
#    I am coding python
# we are doing well
# we are gradually covering up
# but we just started
#                 Thanks
# """
# print(multiLineText)

# textWord = "some text here is getting long"

# print(textWord[-4])

# ans = textWord[3:]
# print(ans)


# print("The number of characters here is " +  str(len(multiLineText)))
# print(f"The number of characters here is {part1} {part2} {part3}")

# print(textWord.upper())
# print(textWord.lower())
# print(textWord.capitalize())

# newList = textWord.split(" ")
# print(newList)

# print(5 == 3)

# print(bool(["Amaka", "David"]))

# print(4 < 2)

# num = 5
# num += 2
# num += 5
# num += 10

# print(num)

# The number of characters here is 113

# print("Hello world")
# number = 200

# names = ["David", "Excellent", 'Loveth', 100, 40, 5] #From database

# data = ["Ikenna", "Ada", 1000, 85, "Okolo"]

# print("Length " + str(len(data)))
# print(names)

# names[3:4] = [300, 100]
# names.extend(data)
# names.pop()

# print(names)
# print(names[1])

# for name in names:
#     name = str(name)
#     name = name.upper()
#     print(name)    
#     print("xyz")
#     print('.........')

# for x in names:
#     if isinstance(x, (str)):
#         x = x.upper()

#     print(x)
#     print("xyz")
#     print('.........')
# num = 100

# print(num)

# num = num + 20 # this line is incrementing the num varaible

# print(num)

# # this line is a list of items
# theList = ["orange", 'mango', 'banana', "gova", "cashwe"]

# aList = list(fruit)

# print(aList)
# print(moreFruit)

# some note 
# more notes

fruit1 = "mango"
fruit2 = 'orange'
num = 30

basket = ["mango", "orange", "gova", "cashew", "banana", "mango", "gova", "banana"]

answer = 20 + 30 * 4 / 2

# eating = basket[7]
# nebour = basket[2:6]

basket[1] = "book"

basket[6] = "bread"


# print(num + 20 * 2)
# print(fruit1)
# print(answer)
# print(basket)
# print(eating)
# print(nebour)

thislist = ["apple", "banana", "cherry"]

print(thislist[2])

thislist[2] = "Mango"

print(thislist[2])

fruits = ("apple", "banana", "cherry", "mango", "gova", "Casava")

print(fruits)

# (first, second, third, fourth,a,b ) = fruits

# print(range(len(fruits)))
# print(range(6))

# for item in fruits:
#     print(item)

# for item in range(len(fruits)):
#     print(fruits[item])

# for(let x = 0; x < fruits.length; x++){
#     print(fruits[x])
# }

fruits = {"first": "mango",
           "second": "bannana", 
           "third": "beans", 
           "fourth":"mango", 
           "fifth": {"one": "car", 
                     "others": {"abc": 1000}, 
                     "two": "house", 
                     "three": "money"
            },
            "sixth": [20, 40, "boy", "baby"]
}

fruitsAb = fruits.copy()

fruitsAb["abc"] = "Groundnut"

print(fruits)


fruits["first"] = "Gover"
print(fruits["fifth"]["others"]['abc'])
print(fruits['sixth'][2])


# print(fruits["first"])


myProps = fruits.keys()
myValues = fruits.values()
entries = fruits.items()
potOfBeans = fruits["third"]
changed = fruits.update({"second": "Oranges"})

# print((fruits))

# fruits["fifth"] = "Pawpaw"
# # fruits.pop('fourth')


# print(fruits)

# print(myValues)
# print(myProps)
# print(entries)
# print(potOfBeans)

# for x in fruits.items():
#     print(x)


item1 = 20
item2 = 30

if item1 < item2:
    print("It is greater")
    print("We are matching")
    print("Good job so far")
    if 2 < 5:
        print("wow we got inside the first if statement")
elif item1 > item2 and item1 < item2:
    print("It is geater")
    print("Another printout")
elif item1 >= item2:
    print("We have found the result")
else:
    value = 50 + 20
    print("It is not true")
    print(value)

print("Hello world")
# nums = [5, 2, 5, 2, 2]

# # using easy python way
# for num in nums:
#     print("x" * num)


# # using more traditional coding way
# print(" ")
# for num in nums:
#     output = ""
#     for inner in range(num):
#         output += "x"
#     print(output)

# nums = [2, 4, 1, 5, 1, 8, 3, 10, 5, 3, 10]

# # get the maximum number
# max = nums[0]
# for num in nums:
#     if num > max:
#         max = num
# print(max)

# for num in range(2, 30, 3):
#     for x in range(5):
#         print(num, x)
    
# else:
#     print("Finished")

# # remove duplicate
# unique = []
# for num in nums:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# # unpacking
# numbers = [20, 10, 5, 3, 60]
# x, y, z, a, b = numbers
# print(a)

# String, Arrays, Tuple and Dictionary is closely related
# word = "Igwekanma the God of my grand father will make me wealthy and powerful"

# if "my" not in word:
#     print("Present")
# else:
#     print("Its present")

# print(word[:])

b = "Hello, World!"
# print(b[-5:-2])
# print(word.upper())
# print(word.split(" "))
# print (f"I said {word} {5.0:.2f}")
word = "Igwekanma the God of my grand father will make me wealthy and powerful"

print(15/2)

# Collection Data types in python are
# list
# set
# tuple
# dictionary

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# thislist[3:5] = ["mango", "cashew", "tomatoes"]
# thislist.insert(3, "pinepple")
# thislist.sort()
# print(thislist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# print( list1 + list2)
# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(type(thisset))

# set1 = {"a", "b", "c", 4}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)
# print("that good") if "brand" in thisdict else print("not good")

names = ["David", "Excellent", 'Loveth', "Ijeoma", "Onyinye"] #From database

newNames = [name for name in names if name != "Ijeoma"]
print(newNames)
thislist = ["banana", "Orange", "Kiwi", "cherry"]

[a, b, *c] = thislist
print(c[0] + " Unpacked")

list2 = list(thislist)
list2.extend(thislist)
print(thislist)
print(list2)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple[0]))

x = ("apple", "banana", "cherry")
x = list(x)
x[1] = "kiwi"
x = tuple(x)

print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange","palm")
thistuple += y

# del thistuple

print(thistuple)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

nums3 = {"first": 1000, "second": 2000, "third": 3000}
iterate = iter(nums3)
print(next(iterate))
print(next(iterate))

def myfunc():
  global x
  x = 300

myfunc()

print(x)

import platform

x = platform.system()
print(x)

import datetime

x = datetime.datetime.now()

print(x.day)
print(x.strftime("%A"))

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=3, separators=(". ", " = "), sort_keys=True))
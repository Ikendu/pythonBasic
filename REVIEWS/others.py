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
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(type(thisset))

set1 = {"a", "b", "c", 4}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
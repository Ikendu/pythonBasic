nums = [5, 2, 5, 2, 2]

# using easy python way
for num in nums:
    print("x" * num)


# using more traditional coding way
print(" ")
for num in nums:
    output = ""
    for inner in range(num):
        output += "x"
    print(output)

nums = [2, 4, 1, 5, 1, 8, 3, 10, 5, 3, 10]

# get the maximum number
max = nums[0]
for num in nums:
    if num > max:
        max = num
print(max)

# remove duplicate
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)


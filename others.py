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

nums = [2, 4, 5, 1, 8, 10, 5, 3]

max = nums[0]
for num in nums:
    if num > max:
        max = num
print(max)


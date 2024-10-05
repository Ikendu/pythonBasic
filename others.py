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


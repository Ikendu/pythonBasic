
nums = {"first": 10, "second": 20, "third": 30}
nums1 = {"first": 100, "second": 200, "third": 300}
nums2 = {"first": 30, "second": 50, "third": 60}
nums3 = {"first": 1000, "second": 2000, "third": 3000}

# print(nums3["third"])


class Add:
    first = 10
    second = 20
    third = 30

    def __init__(self, a, b, c):
        self.num1 = a
        self.num2 = b
        self.num3 = c

nums = Add(20, 30, 40)
nums1 = Add(100, 200, 300)
nums2 = Add(30, 50, 60)
nums3 = Add(1000, 2000, 3000)

print(nums2.third)

# nums = Add(10, 20, 30)
# myObj = Add(100, 200, 50)
# obj2 = Add(30, 10, 50)


# print(myObj.num1)
# final = myObj.num2 + 50
# print(myObj.num3 + final)

# obj2.addition()


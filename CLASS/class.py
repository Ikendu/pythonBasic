
class Add:
    x = 10
    y = 20
    z = 30
    def __init__(self, a, b, c):
        self.num1 = a
        self.num2 = b
        self.num3 = c


nums = Add(10, 20, 30)
myObj = Add(100, 200, 50)
obj2 = Add(30, 10, 50)


print(myObj.num1)
final = myObj.num2 + 50
print(myObj.num3 + final)


from unittest import result


def showString() :
    print("This is coding")
    print("Its getting deep")
    print("Python is the easier")
    print("We are getting good at it")

showString()

def addScore(value, name):
    result = value + 30
    print(name + " scored " + str(result))

def myStudents(*student):
    print(f"first name is {student[0]}")
    print(f"second name is {student[1]}")
    print(f"third name is {student[2]}")
    print(f"last name is {student[-1]}")

addScore(49, "John Man")
addScore(50, "David")

myStudents('John', 'Mary', 'Mich', 'Juliet', 'Gift', 'Akuoma', 'Excel')

def addition(num1=10, num2=20):
    result = num1 + num2
    print(result)

addition(40, 20)

def multiply(num1, num2):
    print(num1 * num2)
    return num1 * num2

final = multiply(20, 40) + 100
print(final)

divider = lambda  a, b : a/b

myResult =  divider(100, 10) + 40

print(int(myResult))

def added(a):
    return lambda b: a + b

final = added(5)
print(final(10))



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
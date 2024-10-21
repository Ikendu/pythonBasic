try:
    age = int(input("Enter your age: "))
    print(age)
    number = 2000
    result = number / age
    print(result)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Age cannot be zero")    



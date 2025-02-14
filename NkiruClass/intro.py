# print("Hello New to Coding")
# print("I am learning Python")

# the description of my car
# we just start python today 30-01-2025
# Intoduction

# myCar = "Toyota Camry"
# myCarYear = 2015
# numStr = "2030"
# myNum = 34.5

# sum = str(myCarYear) + numStr
# sum1 = myCarYear + int(numStr)



# print(type(myCar))
# print(type(myCarYear))
# print(type(myNum))
# myPro = myCar + " House"

# print(myCar)
# print(myCarYear)
# print(numStr)
# print(sum)
# print(sum1)

"""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

myStr = "hello world consectetur adipiscing elit,sed do eivhjjjfghjghjh fhjgffg fgjfghjfgj fjnfghjfgjfgjfgfd hthfgjgfhjusmod tempor incididuntut labore et dolore magna aliqu"
myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","apple", "banana", "cherry", "orange", "kiwi", "melon", "mango",]

# print(myStr)
# print(myStr[1])
# print(myStr[2:7])
# print(myStr[-3])

# print(myList)
# print(myList[0])
# print(myList[:], "ghfghfh")
# print(myList[-3])

# strLenght = len(myStr)
# listLenght = len(myList)
# print(strLenght)
# print(listLenght)


# for x in myList:
#     print(x)

# if "world" in myStr:
#     print("Yes, 'world' is present in the following sentence")
#     print("We are ready")    
# else:
#     print("No, 'world' is not present in the following sentence")

button = "blue" 

if button == "blue":
    print("Start the car")
elif button == "green":
    print("On the AC")  
    print("On the AC")  
elif button == "pink":
    print("On the Television")
elif button == "black":
    print("On the Radio")    
elif button == "red":
    print("Stop the car")
else: 
    print("the car is parked")   


thislist = ["apple", "banana", "cherry", "Mangoes"]
tropical = ["mango", "pineapple", "papaya"]
# print(thislist)
# thislist[0] = "Mellon"
# thislist[1] = "Orange"
# thislist.append("Pineapple")
thislist.append("Grapes")
thislist.insert(3, "Strawberry")
tropical.extend(thislist)
# thislist.pop(2)
# thislist.clear()
# print(thislist)

thislist = ["apple", "banana", "cherry", "Mangoes"]
newList = []
# print(newList)

# for x in thislist:
#     if 'e' in x:
#         print(x)
#     else:
#         # print("No e in " + x)    

# for x in thislist:
#     if 'a' in x:
#         newList.append(x)

# print(newList)  
# newList =[ x for x in thislist if 'a' in x]      
# print(myPro)

serverItems = ("appleii", "bananaii", "cherryii", "orangeii", "kiwiii", "melonii", "mangoii", "orangeii", "kiwiii", "melonii", "mangoii")
# print(thistuple[-2])
# print(len(thistuple))

myNewList = list(serverItems)

# print(myNewList)

myNewList.append('Kokonut')
myNewList.append('Amalala')

# print(myNewList)

# myNewTuppleItems = tuple(myNewList)

# print(myNewTuppleItems)

thislist = ["apple", "banana", "cherry", "Mangoes"]

for x in myNewList:
    thislist.append(x)


# print(thislist)

# copyList = []
# copyList = thislist.copy()

# print("From COPYLIST", copyList)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
# print(tuple3)

# print(serverItems.count("orangeii"))

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("bananas")

# print(thisset)

def myPrintFunction(exc):
    print(f"I am {exc} here")
    print(f"I am {exc} here")
    print(f"I am {exc} here")
    print(f"I am {exc} here")


# myPrintFunction('Jugging')


mySet = {"apple", "banana", "cherry", "Mangoes"}
mySet1 = {"apple", "banana", "cherry", "Mangoes", "MoiMoi"}
mySet.add("newItem")
diff = mySet1.difference(mySet)
# print(diff)

myList = ["apple", "banana", "cherry", "Mangoes"]
myDict = {
    "first":"apple", 
    "sec": {
        "one":"banana", 
        "two": "Palm", 
        "three": {
            "part1": "eye",
            "part2": "nose"
        }
        }, 
    "third": [
        "red", 
        "white", 
        "blue", [
            "hello", 
            "hi",
            'come']], 
    "fourth":"Mangoes"
    }
# myList[1] = "Orange"
# myDict.update({"sec":"Orange"})
# myDict["sec"] = "Orangessss"
# myPrintFunction("Running")
# print(myList[0])
# print(myDict.get("sesc", "Please the prop is not avaible"))
# print(myDict["sec"]["one"])


idx = 0
# while idx <= 10:
#     print("jgnhjfogjofghjdu", idx)
#     if idx == 5:
#         print('We have reached level 5')
#     elif idx == 7:
#         print("Wow we are now in level 7")
#         break
#     elif idx == 9:
#         print("We are now penultimate") 
    
#     idx += 1

# myPrintFunction("Walking")

# while idx <= 10:
#     print("jgnhjfogjofghjdu", idx)
#     idx += 1 
#     if idx == 5:
#         print('We have reached level 5')
#     elif idx == 7:
#         print("Wow we are now in level 7")
        
#     elif idx == 9:
#         print("We are now penultimate") 
    
# print("Out of while loop")

# myArray =["obi", 'ada', 'chike', 'oge']

# for i in myArray:
#     print(i)

# for zzzz in range(10):
#     print(zzzz)


# myPrintFunction("Sitting")

mySchool = 'UNN'

def university(str): 
  print(str)
  print(str)


university('University of Nigeria')
university('Digital Dream')

def work(num1, num2):
    result = num1 + num2
    finalResult = result * 10
    output = finalResult / 2
    return [output]

arrResult = work(10, 20)
arrResult.append(1000)

result = work(20, 30)

print(result)
print(arrResult)

myfunc = lambda num1, num2: num1 + num2


print(myfunc(2, 3))

obj = {"name": "Bean", "shape": "Circle", "color": "White"}

# print(obj["shape"])

# class CakeClass:
#     name = 'chocolate'
#     color = "White"
#     shape = "Triangle"


# myCake1 = CakeClass()
# myCake2 = CakeClass()

# print(myCake1.name)

class Cake:
    def __init__(self, name, color, shape):
        self.name = name
        self.color = color
        self.shape = shape


    def __str__(self):
        return f"the name is {self.name}, The color is {self.color}, with a shape of {self.shape}"
    
    def show(self):
        return f" {self.name} {self.color}  {self.shape} "
    



weddingCake = Cake("Debreeze", "Sky Blue", "Tower" )
# print(weddingCake)
print(weddingCake)


birthDay = Cake("Vintage", "Redish White", "Circle")
print(birthDay.show())

cake1 = Cake("Pawpaw", "Yello White", "Elips")
cake2 = Cake("Vintage", "Redish blue", "Rectanle")
cake3 = Cake("Buns", "Pink", "Squre")
cake4 = Cake("Elukiti", "Pink White", "Star")

# print(cake4)

cake1 = {"name": "Bean", "shape": "Circle", "color": "White"}
cake1 = {"name": "Bean", "shape": "Circle", "color": "White"}


nums = {"first": 10, "second": 20, "third": 30}
nums1 = {"first": 100, "second": 200, "third": 300}
nums2 = {"first": 30, "second": 50, "third": 60}
nums3 = {"first": 1000, "second": 2000, "third": 3000}

# print(nums3["third"])


class Add:
    first = 10
    second = 20
    third = 30

    def __init__(right, a, b, c):
        right.a = a
        right.b = b
        right.c = c
    
    def add(self):
        result = self.a + self.b + self.c
        # print(result)
        return result
    
    def shouting(self):
        print("Hello my good friend")



nums = Add(20, 30, 40)
nums1 = Add(100, 200, 300)
nums2 = Add(30, 50, 60)
nums3 = Add(1000, 2000, 3000)

print(nums2.shouting())
print(nums2.add())


# nums = Add(10, 20, 30)
# myObj = Add(100, 200, 50)
# obj2 = Add(30, 10, 50)


# print(myObj.num1)
# final = myObj.num2 + 50
# print(myObj.num3 + final)

# obj2.addition()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Candidate(Person):
   def __init__(self, fname, lname, address):
      super().__init__(fname, lname)
      self.address = address

   def reverse(self):
      print(self.lastname, self.firstname)


student1 = Person("Ada", "Adaja")
student2 = Candidate("Obi", 'Obinna', "Oppo UNN gate")

student1.printname()
# student1.reverse()
student2.printname()
student2.reverse()
print(student2.address)

listItems = ["chair", 'bed', 'table', 'cup', 'curtine']

getter = iter(listItems)

print(next(getter))
print(next(getter))
print(next(getter))
print(next(getter))
print(next(getter))

num = 50
num2 = 100

def show(): 
   xy = 40  
   print(num + num2, xy)

   def moreShow():
      global yz
      yz = 100
      print(yz, xy, num, num2)
      
   print(num, num2, xy)

   return moreShow()
 


show()

print(num + num2)
print(yz)

# import  function
import index
from function import multiply
import datetime

multiply(30, 20)

print(index.intro)
print(index.items[0])

time = datetime.datetime.now()
print(time.second)




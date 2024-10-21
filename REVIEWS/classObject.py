# Class can have method inside and attributes attach to objects created from the class

class Point:
    def __init__(self, value1, value2):
        self.x = value1
        self.y = value2
        print(f"Ponit x is {self.x} and point y is {self.y}")


    def show(self):
        print("This is a point")
    def exit(self):
        print("Exiting right now...")


point1 = Point(20, 25)
point1.show()
point1.exit()

point1.more = "More wealth coming..."
log = point1.more
print(log)

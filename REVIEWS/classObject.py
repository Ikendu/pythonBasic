# Class can have method inside and attributes attach to objects created from the class

class Point:
    def show(self):
        print("This is a point")
    def exit(self):
        print("Exiting right now...")


point1 = Point()
point1.show()
point1.exit()
point1.more = "More wealth coming..."
log = point1.more
print(log)

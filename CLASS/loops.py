# x = 1
# while x <= 6:
#     print(f"{x} is less than 6")
#     x += 1

# print(p1)
# value = int(input("Enter a value "))
# while value != 10:
#     print("You failed")
#     print("Try again")
#     value = int(input('Enter a value '))
# else:
#    print("You won")


# value = int(input("Enter a value "))
# value = 0
# while value < 10:
#     value += 1       
#     if value == 6:
#         continue
#     print(value)

    
for x in ["banana", "chery", 'gover', 'mango']:
  print(x)
  if(x == 'gover'):
     break

for x in range(5, 10, 2):
   value = 10
   print(value + x)

color = ['black', 'blue', 'red', 'green', 'yellow']
cars = ['lexus', 'innoson', 'lambo', 'toyota']

for x in color:
   for y in cars:
      print(x, y)
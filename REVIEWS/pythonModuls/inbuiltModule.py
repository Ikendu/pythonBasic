import random

# for num in range(5):
#     print(random.randint(20, 50))


class Dice:
    def roll(self):
        print(random.randint(1, 5), random.randint(1, 5))

    
roller1 = Dice()
roller1.roll()    
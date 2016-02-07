class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0
cat = Cat()
cat.name = "Spot"
cat.color = "black"
cat.weight = 16

class Monster():
    def __init__(self):
        self.name = ""
        self.health = 0

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            print ("The monster died.")
        
        

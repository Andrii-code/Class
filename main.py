class Creature:
    def __init__(self,name,power,health,speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed
    def specific(self):
        print("name =", self.name)
        print("power =", self.power)
        print("health =", self.health)
        print("speed =", self.speed)
class Animals(Creature):
    def __init__(self, name, power, health, speed):
        super().__init__(name, power, health, speed)
    def Flying(self):
        print("Не літає")

elf = Creature("Ельф", 3, 10, 10)
elf.specific()
dwarf = Creature("Гном", 6, 15, 3)
dwarf.specific()
man = Creature("Людина",5,12,8)
man.specific()
dog = Animals("Лабрадор", 5 , 7, 17)
dog.specific()
dog.Flying()
"""
we need oop to resolve comp lexity and don have to write so much of a code and it also makes modification easy rathr than pop

it works in object so easy to modify
works on real world basis
"""

class Character:

    def __init__(self, name, health, attack, blood):#if i want to add more like blood
        self.name = name
        self.health = health
        self.attack = attack
        self.blood = blood#modify here

    def attack_enemy(self):
        print(f'{self.name} attack with power {self.attack}{self.blood}') #and here  

warrior = Character('thor',100,50)
mage = Character('gandalf',80,70)
archer = Character('archer',80,90)

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy()


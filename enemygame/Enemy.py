class Enemy:
    def __init__(self, type_enemy,health,attack):
        self.type_enemy=type_enemy
        self.health=health
        self.attack=attack
        

    def talk(self):
        print(f"I am an Enemy {self.type_enemy}, Be prepared to Engage in combat  ")

    def walk(self):
        print(f"The {self.type_enemy} is moving closer")

    def attack_(self):
        print(f"the {self.type_enemy} will attack with {self.attack} power")

    def spl_attack(self):
        print(f"the {self.type_enemy} cannot use thier special attack yet")
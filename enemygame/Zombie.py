from Enemy import *
import random
class Zombie(Enemy):
    def __init__(self,health,attack):
        super().__init__(type_enemy="Zombie",health=health,attack=attack)

    def talk(self):
        print("....grumbling....")

    #def attack_(self):
        #print(f"The {self.type_enemy} will kill you with his {self.attack} damage and eat your brain")
         
    def spl_attack(self):
        print(f"the {self.type_enemy} attacks with {self.attack} power")
        did_spl_attack_work = random.random() < 0.5
        if did_spl_attack_work:
            self.health +=2
            print("special move: zombie gets (+2HP)")
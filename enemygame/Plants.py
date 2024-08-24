from Enemy import *
import random
class Plants(Enemy):
    def __init__(self,  health, attack):
        super().__init__(type_enemy="Plants", health=health, attack=attack)

    def talk(self):
        print("...tuchhhh...tuchhhh...tuchhhh...")

    def spl_attack(self):
        print(f"We {self.type_enemy} shoot multiple peas at the enemy with {self.attack} Power")
        did_spl_attack_work = random.random() < 0.25
        if did_spl_attack_work:
            
            self.attack+=5
            print("Special attack: Plant shoots bigger peas (+5 AP)")
            

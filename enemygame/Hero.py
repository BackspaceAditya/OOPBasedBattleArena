from Weapon import *
class Hero:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
        self.is_weapon_equipped = False
        self.weapon : Weapon = None

    def talk(self):
        print("I the Mighty Hero of Humanity will End your kind right Here and now")

    def weapon_equip(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack += self.weapon.attack_increase
            self.is_weapon_equipped = True
            

    def attack_(self):
        print(f"Hero attacks for {self.attack} damage")       
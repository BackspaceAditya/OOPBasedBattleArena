from Enemy import *
from Zombie import *
from Plants import *
from Hero import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health and e2.health>0: 
        print("-----------------------------------")
        e1.spl_attack()
        e2.spl_attack()
        print(f"{e1.type_enemy} : {e1.health} HP left")
        print(f"{e2.type_enemy} : {e2.health} HP Left")
        e2.attack_()
        e1.health -= e2.attack
        e1.attack_()
        e2.health-= e1.attack

    print("---------------------")

    if e1.health>0:
        print((f"{e1.type_enemy} wins!"))

    else:
        print(f"{e2.type_enemy} wins!")

def hero_battle(hero: Hero, enemy: Enemy):
    hero.talk()
    enemy.talk()

    while hero.health and enemy.health>0: 
        print("-----------------------------------")
        enemy.spl_attack()
        print(f"Hero Health : {hero.health} HP left")
        print(f"{enemy.type_enemy} : {enemy.health} HP Left")
        enemy.attack_()
        hero.health -= enemy.attack
        hero.attack_()
        enemy.health-= hero.attack

    print("---------------------")

    if hero.health>0:
        print("Hero wins!")

    else:
        print(f"{enemy.type_enemy} wins!")


zombie = Zombie(500, 5)
plant = Plants(32, 16)
hero = Hero(32,20)
weapon = Weapon("Sword", 10)
hero.weapon= weapon
hero.weapon_equip()

hero_battle(hero, plant)

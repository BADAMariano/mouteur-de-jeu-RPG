import random
from bloc3 import *

def combat(player, enemy):
    print(f"\n=== COMBAT : {player.name} vs {enemy.name} ===")

    while player.is_alive() and enemy.is_alive():

        print(f"\n{player.name} HP:{player.hp} | {enemy.name} HP:{enemy.hp}")
        print("1. Attaquer")
        print("2. Se soigner")
        print("3. Fuir")

        choix = input("Choix : ")

        # JOUEUR
        if choix == "1":
            dmg = player.deal_damage()
            enemy.take_damage(dmg)
            print(f"{player.name} inflige {dmg} dégâts")

        elif choix == "2":
            player.hp += 15
            print(f"{player.name} se soigne +15 HP")

        elif choix == "3":
            print("Tu fuis !")
            return

        else:
            print("Choix invalide")
            continue

        # ENNEMI MORT ?
        if not enemy.is_alive():
            print(f"\n🏆 {enemy.name} est vaincu !")
            player.gain_xp(enemy.xp_reward)
            break

        # TOUR ENNEMI
        dmg = enemy.deal_damage()
        player.take_damage(dmg)
        print(f"{enemy.name} attaque {dmg} dégâts")

        # JOUEUR MORT ?
        if not player.is_alive():
            print("\nTu es mort...")
            break

    # RESULTAT FINAL
    print("\n=== FIN DU COMBAT ===")

    if player.is_alive():
        print(f" Vainqueur : {player.name}")
    else:
        print(f" Vainqueur : {enemy.name}")


player = Player("Héros")
enemy = Enemy("Gobelin", 50, 15, 5, 50)

combat(player, enemy)
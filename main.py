from bloc2 import combat
from bloc3 import Player, Enemy
from bloc4 import sauvegarder, charger

print("=== MENU ===")
print("1. Nouvelle partie")
print("2. charger partie")

choix = input("choix :")

if choix =="1":
    player = Player("Héros")

elif choix =="2":
    player = charger()

else:
    player = Player("Héros")

    enemy = Enemy("Gobelin", 50, 15, 5, 50,)

    combat(player, enemy)

    # sauvegarde après combat
    sauvegarder(player)


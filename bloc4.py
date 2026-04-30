import json
from bloc3 import Player

def sauvegarder(player):
    data = {
        "name": player.name,
        "hp": player.hp,
        "attack": player.attack,
        "defense": player.defense,
        "xp": player.xp,
        "level": player.level,
        #"inventory": player.inventory,
    
    } 
    with open("save.json","w") as f:
        json.dump(data,f)
        print("Partie sauvegardée !")

def charger():
    try:
        with open("save.json","r") as f:
            data = json.load(f)

            player = Player(data["name"])
            player.hp = data["hp"]
            player.attack = data["attack"]
            player.defense = data["defense"]
            player.xp = data["level"]
           # player.inventory = data["inventory"]

            print("Partie chargée !") 
            return player
        
    except FileNotFoundError:
        print("Aucune sauverge trouvée")
    return Player("Héros")
import tkinter as tk
import random
from bloc3 import Player, Enemy

player = Player("Héros")
score = 0
cooldown = 0

def get_rank():
    if score < 3:
        return " Bronze"
    elif score < 6:
        return " Silver"
    else:
        return "$ Gold"

def new_enemy():
    global score
    if score % 3 == 2:
        return Enemy(" BOSS", 120, 25, 10, 100)
    return random.choice([
        Enemy("Gobelin", 50, 15, 5, 50),
        Enemy("Orc", 80, 20, 8, 80),
        Enemy("Squelette", 40, 18, 3, 40)
    ])

enemy = new_enemy()

# --- UI UPDATE ---
def update_ui():
    hp_player.set(f"{player.name}  {player.hp} | Niveau {player.level}")
    hp_enemy.set(f"{enemy.name}  {enemy.hp}")
    score_text.set(f" Score : {score} | Rang : {get_rank()}")

# --- ACTIONS ---
def attack():
    global enemy, score, cooldown

    dmg = player.deal_damage()
    enemy.take_damage(dmg)
    log.set(f" {dmg} dégâts")

    cooldown = max(0, cooldown - 1)

    if not enemy.is_alive():
        win()
        return

    enemy_turn()
    update_ui()

def special():
    global cooldown

    if cooldown > 0:
        log.set(f" Attaque spéciale dispo dans {cooldown} tours")
        return

    dmg = random.randint(20, 40)
    enemy.take_damage(dmg)
    log.set(f" ATTAQUE SPÉCIALE {dmg} dégâts !")

    cooldown = 3

    if not enemy.is_alive():
        win()
        return

    enemy_turn()
    update_ui()

def heal():
    player.hp = min(player.hp + 15, 100)
    log.set(" +15 HP")

    enemy_turn()
    update_ui()

def enemy_turn():
    if enemy.is_alive():
        dmg = enemy.deal_damage()
        player.take_damage(dmg)
        log.set(f" {enemy.name} inflige {dmg}")

        if not player.is_alive():
            log.set(" GAME OVER")
            disable()

def win():
    global score
    score += 1
    player.gain_xp(enemy.xp_reward)
    log.set(f" {enemy.name} vaincu !")
    next_btn.pack()
    disable()
    update_ui()

def next_fight():
    global enemy
    enemy = new_enemy()
    log.set(" Nouveau combat !")
    next_btn.pack_forget()
    enable()
    update_ui()

def disable():
    btn_attack.config(state="disabled")
    btn_heal.config(state="disabled")
    btn_special.config(state="disabled")

def enable():
    btn_attack.config(state="normal")
    btn_heal.config(state="normal")
    btn_special.config(state="normal")

# --- UI ---
root = tk.Tk()
root.title(" RPG ULTIME ")

hp_player = tk.StringVar()
hp_enemy = tk.StringVar()
log = tk.StringVar()
score_text = tk.StringVar()

tk.Label(root, textvariable=hp_player, font=("Arial", 14)).pack()
tk.Label(root, textvariable=hp_enemy, font=("Arial", 14)).pack()
tk.Label(root, textvariable=score_text, font=("Arial", 12)).pack()

tk.Label(root, textvariable=log).pack(pady=10)

btn_attack = tk.Button(root, text=" Attaquer", command=attack)
btn_attack.pack(pady=5)

btn_special = tk.Button(root, text=" Spéciale", command=special)
btn_special.pack(pady=5)

btn_heal = tk.Button(root, text=" Soigner", command=heal)
btn_heal.pack(pady=5)

next_btn = tk.Button(root, text=" Combat suivant", command=next_fight)

update_ui()
root.mainloop()
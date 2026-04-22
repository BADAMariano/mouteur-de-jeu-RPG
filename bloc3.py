import random

      
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)

    def deal_damage(self):
        return random.randint(5, self.attack)


class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20, 10)
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gagne {amount} XP")
        if self.xp >= 100:
            self.xp = 0
            self.hp += 20
            self.attack += 5
            print(f"{self.name} level up !")


class Enemy(Character):
    def __init__(self, name, hp, attack, defense, xp_reward):
        super().__init__(name, hp, attack, defense)
        self.xp_reward = xp_reward
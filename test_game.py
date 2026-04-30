from bloc3 import Player, Enemy
def test_enemy_take_damage():
    player = Player("Test")
    enemy = Enemy("Gobelin", 50, 15, 5, 50)

    enemy.take_damage(20)
    
    assert enemy.hp < 50
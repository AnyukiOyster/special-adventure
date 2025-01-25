import random
import time

class Character:
    def __init__(self, type, hp: int, base_damage: int):
        self.type = type
        self.hp = hp
        self.base_damage = base_damage

    def __str__(self):
        return f"Здоровье: {self.hp}. Урон: {self.base_damage}"

    def attack(self, target):
        throw = random.randint(1, 10)  # Бросок атаки
        target_throw = random.randint(1, 10)  # Бросок защиты
        damage = self.base_damage
        print(f"{self.type} замахивается... 🎯")
        time.sleep(1)
        if throw == 10:  # Критическая атака, враг не может её отразить
            damage = int(damage * 1.5)  # Модификатор критического урона
            print(f"⚔ {self.type} проводит КРИТИЧЕСКУЮ АТАКУ и наносит {damage} ед. урона!")
        elif throw > target_throw:  # Обычная атака
            print(f"⚔ {self.type} атакует и наносит {damage} ед. урона.")
        else:
            print(f"🛡 {target.type} отражает атаку!")
            damage = 0

        # Уменьшаем здоровье цели противника (но не ниже 0)
        target.hp = max(0, target.hp - damage)

player1=Character('Герой', 50, 10)
enemy1 = Character("Враг", 50, 10)

# Бросок на инициативу
player_turn = random.randint(1, 10)
enemy_turn = random.randint(1, 10)

print("\n🎲 Бросок инициативы:")
time.sleep(1)
print(f"Герой выбросил: {player_turn}, враг выбросил: {enemy_turn}")
time.sleep(0.20)
if player_turn >= enemy_turn:
    first, second = player1, enemy1
else:
    first, second = enemy1, player1
print(f"\n⚔ {first.type} начинает атаку!\n")

while player1.hp > 0 and enemy1.hp > 0:
    if player_turn >= enemy_turn:
        print('Ход героя:')
        time.sleep(1)
        player1.attack(enemy1)
        if enemy1.hp > 0:  # Если враг ещё жив
            print("\nХод врага:")
            time.sleep(1)
            enemy1.attack(player1)
        else:
            time.sleep(1)
            break
    else:
        print('Ход врага:')
        time.sleep(1)
        enemy1.attack(player1)
        if player1.hp > 0:  # Если игрок ещё жив
            print("\nХод героя:")
            time.sleep(1)
            player1.attack(enemy1)
        else:
            time.sleep(1)
            break

    # Выводим текущее состояние здоровья
    time.sleep(1)
    if player1.hp > 0 and enemy1.hp > 0:
        print(f"\n{player1.type}: осталось {player1.hp} ед. здоровья")
        if 20 > player1.hp:
            print("   ⚠ Герой еле держится на ногах!")
        time.sleep(1)
        print(f"{enemy1.type}: осталось {enemy1.hp} ед. здоровья")
        if 20 > enemy1.hp:
            print("   ⚠ Враг тяжело ранен!")
        print("-" * 30)
        time.sleep(1)

# Результат боя
if enemy1.hp <= 0:
    print("Вы победили!")
else:
    print("Герой был повержен... Начать приключение заново?")
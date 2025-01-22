class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} кг)"  # Сведения о предмете


class Inventory:
    def __init__(self):
        self.equipment = []
        self.max_total_weight = 50

    def add_item(self, item):
        total_weight = self.get_total_weight() + item.weight
        #Проверка общего веса предметов в инвентаре с учётом нового предмета
        if total_weight > self.max_total_weight:
            print(f"{item.name} — предмет нельзя добавить в инвентарь: слишком большой вес.")
        else:
            self.equipment.append(item)

    def delete_item(self, item):
        for d in self.equipment:
            if d.name == item.name:  # Ищем предмет по названию
                self.equipment.remove(d)
                break

    def get_total_weight(self): #Метод подсчёта общего веса всех преметов в инвентаре
        return sum(item.weight for item in self.equipment)


sword = Item("Меч", 5)
potion = Item("Зелье", 1)
shield = Item("Щит", 7)

inventory = Inventory()
inventory.add_item(sword)
inventory.add_item(potion)
inventory.add_item(shield)

print(f"Общий вес: {inventory.get_total_weight()} кг")
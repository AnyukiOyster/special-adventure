ACHIEVEMENT_DATA = {
    "Воин": {"description": "Убей 10 врагов", "goal": 10},
    "Путешественник": {"description": "Исследуй 5 новых локаций", "goal": 5},
    "Богач": {"description": "Собери 1000 золотых", "goal": 1000},
}

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.achievements = {}  # Словарь, который содержит {название: объект Achievement}

    def __str__(self):
        return f"{self.name}. Класс: {self.role}"

    def add_achievement(self, achievement):
        # Добавляет достижение в словарь, если игрок его ещё не выполняет.
        if achievement.name not in self.achievements:
            self.achievements[achievement.name] = achievement

    def update_achievement(self, achievement_name, progress):
        # Обновляет прогресс достижения. Если достижение не было начато, добавляет его в словарь пользователя.
        if achievement_name not in self.achievements:
            # Получаем описание и цель из базы данных
            achievement_info = ACHIEVEMENT_DATA.get(achievement_name)
            if achievement_info:
                description = achievement_info["description"]
                goal = achievement_info["goal"]
            else:
                description = "Нет информации о достижении"
                goal = 9999  # Значение по умолчанию
            achievement = Achievement(achievement_name, description, goal)
            self.add_achievement(achievement)

        achievement = self.achievements[achievement_name]
        achievement.update_progress(progress)

    def show_achievements(self):
        # Выводит список достижений игрока.
        for achievement in self.achievements.values():
            print(f"Достижение «{achievement.name}» {achievement.status}\n"
                  f"Прогресс: {achievement.progress}/{achievement.goal}")

class Achievement:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.progress = 0
        self.status = 'не получено'

    def update_progress(self, value):
        # Обновляет прогресс достижения.
        if self.status == 'не получено':
            self.status = 'выполняется'
        self.progress += value
        if self.progress >= self.goal:
            self.progress = self.goal
            self.status = 'получено!'


player = Player("Алиса", "разбойник")

player.update_achievement("Воин", 5)
player.update_achievement("Богач", 500)
player.update_achievement("Воин", 5)  # Должно засчитать достижение
player.show_achievements()
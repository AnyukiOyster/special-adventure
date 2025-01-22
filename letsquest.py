from datetime import datetime, timedelta

class Quest:
    def __init__(self, name, description, status='не начато', reward='50 монет'):
        self.name = name
        self.description = description
        self.status = status
        self.reward = reward
        self.success = ''
        self.deadline = None

    def __str__(self):
        return f"Задание «{self.name}»\n{self.description}\nСтатус: {self.status}\n"

    def start(self):
        if self.status == 'не начато':
            self.status = 'выполняется'
            self.deadline = datetime.now() + timedelta(hours=3)  # Начинаем отсчёт времени на выполнение квеста

    def complete(self):
        if not self.deadline:
            return
        self.status = 'завершено'
        if datetime.now() > self.deadline:
            self.success = 'провалено (время истекло)'
        else:
            self.success = f'выполнено! Награда: {self.reward}'

    def fail(self):
        if self.deadline and datetime.now() > self.deadline:
            self.status = 'завершено'
            self.success = 'провалено (время истекло)'


class QuestLog:
    def __init__(self):
        self.journal = []

    def add_quest(self, quest):
        self.journal.append(quest)

    def check_deadlines(self):
        for quest in self.journal:
            if quest.status == 'выполняется':
                quest.fail()

    def show_quests(self):
        self.check_deadlines()
        for quest in self.journal:
            if quest.status == 'выполняется':
                print(f"Задание «{quest.name}» {quest.status}")
            elif quest.status == 'завершено':
                print(f"Задание «{quest.name}» {quest.success}")


quest1 = Quest("Спасти принцессу", "Найти и спасти принцессу из замка.")
quest2 = Quest("Собрать 10 ягод", "Соберите 10 ягод для зелья.")

log = QuestLog()
log.add_quest(quest1)
log.add_quest(quest2)

quest1.start()
quest2.start()
quest2.complete()

log.show_quests()
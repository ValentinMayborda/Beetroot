"""
Розробіть клас TaskManager, який представляє собою колекцію завдань.
Він повинен мати:
● Протектед атрибут _counter для відстеження ідентифікаторів завдань.
● Словник tasks для зберігання завдань, де кожне завдання має опис та пріоритет.
-----------------------------------------------------------------------------------------------

●Перевантаження наступних операторів:

Перевантаження наступних операторів:
○ __len__: повертає кількість завдань.
○ __getitem__: повертає завдання за його ключем.
○ __setitem__: додає нове завдання за вказаним ключем.
○ __iter__: ітерація по завданнях в порядку спадання пріоритету.
○ __contains__: перевірка наявності завдання за ключем.

● Метод add_task для додавання нового завдання з описом і пріоритетом, який повертає
ідентифікатор нового завдання.
"""


class TaskManager:
    def __init__(self):
        self._counter = 0
        self.tasks = {}

    def add(self, description, priority):
        self._counter += 1
        self.tasks[self._counter] = {'description': description, 'priority': priority}
        return self._counter

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, key):
        return self.tasks[key]

    def __setitem__(self, key, value):
        if not isinstance(value, dict) or 'priority' not in value or 'description' not in value:
            raise ValueError('Помилка наявності')

        self.tasks[key] = value

    def __iter__(self):
        return iter(sorted(self.tasks.items(), key=lambda x: x[1]['priority'], reverse=True))

    def __contains__(self, key):
        return key in self.tasks


t = TaskManager()

t.add('Сходиди в магазин', 3)
t.add('Спорт зал', 1)
t.add('Прання', 2)

print(len(t))
print(t[2])
t[2] = {'description': 'Відпочити', 'priority': 5}
print(t[2])

for task_id, task in t:
    print(f'Id :{task_id}, text priority: {task['priority']}, Description {task['description']}')

print(1 in t)
print(5 in t)

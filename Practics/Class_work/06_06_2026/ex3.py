"""Реалізуйте функції: додати задачу (автоінкремент id),
 позначити виконаною за id,
зберегти/завантажити список задач у JSON
1: Підготувати
2: Зробити щось""" #CRUD

import json

def load_tasks(filename):
    try:
        with open(filename,'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as err:
        return []

def add_task(tasks, title,):
    next_id = max((task['id'] for task in tasks))+1

    tasks.append({'id': next_id, 'title': title, 'done' : False})
    return next_id

def save_tasks(filename, tasks):
    with open(filename,'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def complited_tasks(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return True

        print(task_id)

    return False


tasks = load_tasks('jsonfile.json')
add_task(tasks, 'Купити квіти')
task_id = add_task(tasks, 'Повторити тему словників')
complited_tasks(tasks, task_id)
save_tasks('jsonfile.json', tasks)





import sqlite3
import random

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# task_categories = ["gamedev", "coding", "chores", "homework", "books", "podcasts",
#     "compsci", "games", "purchases", "productivity", "data_analysis","gameengine",
#     "tasks"]

category_and_file = {
    "gamedev":"gamedev_tasks.pickle",
    "books":"programming_books.pickle",
    "gameengine":"termina_game_engine.pickle",
    "courses":"coding_courses.pickle",
    "coding":"js_python_tasks.pickle"
}

def create_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    # create a table
    c.execute("""CREATE TABLE tasks (
        task_name TEXT,
        deadline TEXT,
        category TEXT,
        completed INTEGER,
        difficulty INTEGER,
        important INTEGER,
        urgent INTEGER,
        passionate INTEGER,
        task_id INTEGER
    )""")    

    # Have to commit our command
    conn.commit()

    # Close our connection (best practice)
    conn.close()

def push_task(name, deadline, category, completed, difficulty, important, urgent, passionate):
    task_id=random.randint(1,100000)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?,?)", (name, deadline, category, completed, difficulty, important, urgent, passionate, task_id))
    conn.commit()
    conn.close()

def show_all_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall() # returns array of task items (tuple objects)
    
    print(f"{Fore.BLACK}{Back.GREEN}task\t\t\t\tDEADLINE\tCOMPLETED\tCATEGORY\tID")
    for task in tasks:
        if len(task[0]) <= 20:
            print(f'{Fore.GREEN}"{task[0]}"\t\t{task[1]}\t\t{task[3]}\t{task[2]}\t\t{task[8]}\t\timportant:{task[5]}\t\turgent:{task[6]}\t\tpassionate:{task[7]}\t\t')
        else:
            print(f'{Fore.GREEN}"{task[0]}"\t{task[1]}\t\t{task[3]}\t{task[2]}\t\t{task[8]}\t\timportant:{task[5]}\t\turgent:{task[6]}\t\tpassionate:{task[7]}\t\t')


    conn.commit()
    conn.close()

def remove_all_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("DELETE from tasks")
    tasks = c.fetchall()
    conn.commit()
    conn.close()

def remove_task(name, id='optional'):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE task_name = (?)", [name])
    yesorno = input(f"Are you sure you want to delete task? [yes or no]: {c.fetchall()}")
    if "yes" in yesorno:
        c.execute("DELETE from tasks WHERE task_name = (?)", [name])
    conn.commit()
    conn.close()


def get_all_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.commit()
    conn.close()
    return tasks

def get_tasks(category):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE category = (?)", [category])
    tasks = c.fetchall()
    conn.commit()
    conn.close()
    return tasks

def get_task(name, id='optional'):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE task_name LIKE (?)", [name])
    task = c.fetchall()
    conn.commit()
    conn.close()
    return task


def check_task(name):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("""
    UPDATE tasks SET completed = 1
    WHERE task_name = (?)""", [name])
    conn.commit()
    conn.close()

def mark_task_important(name):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("""
    UPDATE tasks SET important = 1
    WHERE task_name LIKE (?)""", [name])
    conn.commit()
    conn.close()

def mark_task_urgent(name):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("""
    UPDATE tasks SET urgent = 1
    WHERE task_name LIKE (?)""", [name])
    conn.commit()
    conn.close()


def import_legacy_tasks_data():
    for category in category_and_file:
        print(f"category: {category}\t\tassociated file: {category_and_file[category]}")
            
        inputfile = f'old/{category_and_file[category]}'
        
        oldlist = tasklist()
        oldlist.load_data(inputfile)
        for task in oldlist.tasklist:
            # print(task.name, "  within category: ", category)
            push_task(task.name, "12/30/2021", category, 0, 2, 0, 0, 0,)
            # print(task)


# create_table()

# import_legacy_tasks_data()

print(get_all_tasks())
# show_all_tasks()

# remove_all_tasks()


show_all_tasks()
# # print(get_tasks('coding'))
# print(get_task("castlevania clone"))
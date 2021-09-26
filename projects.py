# for importing legacy data format
import pickle

import sqlite3
import random

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# task_categories = ["gamedev", "coding", "chores", "homework", "books", "podcasts",
#     "compsci", "games", "purchases", "productivity", "data_analysis","gameengine",
#     "projects"]

category_and_file = {
    "gamedev":"gamedev_projects.pickle",
    "books":"programming_books.pickle",
    "gameengine":"termina_game_engine.pickle",
    "courses":"coding_courses.pickle",
    "coding":"js_python_projects.pickle"
}

# ==OLD CODE FOR IMPORTING OLD DATA TO BE FORMATTED=================================================

class Project():
    def __init__(self, name, deadline, checked=0):
        self.name = name
        self.deadline = deadline
        self.checked = checked

        id = randint(0, 9999)
        self.project_id = id
    
    def needsCompleted(self):
        if self.checked == 0:
            return u_checkbox_empty
        else:
            return u_checkbox_full
        
    def __str__(self):
        return f"projects.Project object | {self.name}, {self.deadline}, {self.checked}, end of string"

class ProjectList():
    def __init__(self, name="default_projects_list_object"):
        self.name = name
        self.projectlist = []

    def save_data(self, outputfile=''):
        """
        leave outputfile alone for default settings
        """
        if outputfile == '':
            outputfile = f'old/{self.name}.pickle'
        else:
            outputfile = "old/" + outputfile + ".pickle"
        # save array data
        print("save function in projects, ", self.name, " to ", outputfile)
        filestorage = open(outputfile, "wb")
        pickle.dump(self.projectlist, filestorage)
        filestorage.close()

    def load_data(self, inputfile=''):
        """
        leave inputfile alone for default settings
        """
        if inputfile == '':
            inputfile = f'data/{self.name}.pickle'
        # load array data
        try:
            print("load function in projects, ", self.name, " from ", inputfile)
            loadinstorage = open(inputfile, "rb")
            self.projectlist = pickle.load(loadinstorage)
            loadinstorage.close()
        except:
            self.save_data()
        # make sure to add this try-except statement, and to close the handler when done loading/saving.



# ======================================================

### NEW CODE

def create_table():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    # create a table
    c.execute("""CREATE TABLE projects (
        project_name TEXT,
        deadline TEXT,
        category TEXT,
        completed INTEGER,
        difficulty INTEGER,
        important INTEGER,
        urgent INTEGER,
        passionate INTEGER,
        project_id INTEGER
    )""")    

    # Have to commit our command
    conn.commit()

    # Close our connection (best practice)
    conn.close()

def push_project(name, deadline, category, completed, difficulty, important, urgent, passionate):
    project_id=random.randint(1,100000)
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("INSERT INTO projects VALUES (?,?,?,?,?,?,?,?,?)", (name, deadline, category, completed, difficulty, important, urgent, passionate, project_id))
    conn.commit()
    conn.close()

def show_all_projects():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM projects")
    projects = c.fetchall() # returns array of project items (tuple objects)
    
    print(f"{Fore.BLACK}{Back.GREEN}PROJECT\t\t\t\tDEADLINE\tCOMPLETED\tCATEGORY\tID")
    for project in projects:
        if len(project[0]) <= 20:
            print(f'{Fore.GREEN}"{project[0]}"\t\t{project[1]}\t\t{project[3]}\t{project[2]}\t\t{project[8]}\t\timportant:{project[5]}\t\turgent:{project[6]}\t\tpassionate:{project[7]}\t\t')
        else:
            print(f'{Fore.GREEN}"{project[0]}"\t{project[1]}\t\t{project[3]}\t{project[2]}\t\t{project[8]}\t\timportant:{project[5]}\t\turgent:{project[6]}\t\tpassionate:{project[7]}\t\t')


    conn.commit()
    conn.close()

def show_projects(category):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM projects WHERE category like (?)", [category])
    projects = c.fetchall() # returns array of project items (tuple objects)
    
    print(f"{Fore.BLACK}{Back.GREEN}PROJECT\t\t\t\tDEADLINE\tCOMPLETED\tCATEGORY\tID")
    for project in projects:
        if len(project[0]) <= 12:
            print(f'{Fore.GREEN}"{project[0]}"\t\t\t{project[1]}\t\t{project[3]}\t{project[2]}\t\t{project[8]}\t\timportant:{project[5]}\t\turgent:{project[6]}\t\tpassionate:{project[7]}\t\t')
        elif len(project[0]) <= 20:
            print(f'{Fore.GREEN}"{project[0]}"\t\t{project[1]}\t\t{project[3]}\t{project[2]}\t\t{project[8]}\t\timportant:{project[5]}\t\turgent:{project[6]}\t\tpassionate:{project[7]}\t\t')
        else:
            print(f'{Fore.GREEN}"{project[0]}"\t\t{project[1]}\t\t{project[3]}\t{project[2]}\t\t{project[8]}\t\timportant:{project[5]}\t\turgent:{project[6]}\t\tpassionate:{project[7]}\t\t')

            # if len(project.name) <= 14:
            #     print(f'{Fore.GREEN}"{project.name}"\t\t\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')
            # elif len(project.name) <= 20:
            #     print(f'{Fore.GREEN}"{project.name}"\t\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')
            # elif len(project.name) <= 24:
            #     print(f'{Fore.GREEN}"{project.name}"\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')
            # elif len(project.name) <= 50:
            #     print(f'{Fore.GREEN}"{project.name}"\n\t\t\t\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')

    conn.commit()
    conn.close()

def remove_all_projects():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("DELETE from projects")
    projects = c.fetchall()
    conn.commit()
    conn.close()

def remove_project(name, id='optional'):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM projects WHERE project_name = (?)", [name])
    yesorno = input(f"Are you sure you want to delete project? [yes or no]: {c.fetchall()}")
    if "yes" in yesorno:
        c.execute("DELETE from projects WHERE project_name = (?)", [name])
    conn.commit()
    conn.close()


def get_all_projects():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM projects")
    projects = c.fetchall()
    conn.commit()
    conn.close()
    return projects

def get_projects(category):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM projects WHERE category = (?)", [category])
    projects = c.fetchall()
    conn.commit()
    conn.close()
    return projects

def get_project(name, id='optional'):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM projects WHERE project_name LIKE (?)", [name])
    project = c.fetchall()
    conn.commit()
    conn.close()
    return project


def check_project(name):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("""
    UPDATE projects SET completed = 1
    WHERE project_name = (?)""", [name])
    conn.commit()
    conn.close()

def mark_project_important(name):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("""
    UPDATE projects SET important = 1
    WHERE project_name LIKE (?)""", [name])
    conn.commit()
    conn.close()

def mark_project_urgent(name):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("""
    UPDATE projects SET urgent = 1
    WHERE project_name LIKE (?)""", [name])
    conn.commit()
    conn.close()

def mark_project_as_passion_project(name):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("""
    UPDATE projects SET passionate = 1
    WHERE project_name LIKE (?)""", [name])
    conn.commit()
    conn.close()

def import_legacy_projects_data():
    for category in category_and_file:
        print(f"category: {category}\t\tassociated file: {category_and_file[category]}")
            
        inputfile = f'old/{category_and_file[category]}'
        
        oldlist = ProjectList()
        oldlist.load_data(inputfile)
        for project in oldlist.projectlist:
            # print(project.name, "  within category: ", category)
            push_project(project.name, "12/30/2021", category, 0, 2, 0, 0, 0,)
            # print(project)


# create_table()

# import_legacy_projects_data()

print(get_all_projects())
# show_all_projects()
# mark_project_important("megaman style platformer")
# mark_project_as_passion_project("megaman style platformer")

# print(get_project("megaman style platformer"))

# show_projects("gamedev")

# show_projects('books')

# remove_all_projects()
# push_project('task manager app','9/30/2021','coding',0,2,1,1,1)
# push_project('modular GUI tkinter','9/30/2021','coding',0,2,1,1,1)
# push_project('code sudoku game + solver','9/30/2021','gamedev',0,2,1,1,1)
# push_project('castlevania clone','9/30/2021','gamedev',0,2,1,1,1)

# # show_all_projects()
# # print(get_projects('coding'))
# print(get_project("castlevania clone"))

# check_project("castlevania clone")


# show_projects('gamedev')

# show_projects('coding')
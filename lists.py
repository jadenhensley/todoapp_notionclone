# for loading/saving data to files.
import pickle
# for generating id's
from random import randint
# for colored text in terminal
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
# checkbox icons
from formats import u_checkbox_empty, u_checkbox_full
# for iterating id's possibly
import itertools

# currentid = open(f'data/projectid.pickle', "rb")
# id = pickle.load(currentid)
# print(id)

# todo
# 
# potential problem: need to consider how we are doing the ID system for each task
# if we are using multiple lists, probably don't want to be still counting up.
#
# since we set it to 0 at beginning of file, will be awkward when reloading lists from files
#  and may mess up our functionality
#

class Task:
    def __init__(self, name, checked=0):
        self.name = name
        self.checked = checked

        id = randint(0, 9999)
        self.task_id = id
    
    def needsCompleted(self):
        if self.checked == 0:
            return u_checkbox_empty
        else:
            return u_checkbox_full

class Todo:
    def __init__(self, name="default_todo_list_object"):
        self.name = name
        self.todolist = []

    def save_data(self, outputfile=''):
        """
        leave outputfile alone for default settings
        """
        if outputfile == '':
            outputfile = f'data/{self.name}.pickle'
        else:
            outputfile = "data/" + outputfile + ".pickle"

        print("save function in lists, ", self.name, " to ", outputfile)
        filestorage = open(outputfile, "wb")
        pickle.dump(self.todolist, filestorage)
        filestorage.close()

    def load_data(self, inputfile=''):
        """
        leave inputfile alone for default settings
        """
        if inputfile == '':
            inputfile = f'data/{self.name}.pickle'
        else:
            inputfile = "data/" + inputfile + ".pickle"

        # try:
        print("load function in lists, ", self.name, " from ", inputfile)
        loadinstorage = open(inputfile, "rb")
        self.todolist = pickle.load(loadinstorage)
        loadinstorage.close()
        # except:
        #     self.save_data()

        # make sure to add this try-except statement, and to close the handler when done loading/saving.
    
    def push_task(self, task):
        self.todolist.append(Task(task))


    def check_task(self, task_id):
        for task in self.todolist:
            if str(task.task_id) == str(task_id):
                if task.checked == 0:
                    task.checked = 1
                elif task.checked == 1:
                    task.checked = 0

    def remove_task(self, task_id):
        for task in self.todolist:
            if str(task.task_id) == str(task_id):
                self.todolist.remove(task)

    def remove_all(self):
        self.todolist = []

    def show(self):
        # print(f'\ndisplaying tasks from list "{self.name}"')
        print(f"{Fore.BLACK}{Back.GREEN}TASK\t\t\t\t\t\tCOMPLETED\t\tID")
        for task in self.todolist:
            if len(task.name) <= 14: # helps format nicely.
                print(f'{Fore.GREEN}"{task.name}"\t\t\t\t\t\t{task.needsCompleted()}\t\t{task.task_id}')
            elif len(task.name) <= 20:
                print(f'{Fore.GREEN}"{task.name}"\t\t\t\t\t{task.needsCompleted()}\t\t{task.task_id}')
            elif len(task.name) <= 40:
                print(f'{Fore.GREEN}"{task.name}"\t\t\t\t{task.needsCompleted()}\t\t{task.task_id}')



# try:
#     todolist.load_data()
# except:
#     todolist.save_data()

def show_todolist():
    todolist = Todo()
    todolist.load_data()
    todolist.show()

def add_task(task_name):
    todolist = Todo()
    todolist.load_data()
    todolist.push_task(task_name)
    todolist.save_data()

def remove_task(task_id):
    todolist = Todo()
    todolist.load_data()
    todolist.remove_task(task_id)
    todolist.save_data()

def remove_all():
    todolist = Todo()
    todolist.load_data()
    todolist.remove_all()
    todolist.save_data()

def check_uncheck_task(task_id):
    todolist = Todo()
    todolist.load_data()
    todolist.check_task(task_id)
    todolist.save_data()


def save_todolist_data(outputfile="todolist_backup"):
    todolist = Todo()
    todolist.load_data()
    todolist.save_data(outputfile)

def load_todolist_data(inputfile="todolist_backup"):
    todolist = Todo()
    todolist.load_data(inputfile)
    todolist.save_data() # note that we do not provide a parameter. This means that our backup is saved to the current "cache".

# for accessing from GUI modules
def get_todolist_data():
    todolist = Todo()
    todolist.load_data()
    return todolist.todolist

def get_todolist_ids():
    todolist = Todo()
    todolist.load_data()
    id_array = []
    for task in todolist.todolist:
        id_array.append(task.task_id)
    return id_array


if __name__ == "__main__":
    show_todolist()
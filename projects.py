# for loading/saving data to files.
import pickle
# import our parent classes
from lists import *
# from lists import Task, Todo
from weather import current_time

from formats import u_checkbox_empty, u_checkbox_full

# putting our "monthly projects" task category as a subclass of "todo" in a separate file

# todo
#
# we need to make sure the deadline that is inputted is acceptable
#   - should also be doing with other initializations of objects that use variables have right types and format


# note: we inherit from Task and import from lists, but I do not see any real need for this, its safer to keep it separate.
class Project(Task):
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

# alongside our projects having deadlines, we
#  need to have desktop push notifications and google calendar scheduling that updates
# automatically for us. This is what makes a "Project" different from standard "Todo" or "Habit"

# Habit: similar to Project in that it is scheduled, and Todo in that it has checkboxes,
# but recurrs daily, has daily notification, and has multiple checkboxes (depending on the need)

# Will also implement Habits in a separate file with similar functionality

# todo:
#
# scheduling and calendar

class ProjectList():
    def __init__(self, name="default_projects_list_object"):
        self.name = name
        self.projectlist = []

    def save_data(self, outputfile=''):
        """
        leave outputfile alone for default settings
        """
        if outputfile == '':
            outputfile = f'data/{self.name}.pickle'
        else:
            outputfile = "data/" + outputfile + ".pickle"
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
        else:
            inputfile = "data/" + inputfile + ".pickle"
        # load array data
        try:
            print("load function in projects, ", self.name, " from ", inputfile)
            loadinstorage = open(inputfile, "rb")
            self.projectlist = pickle.load(loadinstorage)
            loadinstorage.close()
        except:
            self.save_data()
        # make sure to add this try-except statement, and to close the handler when done loading/saving.
        
    
    def push_project(self, project, deadline=f"{current_time.tm_mon}/30/{current_time.tm_year}"):
        self.projectlist.append(Project(project, deadline))


    def check_project(self, project_id):
        for project in self.projectlist:
            if str(project.project_id) == str(project_id):
                if project.checked == 0:
                    project.checked = 1
                elif project.checked == 1:
                    project.checked = 0

    def remove_project(self, project_id):
        # del self.todolist[task]
        for project in self.projectlist:
            if str(project.project_id) == str(project_id):
                self.projectlist.remove(project)

    def remove_all(self):
        self.projectlist = []

    def show(self):
        # print(f'\ndisplaying tasks from list "{self.name}"')
        print(f"{Fore.BLACK}{Back.GREEN}PROJECT\t\t\t\tDEADLINE\tCOMPLETED\t\tID")
        for project in self.projectlist:
            if len(project.name) <= 14:
                print(f'{Fore.GREEN}"{project.name}"\t\t\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')
            elif len(project.name) <= 20:
                print(f'{Fore.GREEN}"{project.name}"\t\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')
            elif len(project.name) <= 24:
                print(f'{Fore.GREEN}"{project.name}"\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')
            elif len(project.name) <= 50:
                print(f'{Fore.GREEN}"{project.name}"\n\t\t\t\t{project.deadline}\t\t{project.needsCompleted()}\t\t{project.project_id}')
            


def show_projects():
    projects = ProjectList()
    projects.load_data()
    projects.show()

def add_project(project_name):
    projects = ProjectList()
    projects.load_data()
    projects.push_project(project_name)
    projects.save_data()

def remove_project(project_id):
    projects = ProjectList()
    projects.load_data()
    projects.remove_project(project_id)
    projects.save_data()

def remove_all():
    projects = ProjectList()
    projects.load_data()
    projects.remove_all()
    projects.save_data()

def check_uncheck_project(project_id):
    projects = ProjectList()
    projects.load_data()
    projects.check_project(project_id)
    projects.save_data()

def save_projects_data(outputfile="projectslist_backup"):
    projects = ProjectList()
    projects.load_data()
    projects.save_data(outputfile)

def load_projects_data(inputfile="projectslist_backup"):
    projects = ProjectList()
    projects.load_data(inputfile)
    projects.save_data() # note that we do not provide a parameter. This means that our backup is saved to the current "cache".

# for accessing from GUI modules
def get_projects_data():
    projects = ProjectList()
    projects.load_data()
    return projects.projectlist

def get_projects_ids():
    projects = ProjectList()
    projects.load_data()
    id_array = []
    for project in projects.projectlist:
        id_array.append(project.project_id)
    return id_array

if __name__ == "__main__":
    show_projects()
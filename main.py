# for loading/saving data to files.
import pickle
# for generating id's
from random import randint
# for getting weather and temp from an API
import weather
# for getting motivational, or philosophical quotes for inspiration.
import quotes
# for getting local time
import time
# for all things related to todo lists or projects
import tasks, projects
# for deep-copying data / sequence objects
from copy import deepcopy
# for colored text in terminal
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
# formatted text fields for each category label
from formats import weather_label, dailyquote_label, dailyhabits_label, todolist_label, helpstring, monthlyprojects_label
# different formatted unicode symbols for terminal output
from formats import u_checkbox_empty, u_checkbox_full, u_moon, u_sun, u_clouds, u_umbrella
# system-related functions, including terminal arguments
import sys
import getopt
# for running multiple modules in parallel, i.e. multiprocessing
from multiprocessing import Process
# for our GUI
import GUI

# TO-DO: load in color theme from file then use associated variable names.
# put these variables in the formats.py module!
color_quote = Fore.GREEN

def output_dashboard():
    print(f"\n")
    output_weather()
    output_quote()
    output_todo()
    output_projects()
    output_habits()





    # a = Process(target=lists.show_todolist())




    # lists.show_todolist()

    # projects.show_projects()

    # print(dailyhabits_label)

    # print(monthlyprojects_label)

def output_weather():
    print(weather_label)
    print(weather.getLocalTime())
    print(weather.getLocalWeather())

def output_quote():
    print(dailyquote_label, f"{color_quote}\n{quotes.getDailyQuote()}")

def output_todo():
    print(todolist_label)

def output_projects():
    print(monthlyprojects_label)
    projects.show_all_projects()

def output_habits():
    pass

def main(argv):
    # use this for debugging arguments

    # for i, argument in enumerate(argv):
    #     print(i, argument)
    if len(argv) == 0:
        print("no command arguments provided. use 'help' for more info.")
        exit()
    else:
        if argv[0] == "show":
            if len(argv) >= 2:
                if argv[1] in "todo":
                    output_todo()
                elif argv[1] in "projects":
                    output_projects()
                elif argv[1] in "habits":
                    output_habits()
                elif argv[1] in "weather":
                    output_weather()
                elif argv[1] in "quotes":
                    output_quote()
                elif argv[1] in "all":
                    output_dashboard()
            else:
                output_dashboard()
        elif argv[0] == "help":
            print(helpstring)
        elif argv[0] == "add":
            if len(argv) >= 4: # 4 arguments provided (remember that we still access from base0 indices in code)
                if argv[1] == "to":
                    if argv[2] in "todo": # using 'in' instead of '==' keyword allows for ciscoIOS-style argument input
                        print(f"{argv[3:]}")
                        for argument in argv[3:]:
                            if type(argument) is str:
                                print(f"adding {argument} to todo list.")
                                tasks.push_task(argument, "today", "etc", 0, 1, 1, 0, 0)
                    elif argv[2] in "projects":
                        print(f"{argv[3:]}")
                        for argument in argv[3:]:
                            if type(argument) is str:
                                print(f"adding {argument} to projects list.")
                                projects.push_project(argument, "11/30/2021", "etc", 0, 2, 1, 0, 0)
                    elif argv[2] in "habits":
                        print(f"adding {argv[3]} to habit tracker.")
                    else:
                        print("\n* ERROR: invalid input.\n* SYNTAX:  add to [ todo | projects | habits ]  [ task | (project, deadline) | (habit, frequency) ]")

            else:
                print("SYNTAX:  add to [ todo | projects | habits ]  [ task | (project, deadline) | (habit, frequency) ]")
        elif argv[0] == "check":
            if len(argv) >= 3:
                if argv[1] in "todo":
                    print(f"{argv[2:]}")
                    for argument in argv[2:]:
                        if type(int(argument)) is int:
                            print(f"checking off {argument} in todo list.")
                            tasks.check_task(argument)
                if argv[1] in "projects":
                    # print(f"checking off item in projects list with ID {argv[2]}")
                    # projects.check_uncheck_project(argv[2])
                    print(f"{argv[2:]}")
                    for argument in argv[2:]:
                        if type(int(argument)) is int:
                            print(f"checking off {argument} in projects list.")
                            projects.check_project(argument)
                if argv[1] in "habits":
                    print(f"checking off item in habit tracker with ID {argv[2]}")
                else:
                    print("SYNTAX:  check [ todo | projects | habits ]  [ name ]")
            else:
                print("SYNTAX:  check [ todo | projects | habits ]  [ name ]")


        elif argv[0] == "remove":
            if len(argv) >= 4:
                if argv[1] == "from":
                    if argv[2] in "todo":
                        print(f"removing {argv[3]} from todo list.")
                        if argv[3] == "all":
                            tasks.remove_all_tasks()
                        else:
                            print(f"{argv[3:]}")
                            for argument in argv[3:]:
                                if type(int(argument)) is int:
                                    print(f"removing {argument} from todo list.")
                                    tasks.remove_task(argument)
                    elif argv[2] in "projects":
                        print(f"removing {argv[3]} from projects list.")
                        if argv[3] == "all":
                            projects.remove_all_projects()
                        else:
                            print(f"{argv[3:]}")
                            for argument in argv[3:]:
                                if type(int(argument)) is int:
                                    print(f"removing {argument} from projects list.")
                                    projects.remove_project(argument)
                    elif argv[2] in "habits":
                        print(f"removing {argv[3]} from habit tracker.")
                    else:
                        print("\n* ERROR: invalid input.\n* SYNTAX:  remove from [ todo | projects | habits ]  [ name ]\n\t * itemID is listed by show commandm, can include multiple arguments")
            print("\n* SYNTAX:  remove from [ todo | projects | habits ]  [ name ]\n\t * itemID is listed by show command, can include multiple arguments")
                
        elif argv[0] == "mynameis":
            if len(argv) >= 2:
                username = argv[1]
                filestorage = open("config/username.pickle", "wb")
                pickle.dump(username, filestorage)
                filestorage.close()
            else:
                print("please tell me your name :-)")
        
        elif argv[0].lower() == "gui":
            if len(argv) == 1:
                GUI.gui_main()
            elif len(argv) >= 2:
                GUI.set_projects_category(argv[1])
                GUI.gui_main()

        elif argv[0] == "deadlines":
            tempidarray = projects.get_projects_ids()
            for id in tempidarray:
                projects.change_project_deadline(id, "10/30/2021")



        else:
            print("invalid argument. use 'help' for more info.")

if __name__ == "__main__":
    main(sys.argv[1:])

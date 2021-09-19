# for colored text in terminal
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# unicode symbols
u_checkbox_empty = "\u25A1"
u_checkbox_full = "\u25A0"
u_sun = "\u263C"
u_moon = "\u263D"
u_clouds = "\u2601"
u_umbrella = "\u2602"



# category labels
weather_label = f"{Back.BLUE}{Fore.YELLOW}-         TIME / WEATHER DATA           -{Back.BLACK}\n"
dailyquote_label = f"{Back.GREEN}{Fore.BLACK}-            DAILY QUOTE                -{Back.BLACK}\n"
todolist_label = f"{Back.RED}-              TODO LIST                -{Back.BLACK}\n"
dailyhabits_label = f"{Back.MAGENTA}-            DAILY HABITS               -{Back.BLACK}\n"
monthlyprojects_label = f"{Back.MAGENTA}-        MONTHLY PROJECTS               -{Back.BLACK}\n"


# commands / help string
helpstring = "Notes app, coded by @jadenhensley on github. \
\nUSAGE: Notes [command] [value|option|file] \
\n\nCOMMANDS \
\n\n\tshow  [ all | todo | projects | habits | weather | quote ]\n\t\tShows specified data in terminal \
\n\n\tadd to [ todo | projects | habits ]  [ task | (project, deadline) | (habit, frequency) ]\n\t\tAdds given task, project, or habit to the todo, projects, or habits list \
\n\tcheck [ todo | projects | habits ]  [ itemID ]\n\t\tChecks off an item from the indicated list (can also uncheck) \
\n\n\tremove from [ todo | projects | habits ]  [ itemID ] \n\t\tRemoves given task, project, or habit from the todo, projects, or habits list \
\n\n\tsave/load   [ todo | projects | habits ]  [ output-file-name (default=\"...lists_backup\")]\n\t\tSave or Load a list's data to/from a file."

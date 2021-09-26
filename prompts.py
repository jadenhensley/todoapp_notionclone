import json
tasks = []


mode = 'input'

def show_categories():
    f = open('./task_categories.json')
    data = json.load(f)
    categories = data
    for category in categories:
        print(category)
    f.close()


def print_tasks():
    for task in tasks:
        print(task)

subgoals_arr = []

def yesorno(task_property):
    return 1 if task_property in "yes" else 0

def prompt_task_input(maingoal="", mode='maininput'):
    while mode == 'maininput':
        task = str(input("+ "))
        if task == 'q':
            return 0
        elif task =='done':
            # print_tasks()
            return 0
        else:
            difficulty = str(input("rate this tasks difficulty [0-boring, 1-easy, 2-challenging, 3-hard]: "))
            passionate = yesorno(str(input("are you passionate about doing this [y or n]: ")))
            important = yesorno(str(input("is this task important [y or n]: ")))
            urgent = yesorno(str(input("is this task urgent [y or n]: ")))

            if difficulty >= "2":
                has_sub_goals = yesorno(input("is this task difficult enough such that it needs splitten up into smaller tasks/goals? [y or n]"))
                if has_sub_goals:
                    subgoals = prompt_task_input(task, 'subgoals')
                tasks.append({task: {'difficulty': int(difficulty), 'passion': passionate, 'important': important,
                'urgent': urgent, 'subgoals': subgoals}})
            # tasks[task] = difficulty
            else:
                tasks.append({task: {'difficulty': int(difficulty), 'passion': passionate, 'important': important,
                'urgent': urgent}})
                

    subgoals_arr = []
    

    while mode == 'subgoals':
        subgoal = str(input(f"enter subgoal for achieving {maingoal} + "))
        if subgoal == 'q':
            return 0
        elif subgoal =='done':
            # print_tasks()
            # mode == 'maininput'
            return subgoals_arr
        else:
            difficulty = str(input("rate this subgoal's difficulty [0-boring, 1-easy, 2-challenging, 3-hard]: "))
            subgoals_arr.append({subgoal: {'difficulty': int(difficulty)}})
            

def main():
    print("AVAILABLE CATEGORIES")
    show_categories()
    print("What tasks do you plan on doing? Enter: add new task  'done' to submit,'q' to quit.")
    prompt_task_input()
    print_tasks()
    
main()
import csv
import colorama
from colorama import Fore
u_checkbox_empty = "\u25A1"
u_checkbox_full = "\u25A0"


def show_habit_grid():
    with open('./habits_trackbydate.csv') as f:
        reader = csv.reader(f, delimiter=',')
        print("HABITS CONSISTENCY")
        for i, row in enumerate(reader):
            if (i != 0):
                if row[1] == "0":
                    print(f"{Fore.GREEN}{u_checkbox_empty}", end=' ')
                if row[1] == "1":
                    print(f"{Fore.GREEN}{u_checkbox_full}", end=' ')
                if i % 7 == 0:
                    print() # new
                if i % 30 == 0:
                    break # limit to first 30 days, think of this as a month.

show_habit_grid()
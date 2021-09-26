import csv
# import json
u_checkbox_empty = "\u25A1"
u_checkbox_full = "\u25A0"


def show_hours_spent_per_day():
    totalhrs_python = 0
    totalhrs_cplusplus = 0
    totalhrs_projects = 0
    totalhrs_webdev = 0
    totalhrs_gamedev = 0
    totalhrs_uiuxdesign = 0
    totalhrs_compsci = 0
    totalhrs_coding = 0

    with open('./daily_hours_data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader):
            if i != 0:
                print(row[1], "hours in", row[0], "on", row[2])
                if row[0] == "python":
                    totalhrs_python += int(row[1])
                    totalhrs_coding += int(row[1])
                elif row[0] == "coding":
                    totalhrs_coding += int(row[1])
    print(totalhrs_python, "total hrs python found in daily log")
    # print(totalhrs_, "total hrs python")
    # print(totalhrs_, "total hrs python")
    # print(totalhrs_coding, "total hrs coding as a whole")

def show_hours_spent_total():
    with open('./total_hours_data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader):
            if (i != 0) and (row[1] != "0"):
                print(row[1] + "+ hours total committed to knowledge in ", row[0])

def show_habit_grid():
    with open('./habits_trackbydate.csv') as f:
        reader = csv.reader(f, delimiter=',')
        print("HABITS CONSISTENCY")
        for i, row in enumerate(reader):
            if (i != 0):
                if row[1] == "0":
                    print(u_checkbox_empty, end=' ')
                if row[1] == "1":
                    print(u_checkbox_full, end=' ')
                if i % 7 == 0:
                    print() # new
                if i % 30 == 0:
                    break # limit to first 30 days, think of this as a month.

show_habit_grid()


# show_hours_spent_per_day()
# show_hours_spent_total()

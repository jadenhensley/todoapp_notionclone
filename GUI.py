# for GUI
import tkinter as tk
from tkinter import *
# for images
from PIL import ImageTk, Image
# import our lists modules to be read
import projects, lists
# for weather, time
import weather
# lets randomize our banner on startup :)
from random import randint
# for saving / loading in data
import pickle
# allows us to load in theme preferences from config/theme.json
import theme
# allows us to display inspiring quotes
import quotes
# for manipulating gui in real time (important for our use case)
import time

# plan on allowing user to provide wallpaper, for now this just works.
banners = ["media/banner/woodcuts_1.jpg","media/banner/woodcuts_2.jpg","media/banner/woodcuts_3.jpg","media/banner/woodcuts_4.jpg", "media/banner/nasa_the_blue_marble.jpg"]
selected_art = banners[randint(0, len(banners)-1)]

# load in the user's name, to display a friendly message in sidebar

count = 0


username = ""
try:
    loadinstorage = open("config/username.pickle", "rb")
    username = pickle.load(loadinstorage)
    print(username)
    loadinstorage.close()
except:
    print('could not load username')


# our actual functions need to be defined after
# the gui_window() in order for it to be called first,
# yet our gui_window() must also be able to see
# our functions above the file so that they can be called and "exist".
# Right now my brain is dead, so this is the solution
# I came up with.

def goto_add_task():
    gui_add_task()

def goto_check_task():
    gui_check_task()

def goto_remove_task():
    gui_remove_task()

def goto_add_project():
    gui_add_project()

def goto_check_project():
    gui_check_project()

def goto_remove_project():
    gui_remove_project()

def launch_notes_view():
    pass

def launch_todo_view():
    pass




# colors = {"darkblue": "#071e3d",
            #   "background": "#212121",
            #   "neogreen": "#0cbb7b",
            #   "darkmode": "#161618",
            #   "cyanblue": "#278EA5",
            #   "tealblue": "#21e6c1",
            #   "white": "#FFFFFF",
            #   "dracula": "#282a36"}

colors = theme.getThemeConfig()
print(colors)

root = Tk()

# listbox for projects
p_listbox = Listbox(root, fg=colors["subcolor"], bg=colors["boxcolor"],
highlightcolor=colors["headings"], font=("Arial",21), width = 80)
# listbox for tasks
t_listbox = Listbox(root, fg=colors["subcolor"], bg=colors["boxcolor"], 
highlightcolor=colors["headings"], font=("Arial", 21), width = 80)

p_array = projects.get_projects_data()
p_id_array = projects.get_projects_ids()
t_array = lists.get_todolist_data()
t_id_array = lists.get_todolist_ids()

def update_listboxes_data():
    # needs to be called on each button press whether we check the boxes or remove them
    global p_array; global t_array; global p_id_array; global t_id_array
    p_array = []
    p_id_array = []
    t_array = []
    t_id_array = []

    p_array = projects.get_projects_data()
    p_id_array = projects.get_projects_ids()
    t_array= lists.get_todolist_data()
    t_id_array = lists.get_todolist_ids()


    p_listbox.delete(0,'end')
    for count, item in enumerate(p_array):
        p_listbox.insert(count+1, f"{item.needsCompleted()} {item.name} | deadline:{item.deadline}")
    t_listbox.delete(0,'end')
    for count, item in enumerate(t_array):
        t_listbox.insert(count+1, f"{item.needsCompleted()} {item.name}")

update_listboxes_data()

def gui_taskview_window():
    print(p_id_array)
    print(t_id_array)

    time_text = weather.getLocalTime()
    weather_text = weather.getLocalWeather()
    weekday_text = weather.getWeekDay()


    sidebar = Frame(root, width=140, height=500, bg=colors["primarycolor"], relief='sunken', borderwidth = 2)

    sidebar.pack(expand=False, fill='both', side=LEFT, anchor='nw')


    menubar = Frame(sidebar, width=300, height=300, bg=colors["boxcolor"], relief='sunken', borderwidth=0)
    menubar.pack(expand=False, fill='none', side=TOP, anchor='nw')



    iconimage = Image.open("media/icon2.png")
    iconimage = iconimage.resize((140, 100), Image.NEAREST)

    logo = ImageTk.PhotoImage(iconimage)
    logolabel = Label(menubar, image = logo, bg=colors["boxcolor"], anchor="w")
    logolabel.place(x=0, y=0)
    logolabel.pack(side=LEFT)

    logotext = Label(menubar, text="neoNotes", font=("Roboto", 24, "bold"), bg=colors["boxcolor"], fg=colors["headings"], width=20, anchor="w")
    logotext.pack()

    viewlabel = Label(menubar, text="Tasks View", font=("Roboto", 24, "bold"), bg=colors["boxcolor"], fg=colors["headings"], width=20)
    viewlabel.pack()





    

    if weather.TimeOfDay() == 0:
        hellotext=f"Good Morning, {username}."
    elif weather.TimeOfDay() == 1:
        hellotext=f"Hello, {username}."
    elif weather.TimeOfDay() == 2:
        hellotext=f"Good Night, {username}."
    
    hellolabel = Label(sidebar, text=hellotext, font=("Roboto", 24, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
    hellolabel.pack()

    subtext = Label(sidebar, text="It is currently...", font=("Roboto", 18), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
    subtext.pack()
    # spacer = Label(sidebar, text=f"\n____________________\n", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["darkmode"], width=20)
    # spacer.pack()
    timelabel = Label(sidebar, text=f"{time_text}\n____________________", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
    timelabel.pack()
    weatherlabel = Label(sidebar, text=f"{weather_text}\n____________________", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
    weatherlabel.pack()
    weekdaylabel = Label(sidebar, text=f"{weekday_text}\n____________________", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
    weekdaylabel.pack()


    bannerimage = Image.open(selected_art)
    bannerimage = bannerimage.resize((int(root.winfo_screenwidth()), int(root.winfo_screenheight() * .25)), Image.BILINEAR)

    photo = ImageTk.PhotoImage(bannerimage)
    bannerlabel = Label(root, image = photo, bg=colors["background"])
    bannerlabel.pack(fill=BOTH, expand=YES)

    quoteoftheday = Label(root, text=f"{quotes.getDailyQuote()}", font=("Roboto", 12, "bold"), bg=colors["quotebackground"], fg=colors["quoteforeground"], borderwidth=2, relief="solid")
    quoteoftheday.place(x=700, y=100)


    root.title('Notes GUI')
    root.iconbitmap('media/icon2.ico')
    root.configure(background=colors["background"])

    p_label = Label(root, text="Projects to do", font=("Roboto", 28), bg=colors["background"], fg=colors["headings"])
    p_label.pack()

    # our buttons sidebar

    

    p_buttonsbar = Frame(sidebar, width=200, height=300, bg=colors["boxcolor"], relief='flat', borderwidth=0)
    p_buttonsbar.pack(expand=False, fill='both', side=TOP, anchor='nw')

    spacerbar = Frame(sidebar, width=1, height=1000, bg=colors["primarycolor"], relief='flat', borderwidth=0)
    spacerbar.pack(expand=False, fill='both', side=LEFT, anchor='nw')

    t_buttonsbar = Frame(sidebar, width=200, height=300, bg=colors["boxcolor"], relief='flat', borderwidth=0)
    t_buttonsbar.pack(expand=False, fill='both', side=BOTTOM, anchor='nw')

    
    p_add_btn = Image.open("media/addprojectbutton.png")
    p_add_btn = p_add_btn.resize((100, 50), Image.BILINEAR)
    p_formatted_add_btn = ImageTk.PhotoImage(p_add_btn)
    p_additembutton = Button(p_buttonsbar, image=p_formatted_add_btn, command=goto_add_project, width=100, height=50, relief='flat', borderwidth=0)
    p_additembutton.pack(side=LEFT)

    p_check_btn = Image.open("media/checkprojectbutton.png")
    p_check_btn = p_check_btn.resize((100, 50), Image.BILINEAR)
    p_formatted_check_btn = ImageTk.PhotoImage(p_check_btn)
    p_checkitembutton = Button(p_buttonsbar, image=p_formatted_check_btn, command=goto_check_project, width=100, height=50, border=0)
    p_checkitembutton.pack(side=LEFT)

    p_remove_btn = Image.open("media/removeprojectbutton.png")
    p_remove_btn = p_remove_btn.resize((100, 50), Image.BILINEAR)
    p_formatted_remove_btn = ImageTk.PhotoImage(p_remove_btn)
    p_removeitembutton = Button(p_buttonsbar, image=p_formatted_remove_btn, command=goto_remove_project, width=100, height=50, border=0)
    p_removeitembutton.pack(side=LEFT)


    p_listbox.pack()

    
    t_add_btn = Image.open("media/additembutton.png")
    t_add_btn = t_add_btn.resize((100, 50), Image.BILINEAR)
    t_formatted_add_btn = ImageTk.PhotoImage(t_add_btn)
    t_additembutton = Button(t_buttonsbar, image=t_formatted_add_btn, command=goto_add_task, width=100, height=50, border=0)
    t_additembutton.pack(side=LEFT)

    t_check_btn = Image.open("media/checkitembutton.png")
    t_check_btn = t_check_btn.resize((100, 50), Image.BILINEAR)
    t_formatted_check_btn = ImageTk.PhotoImage(t_check_btn)
    t_checkitembutton = Button(t_buttonsbar, image=t_formatted_check_btn, command=goto_check_task, width=100, height=50, border=0)
    t_checkitembutton.pack(side=LEFT)

    t_remove_btn = Image.open("media/removeitembutton.png")
    t_remove_btn = t_remove_btn.resize((100, 50), Image.BILINEAR)
    t_formatted_remove_btn = ImageTk.PhotoImage(t_remove_btn)
    t_removeitembutton = Button(t_buttonsbar, image=t_formatted_remove_btn, command=goto_remove_task, width=100, height=50, border=0)
    t_removeitembutton.pack(side=LEFT)

    t_label = Label(root, text="Tasks to do", font=("Roboto", 28), bg=colors["background"], fg=colors["headings"])
    t_label.pack()

    t_listbox.pack()

    display_in_real_time(timelabel)

    # default window size
    root.geometry("1536x900")
    root.mainloop()

# def resize_image(event):
#     new_width = event.width
#     new_height = event.height
#     bannerimage = copiedimage.resize((new_width, new_height))
#     photo = ImageTk.PhotoImage(image)
#     label.configure(image = photo)
#     label.image = photo

# buttons dont work, needs fixed
# idea: dont provide listbox as argument, simply have add_task and add_project as separate button commands for each respective list

def gui_add_task():
    display_in_real_time(timelabel)
    print("add button clicked")
    lists.add_task("dummy task")
    update_listboxes_data()
    
def gui_remove_task():
    print("remove button clicked")
    try:
        task_index = t_listbox.curselection()[0] 
        t_listbox.delete(task_index)
        lists.remove_task(t_id_array[task_index])
        update_listboxes_data()
    except IndexError:
        print("index error wtf")

def gui_check_task():
    print("check button clicked")
    try:
        task_index = t_listbox.curselection()[0]
        print(t_id_array[task_index])
        lists.check_uncheck_task(t_id_array[task_index])
        update_listboxes_data()
    except IndexError:
        print("index error wtf")

def gui_add_project():
    print("add button clicked")
    projects.add_project("dummy project")
    update_listboxes_data()

def gui_remove_project():
    try:
        project_index = p_listbox.curselection()[0] 
        p_listbox.delete(project_index)
        projects.remove_task(p_id_array[project_index])
        update_listboxes_data()
    except IndexError:
        print("index error wtf")

def gui_check_project():
    try:
        project_index = p_listbox.curselection()[0]
        projects.check_uncheck_project(p_id_array[project_index])
        update_listboxes_data()
    except IndexError:
        print("index error wtf")

def display_in_real_time(label):
    label.config(text=weather.getLocalTime())
    # label.after(1000,display_in_real_time(label))
    # time.sleep(1)


if __name__ == "__main__":
    gui_taskview_window()
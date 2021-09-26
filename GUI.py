# TEMPLATE CLASS FOR GUI APP
# for GUI
import tkinter as tk
from tkinter import *
# for images
from PIL import ImageTk, Image
from datetime import datetime

# # import our lists modules to be read
# import projects, lists
# for weather, time
import weather
# # lets randomize our banner on startup :)
from random import randint
# # for saving / loading in data
# import pickle
# # allows us to load in theme preferences from config/theme.json
import theme
# # allows us to display inspiring quotes
import quotes
# # for manipulating gui in real time (important for our use case)
from time import strftime
# projects
import projects
# tasks
import tasks

# plan on allowing user to provide wallpaper, for now this just works.
# banners = ["media/banner/woodcuts_1.jpg","media/banner/woodcuts_2.jpg","media/banner/woodcuts_3.jpg","media/banner/woodcuts_4.jpg", "media/banner/nasa_the_blue_marble.jpg"]
banners = [
"media/banner/0040.jpg",
"media/banner/0065.jpg",
"media/banner/0092.jpg",
"media/banner/0137.jpg",
"media/banner/0171.jpg",
"media/banner/0173.jpg",
"media/banner/0231.jpg",
"media/banner/0256.jpg",
"media/banner/0258.jpg",
"media/banner/0261.jpg",
"media/banner/0302.jpg",
"media/banner/woodcuts_1.jpg",
"media/banner/woodcuts_2.jpg",
"media/banner/woodcuts_3.jpg",
"media/banner/woodcuts_4.jpg",
"media/banner/nasa_the_blue_marble.jpg"
]



projects_category = "all"
tasks_category = "all"


def set_projects_category(input):
    projects_category = input

def set_tasks_category(input):
    tasks_category = input

projects_array = []
tasks_array = []

if projects_category != "all":
    for project in projects.get_projects(projects_category):
        projects_array.append(project[0])
else:
    for project in projects.get_all_projects():
        projects_array.append(project[0])

if tasks_category != "all":
    for task in tasks.get_tasks(tasks_category):
        tasks_array.append(task[0])
else:
    for task in tasks.get_all_tasks():
        tasks_array.append(task[0])

u_circle =  "\u25CF"

# time_text = weather.getLocalTime()
# weather_text = weather.getLocalWeather()
# weekday_text = weather.getWeekDay()





selected_art = banners[randint(0, len(banners)-1)]

# load in the user's name, to display a friendly message in sidebar

# get theme
colors = theme.getThemeConfig()

# button size i.e. FONT size (important to change depending upon your screen's resolution)

# for smaller screens (720pish)
# buttonfont = "consolas 14 bold"

# for larger screens (1080pish)
buttonfont = "consolas 20 bold"



# initialize Tk root
root = Tk()


# root.resizable(width=False, height=False)

# for smaller screens (720p) where font should also be set smaller
# root.minsize(width=800, height=700)

# for larger screens (1080p) where font is naturally larger
root.minsize(width=1000, height=950)

fullscreenstate = False

def resize(event):
    global fullscreenstate
    fullscreenstate = not fullscreenstate
    root.attributes("-fullscreen", fullscreenstate)
    return "break"



# def replace_quote():
#     quoteoftheday.place(x=100,y=100)

root.bind("<F11>", resize); root.bind("<f>", resize)
root.bind("<Control-q>",exit); root.bind("<Control-w>",exit)


def time(label):
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


quotes_x = 50

def tasks_view(master=root):
    clear_frame()
    menubar = TemplateMenubar(master, f"Tasks View (category: {tasks_category} )")
    quoteoftheday = Label(root, text=f"{quotes.getDailyQuote()}", font=("Roboto", 12, "bold"), bg=colors["quotebackground"], fg=colors["quoteforeground"], borderwidth=2, relief="solid")
    quoteoftheday.place(x=quotes_x, y=100)
    sidebar = TemplateSidebar(master)
    t_listbox = Listbox(master, fg=colors["tealblue"], bg=colors["boxcolor"],
    highlightcolor=colors["headings"], font="consolas 18", width = 80,
    borderwidth=1, relief="groove")

    for count, task in enumerate(tasks_array):
        t_listbox.insert(count+1, f"{u_circle} {task}")
        t_listbox.pack(side=TOP, fill=BOTH)



    # showtime = TimeWidgets(master)
    # showtime.update_clock()

def projects_view(master=root):
    clear_frame()
    menubar = TemplateMenubar(master, f"Projects View (category: {projects_category} )")
    quoteoftheday = Label(root, text=f"{quotes.getDailyQuote()}", font=("Roboto", 12, "bold"), bg=colors["quotebackground"], fg=colors["quoteforeground"], borderwidth=2, relief="solid")
    quoteoftheday.place(x=quotes_x, y=100)
    sidebar = TemplateSidebar(master)
    t_listbox = Listbox(master, fg=colors["tealblue"], bg=colors["boxcolor"],
    highlightcolor=colors["headings"], font="consolas 18", width = 80,
    height=400, borderwidth=1, relief="groove")

    for count, project in enumerate(projects_array):
        pname = f"{u_circle} {project}"
        t_listbox.insert(count+1, pname)
        t_listbox.pack(side=TOP, fill=BOTH)

    # for project in projects_array:
    #     x = Label(master, text=f"{u_circle} {project}",fg=colors["tealblue"], bg=colors["boxcolor"], font="consolas 18 bold", width=400, borderwidth=1, relief="groove", anchor="w")
    #     x.pack(side=TOP, fill=BOTH)

def habits_view(master=root):
    clear_frame()
    menubar = TemplateMenubar(master, "Habits View")
    quoteoftheday = Label(root, text=f"{quotes.getDailyQuote()}", font=("Roboto", 12, "bold"), bg=colors["quotebackground"], fg=colors["quoteforeground"], borderwidth=2, relief="solid")
    quoteoftheday.place(x=quotes_x, y=100)
    sidebar = TemplateSidebar(master)

def logging_view(master=root):
    clear_frame()
    menubar = TemplateMenubar(master, "Log")
    quoteoftheday = Label(root, text=f"{quotes.getDailyQuote()}", font=("Roboto", 12, "bold"), bg=colors["quotebackground"], fg=colors["quoteforeground"], borderwidth=2, relief="solid")
    quoteoftheday.place(x=quotes_x, y=100)
    sidebar = TemplateSidebar(master)

def graphing_view(master=root):
    clear_frame()
    menubar = TemplateMenubar(master, "Data Visualization")
    quoteoftheday = Label(root, text=f"{quotes.getDailyQuote()}", font=("Roboto", 12, "bold"), bg=colors["quotebackground"], fg=colors["quoteforeground"], borderwidth=2, relief="solid")
    quoteoftheday.place(x=quotes_x, y=100)
    sidebar = TemplateSidebar(master)
    
    logviewButton = Button(master,text="Log Hours",fg="white",
    bg=colors["background"], font="consolas 15 bold",
    command=totalhours_graph)
    logviewButton.pack(side=TOP, expand=False, fill=BOTH)

    totalhoursButton = Button(master, text="Graph total hours spent coding", fg="white",
    bg=colors["background"], font="consolas 15 bold", command=totalhours_graph)
    totalhoursButton.pack(side=TOP, expand=False, fill=BOTH)

    habitsButton = Button(master, text="Graph this month's habit streak", fg="white",
    bg=colors["background"], font="consolas 15 bold", command=totalhours_graph)
    habitsButton.pack(side=TOP, expand=False, fill=BOTH)

    moodButton = Button(master, text="Graph my daily mood", fg="white",
    bg=colors["background"], font="consolas 15 bold", command=totalhours_graph)
    moodButton.pack(side=TOP, expand=False, fill=BOTH)

    dailyproductivityButton = Button(master, text="Graph my daily productivity", fg="white",
    bg=colors["background"], font="consolas 15 bold", command=totalhours_graph)
    dailyproductivityButton.pack(side=TOP, expand=False, fill=BOTH)

    timelineButton = Button(master, text="Show Projects Timeline", fg="white",
    bg=colors["background"], font="consolas 15 bold", command=totalhours_graph)
    timelineButton.pack(side=BOTTOM, expand=True, fill=BOTH)


def readinglist_view(master=root):
    clear_frame()
    menubar = TemplateMenubar(master, "Reading List")
    sidebar = TemplateSidebar(master)


def clear_frame(master=root):
    for widgets in master.winfo_children():
        widgets.destroy()
    
def totalhours_graph():
    pass

# not sure what this does
# root.rowconfigure((0, 1, 2, 3), weight=1)




    # if current_size < 2:
    #     current_size += 1
    # else:
    #     current_size = 0

    # sizes = ['1200x950', '800x900', '1280x1920']

    # print(current_size)

    # root.geometry(sizes[current_size])

# load in image
bannerimage = Image.open(selected_art)

# not sure which image size I prefer

# bannerimage = bannerimage.resize((int(root.winfo_screenwidth()*.8), int(root.winfo_screenheight()*.2)), Image.BILINEAR)
bannerimage = bannerimage.resize((int(root.winfo_screenwidth()), int(root.winfo_screenheight()*.25)), Image.BILINEAR)

photo = ImageTk.PhotoImage(bannerimage)

class TimeWidgets():
    def __init__(self, master):
        self.label_date_now = Label(master, text="Current Date", bg="red", font = 'consolas 12 bold')
        self.label_date_now.pack(side=TOP, expand=False)

        self.label_time_now = Label(master, text="Current Time", bg="blue", font = 'consolas 12')
        self.label_time_now.pack(side=TOP, expand=False)

    def update_clock(self):
        time_now = weather.getLocalTime()
        weekday_now = weather.getWeekDay()
        self.label_date_now.config(text = weekday_now)
        self.label_date_now.after(500, self.update_clock)
        self.label_time_now.config(text = time_now)
        self.label_time_now.after(1000, self.update_clock)
        # return formatted_now

class TemplateWindow():
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry) # input, sizexsize
        self.root.config(bg=colors["background"])

        tasks_view(self.root)




        # todo: figure out why our banner isn't loading

        # menubar.forget()

        

        # menubar = TemplateMenubar(self.root, "Projects View")
        # sidebar = TemplateSidebar(self.root)

        self.root.mainloop()
        # mainloop()





        
        


    

class TemplateText(Label):
    def __init__(self, master, text):
        self.viewLabel = Label(master, text=text,fg="white",
        bg=colors["boxcolor"], font=buttonfont,
        borderwidth=2, relief="groove")
        self.viewLabel.pack(side=TOP, expand=True, fill=BOTH)


class TemplateSidebar(Frame):
    def __init__(self, master, bg=colors["boxcolor"], **kwargs):
        super(TemplateSidebar,self).__init__(master, **kwargs)


        # self.master = master
        self.config(bg = bg)
        # sidebarContainer = Frame(master, width=140, height=10000, bg=bg, relief='sunken', borderwidth = 0)
        
        # Frame.__init__(self, master, width=140, height=100, bg=bg, relief='sunken', borderwidth = 0)
        
        # sidebar = Frame(master, width=140, height=10000, bg=colors["primarycolor"], relief='sunken', borderwidth = 0)
        # sidebar.pack(expand=True, fill='y', side=LEFT, anchor='nw')


        self.buttonframe = Frame(self)
        self.buttonframe.config(bg = bg)
        self.buttonframe.grid(row=0,column=0)

        # button = MenuButton(self)

        self.dataLabel = Label(self.buttonframe, text="Data",fg="white",
        bg=colors["boxcolor"], font=buttonfont,
        borderwidth=2, relief="groove")
        self.dataLabel.pack(side=TOP, expand=True, fill=BOTH)

        self.loadbutton = Button(self.buttonframe,text="load/import data",fg="white",
        bg=colors["background"], font="consolas 10 bold", command="resize")
        # self.loadbutton.bind("<Return>", resize)
        self.loadbutton.pack(side=TOP, expand=True, fill=BOTH)

        self.savebutton = Button(self.buttonframe,text="save/export data",fg="white",
        bg=colors["background"], font="consolas 10 bold")
        self.savebutton.pack(side=TOP, expand=True, fill=BOTH)


        self.viewLabel = Label(self.buttonframe, text="Views",fg="white",
        bg=colors["boxcolor"], font=buttonfont,
        borderwidth=2, relief="groove")
        self.viewLabel.pack(side=TOP, expand=True, fill=BOTH)

        self.viewtasksButton = Button(self.buttonframe,text="Tasks",fg="white",
        bg=colors["background"], font=buttonfont,
        command=tasks_view)
        self.viewtasksButton.pack(side=TOP, expand=True, fill=BOTH)


        self.viewprojectsButton = Button(self.buttonframe,text="Projects",fg="white",
        bg=colors["background"], font=buttonfont,
        command=projects_view)
        self.viewprojectsButton.pack(side=TOP, expand=True, fill=BOTH)


        self.viewhabitsButton = Button(self.buttonframe,text="Habits",fg="white",
        bg=colors["background"], font=buttonfont,
        command=habits_view)
        self.viewhabitsButton.pack(side=TOP, expand=True, fill=BOTH)

        self.graphdataButton = Button(self.buttonframe,text="Graph of Data",fg="white",
        bg=colors["background"], font=buttonfont,
        command=graphing_view)
        self.graphdataButton.pack(side=TOP, expand=True, fill=BOTH)

        self.readinglistButton = Button(self.buttonframe,text="Reading List",fg="white",
        bg=colors["background"], font=buttonfont,
        command=readinglist_view)
        self.readinglistButton.pack(side=TOP, expand=True, fill=BOTH)

        self.dataLabel = Label(self.buttonframe, text="Items",fg="white",
        bg=colors["boxcolor"], font=buttonfont,
        borderwidth=2, relief="groove")
        self.dataLabel.pack(side=TOP, expand=True, fill=BOTH)

        self.additem = Button(self.buttonframe,text="add",fg="white",
        bg=colors["primarycolor"],font=buttonfont,
        command="exit")
        self.additem.pack(side=LEFT, expand=False, fill='y')

        self.checkitem = Button(self.buttonframe,text="check",fg="yellow",
        bg=colors["primarycolor"],font=buttonfont,
        command="exit")
        self.checkitem.pack(side=LEFT, expand=False, fill='y')

        self.removeitem = Button(self.buttonframe,text="remove",fg="white",
        bg=colors["primarycolor"],font=buttonfont,
        command="exit")
        self.removeitem.pack(side=LEFT, expand=False, fill='y')







        # button.pack()



        Frame.pack(self, side=LEFT, expand=True, fill='y', anchor='nw')
        # Frame.pack(self, master, expand=True, fill='y', side=LEFT, anchor='nw')



        # buttonsContainer = Frame(master, bg="red", width=20, height=20, relief='sunken', borderwidth = 0)
        
        # sidebarContainer.pack(master, expand=True, fill='y', side=LEFT, anchor='nw')
        # buttonsContainer.pack(self, expand=False)
    


class RedSidebar(TemplateSidebar):
    def __init__(self, master):
        TemplateSidebar.__init__(self, master, bg="red")

# TODO: figure out how to get this template class to have a "level" in the root's heirarchy, so that I can place
# template items within template items, using classes


class TemplateMenubar(Frame):
    def __init__(self, master, current_view):
        Frame.__init__(self, master, width=30000, height=150, bg=colors["boxcolor"], relief='sunken', borderwidth=0)

        banner = TemplateBanner(self)

        Frame.pack(self, expand=True, fill='x', side=TOP, anchor='nw')


        # iconimage = Image.open("media/icon2.png")
        # iconimage = iconimage.resize((140, 100), Image.NEAREST)

        # logo = ImageTk.PhotoImage(iconimage)
        # logolabel = Label(self, image = logo, bg=colors["boxcolor"], anchor="w")
        # logolabel.place(x=0, y=0)
        # logolabel.pack(side=LEFT)


        # logotext = Label(self, text="Notion Clone", font=("Roboto", 24, "bold"), bg=colors["boxcolor"], fg=colors["headings"], width=20, anchor="w")
        # logotext.pack()

        viewlabel = Label(self, text=f"{current_view}", font=("Roboto", 24, "bold"), bg=colors["boxcolor"], fg=colors["headings"], width=50, anchor="w")
        viewlabel.pack()

        # banner =  TemplateBanner(self.master)

class TemplateBanner():
    def __init__(self, master):
        bannerlabel = Label(master, image = photo, bg=colors["background"])
        bannerlabel.pack(expand=True, fill="y")

class MenuButton(Button):
    def __init__(self, master):
        Button.__init__(self, master, text="exit program", fg="red", bg=colors["background"], command="exit")
        Frame.grid(self, row=0, column=0,pady=(10,0))
        Button.pack(master)



# class TemplateMenu:
#     def __init__(self, root,)


# # listbox for projects
# p_listbox = Listbox(root, fg=colors["subcolor"], bg=colors["boxcolor"],
# highlightcolor=colors["headings"], font=("Arial",21), width = 80)
# # listbox for tasks
# t_listbox = Listbox(root, fg=colors["subcolor"], bg=colors["boxcolor"], 
# highlightcolor=colors["headings"], font=("Arial", 21), width = 80)


# def gui_taskview_window():
#     print(p_id_array)
#     print(t_id_array)

#     time_text = weather.getLocalTime()
#     weather_text = weather.getLocalWeather()
#     weekday_text = weather.getWeekDay()


#     sidebar = Frame(root, width=140, height=500, bg=colors["primarycolor"], relief='sunken', borderwidth = 2)

#     sidebar.pack(expand=False, fill='both', side=LEFT, anchor='nw')



#     if weather.TimeOfDay() == 0:
#         hellotext=f"Good Morning, {username}."
#     elif weather.TimeOfDay() == 1:
#         hellotext=f"Hello, {username}."
#     elif weather.TimeOfDay() == 2:
#         hellotext=f"Good Night, {username}."
    
#     hellolabel = Label(sidebar, text=hellotext, font=("Roboto", 24, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
#     hellolabel.pack()

#     subtext = Label(sidebar, text="It is currently...", font=("Roboto", 18), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
#     subtext.pack()
#     # spacer = Label(sidebar, text=f"\n____________________\n", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["darkmode"], width=20)
#     # spacer.pack()
#     timelabel = Label(sidebar, text=f"{time_text}\n____________________", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
#     timelabel.pack()
#     weatherlabel = Label(sidebar, text=f"{weather_text}\n____________________", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
#     weatherlabel.pack()
#     weekdaylabel = Label(sidebar, text=f"{weekday_text}\n____________________", font=("Roboto", 20, "bold"), bg=colors["primarycolor"], fg=colors["boxcolor"], width=20)
#     weekdaylabel.pack()




#     quoteoftheday = Label(root, text=f"{quotes.getDailyQuote()}", font=("Roboto", 12, "bold"), bg=colors["quotebackground"], fg=colors["quoteforeground"], borderwidth=2, relief="solid")
#     quoteoftheday.place(x=700, y=100)


#     root.title('Notes GUI')
#     root.iconbitmap('media/icon2.ico')
#     root.configure(background=colors["background"])

#     p_label = Label(root, text="Projects to do", font=("Roboto", 28), bg=colors["background"], fg=colors["headings"])
#     p_label.pack()

def gui_main():
    label = Label(root, font="consolas 18", background="black", foreground="cyan")
    label.pack(anchor='center')
    time(label)
    window0 = TemplateWindow(root, "Notion Clone -- f to fullscreen, ctrl-q to quit", "1200x950")
    # window1 = TemplateWindow(root, "Notion Clone", "1080x720")


if __name__ == "__main__":
    gui_main()
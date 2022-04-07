import tkinter as tk
from tkinter import *



class Option_Pricer:
    def __init__(self):
        self.top_win = tk.Tk()
        self.top_win.geometry('500x350+300+200')
        self.top_win.title("Option Pricier")
        # Set menu of the window
        self.menus = tk.Menu(self.top_win)
        self.menus.add_command(label = "European Option", command = self.useEuropean)
        self.menus.add_command(label = "Asian Option", command = self.useAsian)
        self.menus.add_command(label = "American Option", command = self.useAmerican)
        self.menus.add_command(label = "About", command = self.gotoAbout)
        self.menus.add_command(label = "Exit", command=self.top_win.quit)
        # Set frames
        self.european = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.asian = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.american = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.about = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.initComponments()

    # Set the
    def initComponments(self):
        self.european.pack(fill=tk.BOTH, expand=True)
        self.european.config(bg='lightblue')

    def useEuropean(self):
        self.european.pack(fill=tk.BOTH, expand=True)
        self.asian.pack_forget()
        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('European Option')
        self.european.config(bg='lightblue')

    def useAsian(self):
        self.asian.pack(fill=tk.BOTH, expand=True)
        self.european.pack_forget()
        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('Asian Option')
        self.asian.config(bg='lightgreen')

    def useAmerican(self):
        self.american.pack(fill=tk.BOTH, expand=True)
        self.asian.pack_forget()
        self.european.pack_forget()
        self.about.pack_forget()
        self.top_win.title('American Option')
        self.american.config(bg='lightyellow')

    def gotoAbout(self):
        self.about.pack(fill=tk.BOTH, expand=True)
        self.american.pack_forget()
        self.asian.pack_forget()
        self.european.pack_forget()
        self.top_win.title('About')
        # photo = PhotoImage(file="C:\\Users\\Tian Yu\\Desktop\\logo.gif")
        # Label(self.about, image=photo).grid(row=11, column=0, sticky='w')
        self.about.config(bg='white')
        self.setAbout()

    def setAbout(self):
        # self.about.grid(row=0, column=0, sticky='w')
        about_title = Label(self.about, text = 'Option Pricier', fg = 'black', bg = 'white', font=("Times New Roman", 18, "bold")).grid(row=0, column=0, sticky='w')
        introduction = Label(self.about, text="1. Introduction", fg = 'black', bg = 'white', font=("Times New Roman", 13, "bold")).grid(row=1, column=0, sticky='w')
        intro_contents1 = "* The option pricier has three option categories, including European Option, Asian Option"
        intro_contents2 = "and American Option. Users can use the top menu to select type."
        intro_contents3 = "* Fill in all blanks and click calculate button, the result will be shown."
        intro_label1 = Label(self.about, text=intro_contents1, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=2, column=0, sticky='w')
        intro_label2 = Label(self.about, text=intro_contents2, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=3, column=0, sticky='w')
        intro_label3 = Label(self.about, text=intro_contents3, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=4, column=0, sticky='w')
        group = Label(self.about, text="2. About", fg = 'black', bg = 'white', font=("Times New Roman", 13, "bold")).grid(row=5, column=0, sticky='w')
        group_contents1 = "*This is the assignment for FITE7405 Techniques in Computational Finance @HKU."
        Label(self.about, text=group_contents1, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=6, column=0, sticky='w')
        group_contents2 = "Group 5"
        Label(self.about, text=group_contents2, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=7, column=0, sticky='w')
        group_contents3 = "Liu Jingyun 3035906655"
        group_contents4 = "Tian Yu 3035905089"
        group_contents5 = "Wang Zhao 3035907037"
        Label(self.about, text=group_contents3, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=8, column=0, sticky='w')
        Label(self.about, text=group_contents4, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=9, column=0, sticky='w')
        Label(self.about, text=group_contents5, fg = 'black', bg = 'white', font=("Times New Roman", 10)).grid(row=10, column=0, sticky='w')
        global photo
        photo = PhotoImage(file="logo.gif")
        Label(self.about, bg='white',image=photo).grid(row=11, column=0, sticky='w')




    #     grid(column=0, row=0)



    def start(self):
        self.top_win.config(menu=self.menus)
        self.top_win.mainloop()


obj = Option_Pricer()
obj.start()
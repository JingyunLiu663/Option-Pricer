import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from EuropeanOption import Black_Schonles_Formulas, Black_Schonles_Formulas_new, Implied_Volatility


class Option_Pricer:
    def __init__(self):
        self.top_win = tk.Tk()
        self.top_win.geometry('600x390+300+200')
        self.top_win.title("Option Pricier")
        # Set menu of the window
        self.menus = tk.Menu(self.top_win, tearoff=False)
        self.europoean_menu = Menu(self.menus, tearoff=False)
        self.menus.add_command(label="European Option", command=self.useEuropean)
        self.menus.add_command(label="Implied Volatility", command=self.useVolatility)

        self.menus.add_command(label="Arithmetic Asian Option", command=self.useArithmeticAsian)
        self.menus.add_command(label="Geometric Asian Option", command=self.useGeometricAsian)

        self.menus.add_command(label="Arithmetic Basket Option", command=self.useArithmeticBasket)
        self.menus.add_command(label="Geometric Basket Option")

        self.menus.add_command(label="American Binominal Tree", command=self.useAmerican)

        self.menus.add_command(label="About", command=self.gotoAbout)
        self.menus.add_command(label="Exit", command=self.top_win.quit)
        # Set frames
        # European Option
        self.european = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.volatility = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        # Asian Option
        self.geometric_asian = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.arithmetic_asian = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        # Basket Option
        self.geometric_basket = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.arithmetic_basket = tk.Frame(self.top_win, relief='ridge', borderwidth=3)

        self.american = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.about = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        self.initComponments()

    # Set the
    def initComponments(self):
        self.european.pack(fill=tk.BOTH, expand=True)
        self.european.config(bg='white')
        self.setEuropean()

    def useEuropean(self):
        self.european.pack(fill=tk.BOTH, expand=True)
        self.volatility.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.geometric_asian.pack_forget()
        self.arithmetic_basket.pack_forget()
        self.geometric_basket.pack_forget()
        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('European Option')
        self.european.config(bg='white')
        self.setEuropean()

    def useVolatility(self):
        self.volatility.pack(fill=tk.BOTH, expand=True)
        self.european.pack_forget()
        self.geometric_asian.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.arithmetic_basket.pack_forget()
        self.geometric_basket.pack_forget()
        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('Implied Volatility')
        self.volatility.config(bg='white')
        self.setVolatility()

    def useArithmeticAsian(self):
        self.arithmetic_asian.pack(fill=tk.BOTH, expand=True)
        self.european.pack_forget()
        self.volatility.pack_forget()
        self.geometric_asian.pack_forget()
        self.arithmetic_basket.pack_forget()
        self.geometric_basket.pack_forget()
        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('Arithmetic Asian Option')
        self.arithmetic_asian.config(bg='white')
        self.setArithmeticAsian()

    def useGeometricAsian(self):
        self.geometric_asian.pack(fill=tk.BOTH, expand=True)
        self.european.pack_forget()
        self.volatility.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.arithmetic_basket.pack_forget()
        self.geometric_basket.pack_forget()

        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('Geometric Asian Option')
        self.geometric_asian.config(bg='White')
        self.setGeometricAsian()

    def useArithmeticBasket(self):
        self.arithmetic_basket.pack(fill=tk.BOTH, expand=True)
        self.european.pack_forget()
        self.volatility.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.geometric_asian.pack_forget()
        self.geometric_basket.pack_forget()
        self.about.pack_forget()
        self.top_win.title('Arithmetic Basket Option')
        self.arithmetic_basket.config(bg='lightgreen')



    def useAmerican(self):
        self.american.pack(fill=tk.BOTH, expand=True)
        self.volatility.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.geometric_asian.pack_forget()
        self.european.pack_forget()
        self.about.pack_forget()
        self.top_win.title('American Option')
        self.american.config(bg='lightyellow')

    def gotoAbout(self):
        self.about.pack(fill=tk.BOTH, expand=True)
        self.american.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.geometric_asian.pack_forget()
        self.arithmetic_basket.pack_forget()
        self.geometric_basket.pack_forget()
        self.european.pack_forget()
        self.volatility.pack_forget()
        self.top_win.title('About')
        self.about.config(bg='white')
        self.setAbout()

    def setEuropean(self):
        # Initialization the European option page
        # Label(self.european, text = 'European Option', fg = 'black', bg = 'white', font=("Times New Roman", 10, "bold")).grid(row=0, column=0, sticky='w')
        Label(self.european, text='Spot Price: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=0, column=0, sticky='w', pady=5)
        self.input_spot_price_european = Text(self.european, height=1, width=23, borderwidth=2)
        self.input_spot_price_european.grid(row=0, column=1,sticky='w')
        Label(self.european, text='   Strike Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(row=0, column=2, sticky='w')
        self.input_strike_price_european = Text(self.european, height=1, width=23, borderwidth=2)
        self.input_strike_price_european.grid(row=0, column=3, sticky='w')

        Label(self.european, text='Risk Free Rate: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=1, column=0, sticky='w', pady=10)
        self.input_rise_free_rate_european = Text(self.european, height=1, width=23, borderwidth=2)
        self.input_rise_free_rate_european.grid(row=1, column=1, sticky='w')

        # Label(self.european, text='   Start Time: ', fg='black', bg='white', font=("Times New Roman", 10, "bold")).grid(
        #     row=1, column=2, sticky='w')
        # self.input_start_time_european = Text(self.european, height=1, width=21, borderwidth=2)
        # self.input_start_time_european.grid(row=1, column=3, sticky='w')
        # self.input_start_time_european.insert(INSERT, "dd/MM/yyyy")
        Label(self.european, text='   Maturity: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=1, column=2, sticky='w')

        self.input_maturity_european = Text(self.european, height=1, width=23, borderwidth=2)
        self.input_maturity_european.grid(row=1, column=3,sticky='w')
        # self.input_maturity_european.insert(INSERT, "")

        Label(self.european, text='Repo Rate: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=2, column=0, sticky='w', pady=10)
        self.input_repo_european = Text(self.european, height=1, width=23, borderwidth=2)
        self.input_repo_european.grid(row=2, column=1, sticky='w')

        Label(self.european, text='   Volatility: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=2, column=2, sticky='w')
        self.input_volatility_european = Text(self.european, height=1, width=23, borderwidth=2)
        self.input_volatility_european.grid(row=2, column=3, sticky='w')


        Label(self.european, text='Option Type: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=3, column=0, sticky='w', pady=10)

        self.select_option_european = StringVar()
        self.input_option_european = ttk.Combobox(self.european, width=15, textvariable=self.select_option_european)
        self.input_option_european.grid(row=3, column=1, sticky='w')
        self.input_option_european['values'] = ('Call Option', 'Put Option')
        self.input_option_european.current(0)

        self.clear_european = Button(self.european, text="Clear", width=10, command=self.clearEuropean)
        self.clear_european.grid(row=3, column=3, sticky='w')
        self.clear_european = Button(self.european, text="Submit", width=10, command=self.doEuropeanOption)
        self.clear_european.grid(row=3, column=2, sticky='w')

        Label(self.european, text='Result: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(row=4, column=0, sticky='w')
        self.european_result = Text(self.european, height=12, width=82, borderwidth=2)
        self.european_result.place(x=5, y=195)

    def setVolatility(self):
        Label(self.volatility, text='Spot Price: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=0, column=0, sticky='w', pady=5)
        self.input_spot_price_volatility = Text(self.volatility, height=1, width=23, borderwidth=2)
        self.input_spot_price_volatility.grid(row=0, column=1, sticky='w')

        Label(self.volatility, text='   Strike Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(row=0, column=2, sticky='w')
        self.input_strike_price_volatility = Text(self.volatility, height=1, width=23, borderwidth=2)
        self.input_strike_price_volatility.grid(row=0, column=3, sticky='w')

        Label(self.volatility, text='Risk Free Rate: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=1, column=0, sticky='w', pady=10)
        self.input_rise_free_rate_volatility = Text(self.volatility, height=1, width=23, borderwidth=2)
        self.input_rise_free_rate_volatility.grid(row=1, column=1, sticky='w')

        Label(self.volatility, text='Repo Rate: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=2, column=0, sticky='w', pady=10)
        self.input_repo_volatility = Text(self.volatility, height=1, width=23, borderwidth=2)
        self.input_repo_volatility.grid(row=2, column=1, sticky='w')

        Label(self.volatility, text='   Maturity: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=1, column=2, sticky='w')
        self.input_maturity_volatility = Text(self.volatility, height=1, width=23, borderwidth=2)
        self.input_maturity_volatility.grid(row=1, column=3, sticky='w')

        Label(self.volatility, text='   Option Price: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=2, column=2, sticky='w')
        self.input_option_price_volatility = Text(self.volatility, height=1, width=23, borderwidth=2)
        self.input_option_price_volatility.grid(row=2, column=3, sticky='w')

        Label(self.volatility, text='Option Type: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=3, column=0, sticky='w', pady=10)
        self.select_option_volatility = StringVar()
        self.input_option_volatility = ttk.Combobox(self.volatility, width=15, textvariable=self.select_option_volatility)
        self.input_option_volatility.grid(row=3, column=1, sticky='w')
        self.input_option_volatility['values'] = ('Call Option', 'Put Option')
        self.input_option_volatility.current(0)

        self.clear_volatility = Button(self.volatility, text="Clear", width=10, command=self.clearVolatility)
        self.clear_volatility.grid(row=3, column=3, sticky='w')
        self.submit_volatility = Button(self.volatility, text="Submit", width=10, command=self.doVolatility)
        self.submit_volatility.grid(row=3, column=2, sticky='w')

        Label(self.volatility, text='Result: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(row=4,
                                                                                                                 column=0,
                                                                                                                 sticky='w')
        self.result_volatility = Text(self.volatility, height=12, width=82, borderwidth=2)
        self.result_volatility.place(x=5, y=195)


    def setArithmeticAsian(self):
        Label(self.arithmetic_asian, text='Spot Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=0, column=0, sticky='w', pady=5)
        self.input_spot_price_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_spot_price_arithmetic_asian.grid(row=0, column=1, sticky='w')

        Label(self.arithmetic_asian, text='   Strike Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(row=0, column=2, sticky='w')
        self.input_strike_price_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_strike_price_arithmetic_asian.grid(row=0, column=3, sticky='w')

        Label(self.arithmetic_asian, text='Risk Free Rate: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=0, sticky='w', pady=10)
        self.input_rise_free_rate_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_rise_free_rate_arithmetic_asian.grid(row=1, column=1, sticky='w')

        Label(self.arithmetic_asian, text='   Maturity: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=2, sticky='w')
        self.input_maturity_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_maturity_arithmetic_asian.grid(row=1, column=3, sticky='w')

        Label(self.arithmetic_asian, text='Volatility: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=0, sticky='w', pady=10)
        self.input_volatility_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_volatility_arithmetic_asian.grid(row=2, column=1, sticky='w')

        Label(self.arithmetic_asian, text='   Observe No.: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=2, sticky='w')
        self.input_observe_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_observe_arithmetic_asian.grid(row=2, column=3, sticky='w')

        Label(self.arithmetic_asian, text='Option Type: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=0, sticky='w', pady=10)
        self.select_option_arithmetic_asian = StringVar()
        self.input_option_arithmetic_asian = ttk.Combobox(self.arithmetic_asian, width=21,
                                                         textvariable=self.select_option_arithmetic_asian)
        self.input_option_arithmetic_asian.grid(row=3, column=1, sticky='w')
        self.input_option_arithmetic_asian['values'] = ('Call Option', 'Put Option')
        self.input_option_arithmetic_asian.current(0)

        Label(self.arithmetic_asian, text='   Calculation: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=2, sticky='w', pady=10)
        self.select_calcualtion_arithmetic_asian = StringVar()
        self.input_calcualtion_arithmetic_asian = ttk.Combobox(self.arithmetic_asian, width=21,
                                                              textvariable=self.select_calcualtion_arithmetic_asian)
        self.input_calcualtion_arithmetic_asian.grid(row=3, column=3, sticky='w')
        self.input_calcualtion_arithmetic_asian['values'] = ('Closed-Form Fomula', 'Standard MC')
        self.input_calcualtion_arithmetic_asian.current(0)

        Label(self.arithmetic_asian, text='Result: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=5, column=0, sticky='w')

        Label(self.arithmetic_asian, text='MC Path No.: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=4, column=0, sticky='w')
        self.input_path_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_path_arithmetic_asian.grid(row=4, column=1, sticky='w')

        Label(self.arithmetic_asian, text='   Control Variate: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=4, column=2, sticky='w')
        self.select_control_arithmetic_asian = StringVar()
        self.input_control_arithmetic_asian = ttk.Combobox(self.arithmetic_asian, width=21,
                                                               textvariable=self.select_control_arithmetic_asian)
        self.input_control_arithmetic_asian.grid(row=4, column=3, sticky='w')
        self.input_control_arithmetic_asian['values'] = ('No control variate', 'Geometric Asian option')
        self.input_control_arithmetic_asian.current(0)

        self.clear_arithmetic_asian = Button(self.arithmetic_asian, text="Clear", width=10,
                                            command=self.clearArithmeticAsian)
        self.clear_arithmetic_asian.place(x=220, y=193)
        self.submit_arithmetic_asian = Button(self.arithmetic_asian, text="Submit", width=10,
                                             command=self.doGeometricAsian)
        self.submit_arithmetic_asian.place(x=120, y=193)

        self.result_arithmetic_asian = Text(self.arithmetic_asian, height=10, width=82, borderwidth=2)
        self.result_arithmetic_asian.place(x=5, y=225)


    def setGeometricAsian(self):
        Label(self.geometric_asian, text='Spot Price: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=0, column=0, sticky='w', pady=5)
        self.input_spot_price_geometric_asian = Text(self.geometric_asian, height=1, width=23, borderwidth=2)
        self.input_spot_price_geometric_asian.grid(row=0, column=1, sticky='w')

        Label(self.geometric_asian, text='   Strike Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(row=0, column=2, sticky='w')
        self.input_strike_price_geometric_asian = Text(self.geometric_asian, height=1, width=23, borderwidth=2)
        self.input_strike_price_geometric_asian.grid(row=0, column=3, sticky='w')

        Label(self.geometric_asian, text='Risk Free Rate: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=1, column=0, sticky='w', pady=10)
        self.input_rise_free_rate_geometric_asian = Text(self.geometric_asian, height=1, width=23, borderwidth=2)
        self.input_rise_free_rate_geometric_asian.grid(row=1, column=1, sticky='w')

        Label(self.geometric_asian, text='   Maturity: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=1, column=2, sticky='w')
        self.input_maturity_geometric_asian = Text(self.geometric_asian, height=1, width=23, borderwidth=2)
        self.input_maturity_geometric_asian.grid(row=1, column=3, sticky='w')

        Label(self.geometric_asian, text='Volatility: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=2, column=0, sticky='w', pady=10)
        self.input_volatility_geometric_asian = Text(self.geometric_asian, height=1, width=23, borderwidth=2)
        self.input_volatility_geometric_asian.grid(row=2, column=1, sticky='w')

        Label(self.geometric_asian, text='   Observe No.: ', fg='black', bg='white',font=("Times New Roman", 12, "bold")).grid(
            row=2, column=2, sticky='w')
        self.input_observe_geometric_asian = Text(self.geometric_asian, height=1, width=23, borderwidth=2)
        self.input_observe_geometric_asian.grid(row=2, column=3, sticky='w')

        Label(self.geometric_asian, text='Option Type: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=3, column=0, sticky='w', pady=10)
        self.select_option_geometric_asian = StringVar()
        self.input_option_geometric_asian = ttk.Combobox(self.geometric_asian, width=21, textvariable=self.select_option_geometric_asian)
        self.input_option_geometric_asian.grid(row=3, column=1, sticky='w')
        self.input_option_geometric_asian['values'] = ('Call Option', 'Put Option')
        self.input_option_geometric_asian.current(0)

        Label(self.geometric_asian, text='   Calculation: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=2, sticky='w', pady=10)
        self.select_calcualtion_geometric_asian = StringVar()
        self.input_calcualtion_geometric_asian = ttk.Combobox(self.geometric_asian, width=21,
                                                         textvariable=self.select_calcualtion_geometric_asian)
        self.input_calcualtion_geometric_asian.grid(row=3, column=3, sticky='w')
        self.input_calcualtion_geometric_asian['values'] = ('Closed-Form Fomula', 'Standard MC')
        self.input_calcualtion_geometric_asian.current(0)

        Label(self.geometric_asian, text='Result: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(row=4, column=0, sticky='w')

        self.clear_geometric_asian = Button(self.geometric_asian, text="Clear", width=10, command=self.clearGeometricAsian)
        self.clear_geometric_asian.place(x=220, y=165)
        self.submit_geometric_asian = Button(self.geometric_asian, text="Submit", width=10, command=self.doGeometricAsian)
        self.submit_geometric_asian.place(x=120, y=165)

        self.result_geometric_asian = Text(self.geometric_asian, height=12, width=82, borderwidth=2)
        self.result_geometric_asian.place(x=5, y=195)


    def setArithmeticBasket(self):
        print()


    def setAbout(self):
        # self.about.grid(row=0, column=0, sticky='w')
        about_title = Label(self.about, text='Option Pricier', fg='black', bg='white',
                            font=("Times New Roman", 18, "bold")).grid(row=0, column=0, sticky='w')
        introduction = Label(self.about, text="1. Introduction", fg='black', bg='white',
                             font=("Times New Roman", 13, "bold")).grid(row=1, column=0, sticky='w')
        intro_contents1 = "* The option pricier has three option categories, including European Option, Asian Option"
        intro_contents2 = "and American Option. Users can use the top menu to select type."
        intro_contents3 = "* Fill in all blanks and click calculate button, the result will be shown."
        intro_label1 = Label(self.about, text=intro_contents1, fg='black', bg='white',
                             font=("Times New Roman", 10)).grid(row=2, column=0, sticky='w')
        intro_label2 = Label(self.about, text=intro_contents2, fg='black', bg='white',
                             font=("Times New Roman", 10)).grid(row=3, column=0, sticky='w')
        intro_label3 = Label(self.about, text=intro_contents3, fg='black', bg='white',
                             font=("Times New Roman", 10)).grid(row=4, column=0, sticky='w')
        group = Label(self.about, text="2. About", fg='black', bg='white', font=("Times New Roman", 13, "bold")).grid(
            row=5, column=0, sticky='w')
        group_contents1 = "*This is the assignment for FITE7405 Techniques in Computational Finance @HKU."
        Label(self.about, text=group_contents1, fg='black', bg='white', font=("Times New Roman", 10)).grid(row=6, column=0, sticky='w')
        group_contents2 = "Group 5"
        Label(self.about, text=group_contents2, fg='black', bg='white', font=("Times New Roman", 10)).grid(row=7, column=0, sticky='w')
        group_contents3 = "Liu Jingyun 3035906655"
        group_contents4 = "Tian Yu 3035905089"
        group_contents5 = "Wang Zhao 3035907037"
        Label(self.about, text=group_contents3, fg='black', bg='white', font=("Times New Roman", 10)).grid(row=8, column=0, sticky='w')
        Label(self.about, text=group_contents4, fg='black', bg='white', font=("Times New Roman", 10)).grid(row=9, column=0, sticky='w')
        Label(self.about, text=group_contents5, fg='black', bg='white', font=("Times New Roman", 10)).grid(row=10, column=0, sticky='w')
        global photo
        photo = PhotoImage(file="logo.gif")
        Label(self.about, bg='white', image=photo).grid(row=11, column=0, sticky='w')

    # Clear all fields in the European option page
    def clearEuropean(self):
        self.input_spot_price_european.delete('1.0','end')
        self.input_maturity_european.delete('1.0', 'end')
        self.input_rise_free_rate_european.delete('1.0', 'end')
        self.input_repo_european.delete('1.0', 'end')
        self.input_volatility_european.delete('1.0', 'end')
        self.input_strike_price_european.delete('1.0', 'end')
        self.input_option_european['values'] = ('Call Option', 'Put Option')
        self.input_option_european.current(0)

    # Clear all fields in the volatility page
    def clearVolatility(self):
        self.input_spot_price_volatility.delete('1.0', 'end')
        self.input_maturity_volatility.delete('1.0', 'end')
        self.input_rise_free_rate_volatility.delete('1.0', 'end')
        self.input_repo_volatility.delete('1.0', 'end')
        self.input_option_price_volatility.delete('1.0', 'end')
        self.input_strike_price_volatility.delete('1.0', 'end')
        self.input_option_volatility['values'] = ('Call Option', 'Put Option')
        self.input_option_volatility.current(0)

    def clearGeometricAsian(self):
        self.input_maturity_geometric_asian.delete('1.0', 'end')
        self.input_rise_free_rate_geometric_asian.delete('1.0', 'end')
        self.input_volatility_geometric_asian.delete('1.0', 'end')
        self.input_spot_price_geometric_asian.delete('1.0', 'end')
        self.input_strike_price_geometric_asian.delete('1.0', 'end')
        self.input_observe_geometric_asian.delete('1.0', 'end')
        self.input_calcualtion_geometric_asian['values'] = ('Closed-Form Fomula', 'Standard MC')
        self.input_calcualtion_geometric_asian.current(0)
        self.input_option_geometric_asian['values'] = ('Call Option', 'Put Option')
        self.input_option_geometric_asian.current(0)

    def clearArithmeticAsian(self):
        self.input_maturity_arithmetic_asian.delete('1.0', 'end')
        self.input_rise_free_rate_arithmetic_asian.delete('1.0', 'end')
        self.input_volatility_arithmetic_asian.delete('1.0', 'end')
        self.input_spot_price_arithmetic_asian.delete('1.0', 'end')
        self.input_strike_price_arithmetic_asian.delete('1.0', 'end')
        self.input_observe_arithmetic_asian.delete('1.0', 'end')

    # Calculate the European option price
    def doEuropeanOption(self):
        try:
            S = (float) (self.input_spot_price_european.get("1.0", "end"))
            K = (float) (self.input_strike_price_european.get("1.0", "end"))
            t = (str) (self.input_start_time_european.get("1.0", "end"))
            T = (str) (self.input_maturity_european.get("1.0", "end"))
            r = (float) (self.input_rise_free_rate_european.get("1.0", "end"))
            q = (float) (self.input_repo_european.get("1.0", "end"))
            sigma = (float) (self.input_volatility_european.get("1.0", "end"))
            option = self.input_option_european.get()
            if option == "Call Option":
                option = 'C'
            else:
                option = 'P'
            result = "Spot Price: " + self.input_spot_price_european.get("1.0","end") + "Strike Price: " + self.input_strike_price_european.get("1.0", "end") + "Start Time: " + t + "End Time: " + T + \
                     "Risk free rate: " + self.input_rise_free_rate_european.get("1.0", "end") + "Volatility: " + self.input_volatility_european.get("1.0", "end") + \
                     "Repo Rate" + self.input_repo_european.get("1.0", "end") + "Option Type: " + self.input_option_european.get()
            result += "\n\n\n" + "Result: " +  str(Black_Schonles_Formulas_new(S, K, t, T, sigma, r, q, option))
            self.european_result.insert(INSERT, result)
        except Exception as result:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    # Calculate the volatility
    def doVolatility(self):
        try:
            S = (float)(self.input_spot_price_volatility.get("1.0", "end"))
            K = (float)(self.input_strike_price_volatility.get("1.0", "end"))
            t = (str)(self.input_start_time_volatility.get("1.0", "end"))
            T = (str)(self.input_maturity_volatility.get("1.0", "end"))
            r = (float)(self.input_rise_free_rate_volatility.get("1.0", "end"))
            q = (float)(self.input_repo_volatility.get("1.0", "end"))
            price = (float)(self.input_option_price_volatility.get("1.0", "end"))
            option = self.input_option_volatility.get()
            if option == "Call Option":
                option = 'C'
            else:
                option = 'P'

            result = "Spot Price: " + self.input_spot_price_volatility.get("1.0", "end") + "Strike Price: " + self.input_strike_price_volatility.get(
                "1.0", "end") + "Start Time: " + t + "End Time: " + T + "Risk free rate: " + self.input_rise_free_rate_volatility.get("1.0","end") + "Option Price: " + self.input_option_price_volatility.get(
                "1.0", "end") + "Repo Rate: " + q + "Option Type: " + self.input_option_volatility.get()
            result += "\n\n\n" + "Result: " + str(Implied_Volatility(S, K, t, T, price, r, q, option))
            self.european_result.insert(INSERT, result)
        except Exception as res:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    def doGeometricAsian(self):
        print("doGeometricAsian")

    def start(self):
        self.top_win.config(menu=self.menus)
        self.top_win.mainloop()


obj = Option_Pricer()
obj.start()

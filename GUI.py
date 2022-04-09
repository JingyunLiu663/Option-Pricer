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
        self.menus.add_command(label="Geometric Basket Option", command=self.useGeometricBasket)
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
        # American
        self.american = tk.Frame(self.top_win, relief='ridge', borderwidth=3)
        # About page
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
        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('Arithmetic Basket Option')
        self.arithmetic_basket.config(bg='white')
        self.setArithmeticBasket()

    def useGeometricBasket(self):
        self.geometric_basket.pack(fill=tk.BOTH, expand=True)
        self.european.pack_forget()
        self.volatility.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.geometric_asian.pack_forget()
        self.arithmetic_basket.pack_forget()
        self.american.pack_forget()
        self.about.pack_forget()
        self.top_win.title('Geometric Basket Option')
        self.geometric_basket.config(bg='white')
        self.setGeometricBasket()


    def useAmerican(self):
        self.american.pack(fill=tk.BOTH, expand=True)
        self.volatility.pack_forget()
        self.arithmetic_asian.pack_forget()
        self.geometric_asian.pack_forget()
        self.arithmetic_basket.pack_forget()
        self.geometric_basket.pack_forget()
        self.european.pack_forget()
        self.about.pack_forget()
        self.top_win.title('American Option')
        self.american.config(bg='white')
        self.setAmerican()


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

        Label(self.arithmetic_asian, text='Result: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=5, column=0, sticky='w')

        Label(self.arithmetic_asian, text='MC Path No.: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(
            row=4, column=0, sticky='w')
        self.input_path_arithmetic_asian = Text(self.arithmetic_asian, height=1, width=23, borderwidth=2)
        self.input_path_arithmetic_asian.grid(row=4, column=1, sticky='w')

        Label(self.arithmetic_asian, text='   Control Variate: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=2, sticky='w')
        self.select_control_arithmetic_asian = StringVar()
        self.input_control_arithmetic_asian = ttk.Combobox(self.arithmetic_asian, width=21,
                                                               textvariable=self.select_control_arithmetic_asian)
        self.input_control_arithmetic_asian.grid(row=3, column=3, sticky='w')
        self.input_control_arithmetic_asian['values'] = ('With control variate', 'Standard MC')
        self.input_control_arithmetic_asian.current(0)

        self.clear_arithmetic_asian = Button(self.arithmetic_asian, text="Clear", width=10,
                                            command=self.clearArithmeticAsian)
        self.clear_arithmetic_asian.place(x=300, y=170)
        self.submit_arithmetic_asian = Button(self.arithmetic_asian, text="Submit", width=10,
                                             command=self.doArithmeticAsian)
        self.submit_arithmetic_asian.place(x=390, y=170)

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
        Label(self.arithmetic_basket, text='Spot Price 1: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=0, column=0, sticky='w', pady=5)
        self.input_spot_price1_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_spot_price1_arithmetic_basket.grid(row=0, column=1, sticky='w')
        Label(self.arithmetic_basket, text='   Spot Price 2: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=0, column=2, sticky='w', pady=5)
        self.input_spot_price2_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_spot_price2_arithmetic_basket.grid(row=0, column=3, sticky='w')

        Label(self.arithmetic_basket, text='Volatility 1: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=0, sticky='w', pady=5)
        self.input_volatility1_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_volatility1_arithmetic_basket.grid(row=1, column=1, sticky='w')
        Label(self.arithmetic_basket, text='   Volatility 2: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=2, sticky='w', pady=5)
        self.input_volatility2_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_volatility2_arithmetic_basket.grid(row=1, column=3, sticky='w')

        Label(self.arithmetic_basket, text='Risk Free Rate: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=0, sticky='w', pady=5)
        self.input_rise_free_rate_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_rise_free_rate_arithmetic_basket.grid(row=2, column=1, sticky='w')
        Label(self.arithmetic_basket, text='   Maturity: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=2, sticky='w', pady=5)
        self.input_maturity_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_maturity_arithmetic_basket.grid(row=2, column=3, sticky='w')

        Label(self.arithmetic_basket, text='Strike Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=0, sticky='w', pady=5)
        self.input_strike_price_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_strike_price_arithmetic_basket.grid(row=3, column=1, sticky='w')
        Label(self.arithmetic_basket, text='   Correlation: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=2, sticky='w', pady=5)
        self.input_correlation_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_correlation_arithmetic_basket.grid(row=3, column=3, sticky='w')

        Label(self.arithmetic_basket, text='Option Type: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=4, column=0, sticky='w', pady=10)
        self.select_option_arithmetic_basket = StringVar()
        self.input_option_arithmetic_basket = ttk.Combobox(self.arithmetic_basket, width=21,
                                                          textvariable=self.select_option_arithmetic_basket)
        self.input_option_arithmetic_basket.grid(row=4, column=1, sticky='w')
        self.input_option_arithmetic_basket['values'] = ('Call Option', 'Put Option')
        self.input_option_arithmetic_basket.current(0)

        Label(self.arithmetic_basket, text='   Control Variate: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=4, column=2, sticky='w', pady=10)
        self.select_control_arithmetic_basket = StringVar()
        self.input_control_arithmetic_basket = ttk.Combobox(self.arithmetic_basket, width=21,
                                                               textvariable=self.select_control_arithmetic_basket)
        self.input_control_arithmetic_basket.grid(row=4, column=3, sticky='w')
        self.input_control_arithmetic_basket['values'] = ('With control variate', 'Standard MC')
        self.input_control_arithmetic_basket.current(0)

        Label(self.arithmetic_basket, text='MC Path No.: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=5, column=0, sticky='w')
        self.input_path_arithmetic_basket = Text(self.arithmetic_basket, height=1, width=23, borderwidth=2)
        self.input_path_arithmetic_basket.grid(row=5, column=1, sticky='w')


        Label(self.arithmetic_basket, text='Result: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=6, column=0, sticky='w')
        self.clear_arithmetic_basket = Button(self.arithmetic_basket, text="Clear", width=10,
                                             command=self.clearArithmeticBasket)
        self.clear_arithmetic_basket.place(x=300, y=178)
        self.submit_arithmetic_basket = Button(self.arithmetic_basket, text="Submit", width=10,
                                              command=self.doArithmeticBasket)
        self.submit_arithmetic_basket.place(x=400, y=178)

        self.result_arithmetic_basket = Text(self.arithmetic_basket, height=10, width=82, borderwidth=2)
        self.result_arithmetic_basket.place(x=5, y=230)


    def setGeometricBasket(self):
        Label(self.geometric_basket, text='Spot Price 1: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=0, column=0, sticky='w', pady=5)
        self.input_spot_price1_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_spot_price1_geometric_basket.grid(row=0, column=1, sticky='w')
        Label(self.geometric_basket, text='   Spot Price 2: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=0, column=2, sticky='w', pady=5)
        self.input_spot_price2_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_spot_price2_geometric_basket.grid(row=0, column=3, sticky='w')

        Label(self.geometric_basket, text='Volatility 1: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=0, sticky='w', pady=5)
        self.input_volatility1_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_volatility1_geometric_basket.grid(row=1, column=1, sticky='w')
        Label(self.geometric_basket, text='   Volatility 2: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=2, sticky='w', pady=5)
        self.input_volatility2_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_volatility2_geometric_basket.grid(row=1, column=3, sticky='w')

        Label(self.geometric_basket, text='Risk Free Rate: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=0, sticky='w', pady=5)
        self.input_rise_free_rate_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_rise_free_rate_geometric_basket.grid(row=2, column=1, sticky='w')
        Label(self.geometric_basket, text='   Maturity: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=2, sticky='w', pady=5)
        self.input_maturity_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_maturity_geometric_basket.grid(row=2, column=3, sticky='w')

        Label(self.geometric_basket, text='Strike Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=0, sticky='w', pady=5)
        self.input_strike_price_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_strike_price_geometric_basket.grid(row=3, column=1, sticky='w')
        Label(self.geometric_basket, text='   Correlation: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=2, sticky='w', pady=5)
        self.input_correlation_geometric_basket = Text(self.geometric_basket, height=1, width=23, borderwidth=2)
        self.input_correlation_geometric_basket.grid(row=3, column=3, sticky='w')

        Label(self.geometric_basket, text='Option Type: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=4, column=0, sticky='w', pady=10)
        self.select_option_geometric_basket = StringVar()
        self.input_option_geometric_basket = ttk.Combobox(self.geometric_basket, width=21,
                                                          textvariable=self.select_option_geometric_basket)
        self.input_option_geometric_basket.grid(row=4, column=1, sticky='w')
        self.input_option_geometric_basket['values'] = ('Call Option', 'Put Option')
        self.input_option_geometric_basket.current(0)

        Label(self.geometric_basket, text='   Calculation: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=4, column=2, sticky='w', pady=10)
        self.select_calcualtion_geometric_basket = StringVar()
        self.input_calcualtion_geometric_basket = ttk.Combobox(self.geometric_basket, width=21,
                                                              textvariable=self.select_calcualtion_geometric_basket)
        self.input_calcualtion_geometric_basket.grid(row=4, column=3, sticky='w')
        self.input_calcualtion_geometric_basket['values'] = ('Closed-Form Fomula', 'Standard MC')
        self.input_calcualtion_geometric_basket.current(0)

        Label(self.geometric_basket, text='Result: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=5, column=0, sticky='w')
        self.clear_geometric_basket = Button(self.geometric_basket, text="Clear", width=10,
                                             command=self.clearGeometricBasket)
        self.clear_geometric_basket.place(x=120, y=178)
        self.submit_geometric_basket = Button(self.geometric_basket, text="Submit", width=10,
                                              command=self.doGeometricBasket)
        self.submit_geometric_basket.place(x=210, y=178)

        self.result_geometric_basket = Text(self.geometric_basket, height=11, width=82, borderwidth=2)
        self.result_geometric_basket.place(x=5, y=210)

    def setAmerican(self):
        Label(self.american, text='Spot Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=0, column=0, sticky='w', pady=5)
        self.input_spot_price_american = Text(self.american, height=1, width=23, borderwidth=2)
        self.input_spot_price_american.grid(row=0, column=1, sticky='w')
        Label(self.american, text='   Strike Price: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=0, column=2, sticky='w', pady=5)
        self.input_strike_american = Text(self.american, height=1, width=23, borderwidth=2)
        self.input_strike_american.grid(row=0, column=3, sticky='w')

        Label(self.american, text='Risk Free Rate: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=0, sticky='w', pady=5)
        self.input_rise_free_rate_american = Text(self.american, height=1, width=23, borderwidth=2)
        self.input_rise_free_rate_american.grid(row=1, column=1, sticky='w')

        Label(self.american, text='   Maturity: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=1, column=2, sticky='w', pady=5)
        self.input_maturity_american = Text(self.american, height=1, width=23, borderwidth=2)
        self.input_maturity_american.grid(row=1, column=3, sticky='w')

        Label(self.american, text='Volatility: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=0, sticky='w', pady=5)
        self.input_volatility_american = Text(self.american, height=1, width=23, borderwidth=2)
        self.input_volatility_american.grid(row=2, column=1, sticky='w')

        Label(self.american, text='   Steps No.: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=2, column=2, sticky='w', pady=5)
        self.input_steps_american = Text(self.american, height=1, width=23, borderwidth=2)
        self.input_steps_american.grid(row=2, column=3, sticky='w')

        Label(self.american, text='Option Type: ', fg='black', bg='white',
              font=("Times New Roman", 12, "bold")).grid(
            row=3, column=0, sticky='w', pady=10)
        self.select_option_american = StringVar()
        self.input_option_american = ttk.Combobox(self.american, width=21,
                                                          textvariable=self.select_option_american)
        self.input_option_american.grid(row=3, column=1, sticky='w')
        self.input_option_american['values'] = ('Call Option', 'Put Option')
        self.input_option_american.current(0)

        self.clear_american = Button(self.american, text="Clear", width=10,
                                             command=self.clearAmerican)
        self.clear_american.place(x=320, y=110)
        self.submit_american = Button(self.american, text="Submit", width=10,
                                              command=self.doAmerican)
        self.submit_american.place(x=410, y=110)

        Label(self.american, text='Result: ', fg='black', bg='white', font=("Times New Roman", 12, "bold")).grid(row=4, column=0, sticky='w')
        self.result_american = Text(self.american, height=13, width=82, borderwidth=2)
        self.result_american.place(x=5, y=175)






    def setAbout(self):
        # self.about.grid(row=0, column=0, sticky='w')
        Label(self.about, text='Option Pricier', fg='black', bg='white',
                            font=("Times New Roman", 18, "bold")).grid(row=0, column=0, sticky='w')
        Label(self.about, text="1. Introduction", fg='black', bg='white',
                             font=("Times New Roman", 13, "bold")).grid(row=1, column=0, sticky='w')
        intro_contents1 = "* The option pricier has three option categories, including European Option, Asian Option"
        intro_contents2 = "and American Option. Users can use the top menu to select type."
        intro_contents3 = "* Fill in all blanks and click calculate button, the result will be shown."
        Label(self.about, text=intro_contents1, fg='black', bg='white',
                             font=("Times New Roman", 10)).grid(row=2, column=0, sticky='w')
        Label(self.about, text=intro_contents2, fg='black', bg='white',
                             font=("Times New Roman", 10)).grid(row=3, column=0, sticky='w')
        Label(self.about, text=intro_contents3, fg='black', bg='white',
                             font=("Times New Roman", 10)).grid(row=4, column=0, sticky='w')
        Label(self.about, text="2. About", fg='black', bg='white', font=("Times New Roman", 13, "bold")).grid(
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
        # self.input_option_european['values'] = ('Call Option', 'Put Option')
        self.input_option_european.current(0)
        self.european_result.delete('1.0', 'end')

    # Clear all fields in the volatility page
    def clearVolatility(self):
        self.input_spot_price_volatility.delete('1.0', 'end')
        self.input_maturity_volatility.delete('1.0', 'end')
        self.input_rise_free_rate_volatility.delete('1.0', 'end')
        self.input_repo_volatility.delete('1.0', 'end')
        self.input_option_price_volatility.delete('1.0', 'end')
        self.input_strike_price_volatility.delete('1.0', 'end')
        # self.input_option_volatility['values'] = ('Call Option', 'Put Option')
        self.input_option_volatility.current(0)
        self.result_volatility.delete('1.0', 'end')

    def clearGeometricAsian(self):
        self.input_maturity_geometric_asian.delete('1.0', 'end')
        self.input_rise_free_rate_geometric_asian.delete('1.0', 'end')
        self.input_volatility_geometric_asian.delete('1.0', 'end')
        self.input_spot_price_geometric_asian.delete('1.0', 'end')
        self.input_strike_price_geometric_asian.delete('1.0', 'end')
        self.input_observe_geometric_asian.delete('1.0', 'end')
        # self.input_calcualtion_geometric_asian['values'] = ('Closed-Form Fomula', 'Standard MC')
        self.input_calcualtion_geometric_asian.current(0)
        # self.input_option_geometric_asian['values'] = ('Call Option', 'Put Option')
        self.input_option_geometric_asian.current(0)
        self.result_geometric_asian.delete('1.0', 'end')


    # Clear all fields of Arithmetic Asian Option
    def clearArithmeticAsian(self):
        self.input_maturity_arithmetic_asian.delete('1.0', 'end')
        self.input_rise_free_rate_arithmetic_asian.delete('1.0', 'end')
        self.input_volatility_arithmetic_asian.delete('1.0', 'end')
        self.input_spot_price_arithmetic_asian.delete('1.0', 'end')
        self.input_strike_price_arithmetic_asian.delete('1.0', 'end')
        self.input_observe_arithmetic_asian.delete('1.0', 'end')
        self.input_path_arithmetic_asian.delete('1.0', 'end')
        self.input_option_arithmetic_asian.current(0)
        self.input_control_arithmetic_asian.current(0)
        self.result_arithmetic_asian.delete('1.0', 'end')

    # Clear all fields of Arithmetic Basket Option
    def clearArithmeticBasket(self):
        self.input_spot_price1_arithmetic_basket.delete('1.0', 'end')
        self.input_spot_price2_arithmetic_basket.delete('1.0', 'end')
        self.input_volatility1_arithmetic_basket.delete('1.0', 'end')
        self.input_volatility2_arithmetic_basket.delete('1.0', 'end')
        self.input_strike_price_arithmetic_basket.delete('1.0', 'end')
        self.input_rise_free_rate_arithmetic_basket.delete('1.0', 'end')
        self.input_maturity_arithmetic_basket.delete('1.0', 'end')
        self.input_correlation_arithmetic_basket.delete('1.0', 'end')
        self.input_path_arithmetic_basket.delete('1.0', 'end')
        self.input_option_arithmetic_basket.current(0)
        self.input_control_arithmetic_basket.current(0)
        self.result_arithmetic_basket.delete('1.0', 'end')


    # Clear all fields of Geometric Basket Option
    def clearGeometricBasket(self):
        self.input_spot_price1_geometric_basket.delete('1.0', 'end')
        self.input_spot_price2_geometric_basket.delete('1.0', 'end')
        self.input_volatility1_geometric_basket.delete('1.0', 'end')
        self.input_volatility2_geometric_basket.delete('1.0', 'end')
        self.input_strike_price_geometric_basket.delete('1.0', 'end')
        self.input_rise_free_rate_geometric_basket.delete('1.0', 'end')
        self.input_maturity_geometric_basket.delete('1.0', 'end')
        self.input_correlation_geometric_basket.delete('1.0', 'end')
        self.input_option_geometric_basket.current(0)
        self.input_calcualtion_geometric_basket.current(0)
        self.result_arithmetic_basket.delete('1.0', 'end')

    # Clear all fields in American Option
    def clearAmerican(self):
        self.input_spot_price_american.delete('1.0', 'end')
        self.input_maturity_american.delete('1.0', 'end')
        self.input_strike_american.delete('1.0', 'end')
        self.input_volatility_american.delete('1.0', 'end')
        self.input_rise_free_rate_american.delete('1.0', 'end')
        self.input_steps_american.delete('1.0', 'end')
        self.input_option_american.current(0)



    # Calculate the European option price
    def doEuropeanOption(self):
        try:
            S = (float) (self.input_spot_price_european.get("1.0", "end"))
            K = (float) (self.input_strike_price_european.get("1.0", "end"))
            T = (float) (self.input_maturity_european.get("1.0", "end"))
            print(T)
            r = (float) (self.input_rise_free_rate_european.get("1.0", "end"))
            q = (float) (self.input_repo_european.get("1.0", "end"))
            sigma = (float) (self.input_volatility_european.get("1.0", "end"))
            option = self.input_option_european.get()
            if option == "Call Option":
                option = 'C'
            else:
                option = 'P'

            # result = "Spot Price: " + S + "Strike Price: " + K + "End Time: " + T + \
            #          "Risk free rate: " + r + "Volatility: " + sigma + \
            #          "Repo Rate" + q + "Option Type: " + self.input_option_european.get()
            result = Black_Schonles_Formulas_new(S, K, 0, T, sigma, r, q, option)
            self.european_result.insert(INSERT, result)
        except Exception as result:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    # Calculate the volatility
    def doVolatility(self):
        try:
            S = (float) (self.input_spot_price_volatility.get("1.0", "end"))
            K = (float) (self.input_strike_price_volatility.get("1.0", "end"))
            T = (float) (self.input_maturity_volatility.get("1.0", "end"))
            r = (float) (self.input_rise_free_rate_volatility.get("1.0", "end"))
            q = (float) (self.input_repo_volatility.get("1.0", "end"))
            price = (float) (self.input_option_price_volatility.get("1.0", "end"))
            option = self.input_option_volatility.get()
            if option == "Call Option":
                option = 'C'
            else:
                option = 'P'

            # result = "Spot Price: " + self.input_spot_price_volatility.get("1.0", "end") + "Strike Price: " + self.input_strike_price_volatility.get(
            #     "1.0", "end") + "End Time: " + T + "Risk free rate: " + self.input_rise_free_rate_volatility.get("1.0","end") + "Option Price: " + self.input_option_price_volatility.get(
            #     "1.0", "end") + "Repo Rate: " + q + "Option Type: " + self.input_option_volatility.get()
            result = Implied_Volatility(S, K, 0, T, price, r, q, option)
            self.european_result.insert(INSERT, result)
        except Exception as res:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    def doArithmeticAsian(self):
        try:
            S = (float) (self.input_spot_price_arithmetic_asian.get("1.0", "end"))
            K = (float) (self.input_strike_price_arithmetic_asian.get("1.0", "end"))
            r = (float) (self.input_rise_free_rate_arithmetic_asian.get("1.0", "end"))
            T = (float) (self.input_maturity_arithmetic_asian.get("1.0", "end"))
            sigma = (float) (self.input_volatility_arithmetic_asian.get("1.0", "end"))
            observe_num = (float) (self.input_observe_arithmetic_asian.get("1.0", "end"))
            path_num = (float) (self.input_path_arithmetic_asian.get("1.0", "end"))
            option = self.input_option_arithmetic_asian.get()
            control = self.input_control_arithmetic_asian.get()
            # Result here *******
            # result = 调你们的函数
            # self.result_arithmetic_asian.insert((INSERT, result)


        except Exception as res:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    def doGeometricAsian(self):
        try:
            S = (float) (self.input_spot_price_geometric_asian.get("1.0", "end"))
            K = (float) (self.input_strike_price_geometric_asian.get("1.0", "end"))
            r = (float) (self.input_rise_free_rate_geometric_asian.get("1.0", "end"))
            T = (float) (self.input_maturity_geometric_asian.get("1.0", "end"))
            sigma = (float) (self.input_volatility_geometric_asian.get("1.0", "end"))
            observe_num = (float) (self.input_observe_geometric_asian.get("1.0", "end"))
            option = self.input_option_geometric_asian.get()
            calcualtion = self.input_calcualtion_geometric_asian.get()
            # Result here *******
            # result = 调你们的函数
            # self.result_geometric_asian(INSERT, result)

        except Exception:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    def doArithmeticBasket(self):
        print("Arithmetic Basket")
        try:
            S1 = (float) (self.input_spot_price1_arithmetic_basket.get("1.0", "end"))
            S2 = (float) (self.input_spot_price2_arithmetic_basket.get("1.0", "end"))
            sigma1 = (float) (self.input_volatility1_arithmetic_basket.get("1.0", "end"))
            sigma2 = (float) (self.input_volatility2_arithmetic_basket.get("1.0", "end"))
            r = (float) (self.input_rise_free_rate_arithmetic_basket.get("1.0", "end"))
            T = (float) (self.input_maturity_arithmetic_basket.get("1.0", "end"))
            K = (float) (self.input_strike_price_arithmetic_basket.get("1.0", "end"))
            correlation = (float) (self.input_correlation_arithmetic_basket.get("1.0", "end"))
            path = (float) (self.input_path_arithmetic_basket.get("1.0", "end"))
            option = self.input_option_arithmetic_basket.get()
            control = self.input_control_arithmetic_basket.get()
            # Result here *******
            # result = 调你们的函数
            # self.result_arithmetic_basket(INSERT, result)

        except Exception as res:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    def doGeometricBasket(self):
        print("Geometric Basket")
        try:
            S1 = (float)(self.input_spot_price1_geometric_basket.get("1.0", "end"))
            S2 = (float)(self.input_spot_price2_geometric_basket.get("1.0", "end"))
            sigma1 = (float)(self.input_volatility1_geometric_basket.get("1.0", "end"))
            sigma2 = (float)(self.input_volatility2_geometric_basket.get("1.0", "end"))
            r = (float)(self.input_rise_free_rate_geometric_basket.get("1.0", "end"))
            T = (float)(self.input_maturity_geometric_basket.get("1.0", "end"))
            K = (float)(self.input_strike_price_geometric_basket.get("1.0", "end"))
            correlation = (float)(self.input_correlation_geometric_basket.get("1.0", "end"))
            option = self.input_option_geometric_basket.get()
            calculation = self.input_calcualtion_geometric_basket.get()
            # Result here **************
            # result = 调你们的函数
            # self.result_geometric_basket(INSERT, result)

        except Exception as res:
            messagebox.showerror('Error', 'Input format error, please check your input.')

    def doAmerican(self):
        print("American")
        try:
            S = (float) (self.input_spot_price_american.get("1.0", "end"))
            sigma = (float) (self.input_volatility_american.get("1.0", "end"))
            r = (float)(self.input_rise_free_rate_american.get("1.0", "end"))
            T = (float)(self.input_maturity_american.get("1.0", "end"))
            K = (float)(self.input_strike_american.get("1.0", "end"))
            steps_num = (float) (self.input_steps_american.get("1.0", "end"))
            option = self.input_option_american.get()
            # Result here **************
            # result = 调你们的函数
            # self.result_american(INSERT, result)

        except Exception as res:
            messagebox.showerror('Error', 'Input format error, please check your input.')


    def start(self):
        self.top_win.config(menu=self.menus)
        self.top_win.mainloop()


obj = Option_Pricer()
obj.start()

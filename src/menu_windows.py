from tkinter import *
import company_stock_info
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
import tkinter as tk
import descriptive_analytics_menu
import predictive_analytics_menu


def opt_main_menu(window):
    window.destroy()
    starting_window()


def starting_window():
    window = Tk()
    window.title("Welcome to the Stock Analysis app")
    window.geometry('600x400')
    
    inset = "Stock Trader"
    Label(window, text="""Welcome to the {} application""".format(inset)).pack()
    
    def opt_proceed():
        window.destroy()
        stock_menu_window()
    
    Button(window, text="Proceed", command = opt_proceed).pack()
    Button(window, text="Quit", command = window.destroy).pack()
    
    window.mainloop()


def stock_menu_window():
    window = Tk()
    window.title("Stock Menu")
     
    window.geometry('600x400')
     
    lbl = Label(window, text="""You are now at the stock code menu. Please enter a company name or code 
                              in the box provided below and click the 'Search Company' button. If
                              the name/code is invalid you will not proceed to the next window.""").pack()
    
    # Entry(window, width=10).pack()
    
    def opt_proceed(stock_code):
        window.destroy()
        stock_exploration_window(stock_code)
    
    def opt_quit():
        window.destroy()
        exit()
        
    def user_input():
        print(entry.get())
        df = company_stock_info.get_company_names()
        print(list(df.columns))
        
        if (entry.get().upper() in df.index) or (entry.get().lower in df.Name):
            print("Success with list")
            stock_code = entry.get()
            opt_proceed(stock_code)
        
        else:
            Label(window, text = "Invalid entry, please try again").pack()
       
            
    entry = Entry(window, width=10)
    entry.bind("<Button-1>", user_input)
    entry.pack()
    
    Button(window, text="Search Company", command=user_input).pack()
    Button(window, text="Quit", command = window.destroy).pack()
    Button(window, text="Main Menu", command = lambda: opt_main_menu(window)).pack()
    
    window.mainloop()
    
    
def stock_exploration_window(stock_code):
    window = Tk()
    window.title("Welcome to the stock exploration, Please select an option below")
    window.geometry('600x400')
    
    Label(window, text="""Please select a valid option""").pack()
    
    def opt_descriptive():
        window.destroy()
        des_fourth_window(stock_code)
    
    def opt_predictive():
        window.destroy()
        pred_fourth_window(stock_code)
    
    def opt_back():
        window.destroy()
        stock_menu_window()
    
    
    Button(window, text="Descriptive Analytics", command=opt_descriptive).pack()
    Button(window, text="Predictive Analytics", command = opt_predictive).pack()
    Button(window, text="Back", command = opt_back).pack()
    Button(window, text="Main Menu", command = lambda: opt_main_menu(window)).pack()
    Button(window, text="Quit", command = window.destroy).pack()
    
    window.mainloop()
    
def des_fourth_window(stock_code):
    window = Tk()
    window.title("Descriptive Analytics Menu")
    window.geometry('600x400')
    
    Label(window, text="""Please select an option """).pack()
    
    def basic_statistics():
        
        var = 'basic statistics'
        calendar_window(window, stock_code, var)
        
        # company_stock_info.get_basic_statistics(x, stock_code)
        # display_basic_statistics(dates, stock_code)
        
    def opt_b():
        lbl.configure(text= "You chose option b")
        print("In the clear")
        window.destroy()
        exit()
    
    def opt_back():
        window.destroy()
        stock_exploration_window(stock_code)
        
        
    def opt_other_stats():
        window.destroy()
        other_stats_window(stock_code)
    
    Button(window, text="Basic Statistics", command=basic_statistics).pack()
    Button(window, text="Other Statistics", command = opt_other_stats).pack()
    Button(window, text="Back", command = opt_back).pack()
    Button(window, text="Main Menu", command = lambda: opt_main_menu(window)).pack()
    Button(window, text="Quit", command = window.destroy).pack()
    
    window.mainloop()

def pred_fourth_window(stock_code):    
    window = Tk()
    window.title("Predictive Analytics Menu")
    window.geometry('600x400')
    
    Label(window, text="""Please select an option """).pack()
    
    print("In fourth descriptive window")
    
    def opt_back():
        window.destroy()
        stock_exploration_window(stock_code)
        
        
    def opt_lin_reg():
        caller = "linear regression"
        calendar_window(window, stock_code, caller)
        
        
    Button(window, text="Linear Regression", command=opt_lin_reg).pack()
    Button(window, text="Main Menu",command = lambda: opt_main_menu(window)).pack()
    Button(window, text="Back", command = opt_back).pack()
    Button(window, text="Quit", command = window.destroy).pack()
    
    window.mainloop()


def basic_statistics_window(stats_dict, dates, stock_code):
    window = Tk()
    window.title("Basic Statistics Menu")
    window.geometry('600x400')
    
    top = "=============== Basic Statistics ================"
    row1 = "| " + "Mean " + "   =   " + str(stats_dict['Mean']) + " |"
    row2 = "| " + "Median " + "   =   " + str(stats_dict['Median']) + " |"
    row3 = "| " + "1st Quartile " + "   =   " + str(stats_dict['1stQ']) + " |"
    row4 = "| " + "3rd Quartile " + "   =   " + str(stats_dict['3rdQ']) + " |"
    row5 = "| " + "Inter Quartile Range " + "   =   " + str(stats_dict['Inter_Quartile_Range']) + " |"
    row6 = "| " + "Max " + "   =   " + str(stats_dict['Max']) + " |"
    row7 = "| " + "Min " + "   =   " + str(stats_dict['Min']) + " |"
    row8 = "| " + "Range " + "   =   " + str(stats_dict['Range']) + " |"
    row9 = "| " + "Standard Deviation " + "   =   " + str(stats_dict['Standard_Deviation']) + " |"
    row10 = "| " + "Coef of Variation " + "   =   " + str(stats_dict['Coef_of_variation']) + " |"
    row11 = "| " + "Variance " + "   =   " + str(stats_dict['Variance']) + " |"
    bottom = "=" * 40
    
    Label(window, text = """Basic Statistics for the stock code {} for the time frame {} to {}""".format(stock_code, dates[0], dates[1])).pack()
    Label(window, text= top).pack()
    Label(window, text= row1).pack()
    Label(window, text= row2).pack()
    Label(window, text= row3).pack()
    Label(window, text= row4).pack()
    Label(window, text= row5).pack()
    Label(window, text= row6).pack()
    Label(window, text= row7).pack()
    Label(window, text= row8).pack()
    Label(window, text= row9).pack()
    Label(window, text= row10).pack()
    Label(window, text= row11).pack()
    Label(window, text= bottom).pack()
    
    
    window.mainloop()


# global dates
# dates = []

    
def calendar_window(window, stock_code, caller):
    
    dates = []
    def process_choice():
        
        print(calendar.selection_get())
        if(calendar.selection_get().year > 2019):
            print_warning_window(stock_code, caller)
            
        if len(dates) < 2:
            dates.append(calendar.selection_get())
            print("Contents of dates: ")
            print(dates)
            if len(dates) == 1:
                print_additional_date_window(stock_code, caller)
                
            if len(dates) == 2:
                print_inform_done_window(stock_code, caller)
                
            
        else:
            dates.sort()
            top.destroy()
            if(caller == 'basic statistics'):
                 stats_dict = company_stock_info.get_basic_statistics(dates, stock_code)
                 basic_statistics_window(stats_dict, dates, stock_code)
            if(caller == 'moving average'):
                print("moving average")
                descriptive_analytics_menu.moving_average(dates, stock_code)
            if(caller == 'expected returns'):
                descriptive_analytics_menu.expected_returns(dates, stock_code)
            if(caller == 'time series'):
                descriptive_analytics_menu.raw_time_series(dates, stock_code)
            if(caller == 'weighted moving average'):
                descriptive_analytics_menu.weighted_moving_average(dates, stock_code)
            if(caller == 'MACD'):
                descriptive_analytics_menu.macd(dates, stock_code)
            if(caller == 'linear regression'):
                number_input_window(dates, stock_code)
            
        
            ## Now it has to do something, slice the data, display statistics
    def proceed():
        
        if len(dates) == 2:
             # window.destroy()
             top.destroy()
             # send_to_calendar(x)
             print("Will it return?")
             if(caller == 'basic statistics'):
                 stats_dict = company_stock_info.get_basic_statistics(dates, stock_code)
                 basic_statistics_window(stats_dict, dates, stock_code) 
             if(caller == 'moving average'):
                 descriptive_analytics_menu.moving_average(dates, stock_code)
             if(caller == 'expected returns'):
                 descriptive_analytics_menu.expected_returns(dates, stock_code)
             if(caller == 'time series'):
                 descriptive_analytics_menu.raw_time_series(dates, stock_code)
             if(caller == 'weighted moving average'):
                 descriptive_analytics_menu.weighted_moving_average(dates, stock_code)
             if(caller == 'MACD'):
                 descriptive_analytics_menu.macd(dates, stock_code)
             if(caller == 'linear regression'):
                 number_input_window(dates, stock_code)
                
        else:
            temp = Tk()
            temp.title("Warning message")
            temp.geometry('400x300')
            Label(temp, text="Please enter another date").pack()
            temp.mainloop()
            
    top = tk.Toplevel(window)
    calendar = Calendar(top,
                   font="Calibri 16", selectmode='day',
                   cursor="hand1", title = "Hello", day=1, month=1, year=2019)
    calendar.pack(fill="both", expand=True)
    ttk.Button(top, text="Select", command=process_choice).pack()
    ttk.Button(top, text="Done", command=proceed).pack()


def other_stats_window(stock_code):
    
    window = Tk()
    window.title("Other Statisctics Window")
    window.geometry('600x400')
    
    def opt_pred_main_menu():
        window.destroy()
        pred_fourth_window(stock_code)
        
    def opt_mov_average():
        window.destroy()
        # mov_avg_window(stock_code)
        flag = "moving average"
        elite_window(stock_code, flag)
    def opt_exp_returns():
        window.destroy()
        flag = "expected returns"
        elite_window(stock_code, flag)
        # exp_returns_window(stock_code)
    
    def opt_time_series():
        window.destroy()
        flag = "time series"
        elite_window(stock_code, flag)
        # time_series_window(stock_code)
    
    def opt_wmov_avg():
        window.destroy()
        flag = "weighted moving average"
        elite_window(stock_code, flag)
        # wmov_avg_window(stock_code)
        
    def opt_macd():
        window.destroy()
        flag = "MACD"
        elite_window(stock_code, flag)
        # macd_window(stock_code)
        
    def opt_back():
        window.destroy()
        des_fourth_window(stock_code)
            
    Label(window, text="Please select which statistic you would like to see").pack()
    Button(window, text="Moving Average", command = opt_mov_average).pack()
    Button(window, text="Expected Returns", command = opt_exp_returns).pack()
    Button(window, text="Raw Time Series", command = opt_time_series).pack()
    Button(window, text="Weighted Moving Average", command = opt_wmov_avg).pack()
    Button(window, text="MACD", command = opt_macd).pack()
    Button(window, text="Back", command = opt_back).pack()
    Button(window, text="Main Menu",command = lambda: opt_main_menu(window)).pack()
    Button(window, text="Quit", command = window.destroy).pack()
    
    window.mainloop()


def elite_window(stock_code, flag):
    window = Tk()
    window.title("{} window".format(flag))
    window.geometry('600x400')
    
    def opt_back():
        window.destroy()
        other_stats_window(stock_code)
    
    
    Label(window, text="""You are at the {} window. Please click on 
             proceed if you wish to continue, otherwise click back to return 
             to the main menu""".format(flag)).pack()
    
    Button(window, text="Proceed", command = lambda: calendar_window(window, stock_code, flag)).pack()
    Button(window, text="Back", command = opt_back).pack()
    Button(window, text="Main Menu",command = lambda: opt_main_menu(window)).pack()
    Button(window, text="Quit", command = window.destroy).pack()
    window.mainloop()

    
def number_input_window(dates, stock_code):
    window = Tk()
    window.title("Number input window")
    window.geometry('600x400')
    
    def user_input():
        inp = entry.get()
        num_days = int(inp)
        predictive_analytics_menu.linearRegression(dates, stock_code, num_days)
        window.destroy()
    
    Label(window, text="Please enter the number of days to predict in advance").pack()
    entry = Entry(window, width=10)
    entry.bind("<Button-1>", user_input)
    entry.pack()
    
    Button(window, text="Confirm", command=user_input).pack()
    window.mainloop()


def print_warning_window(stock_code, caller):
    
    window = Tk()
    window.title("Warning")
    window.geometry('400x300')
    
    Label(window, text="Please enter a valid date").pack()
    
    def proceed():
        window.destroy()
        calendar_window(window, stock_code, caller)
        
    Button(window, text="Okay", command = proceed).pack()
    window.mainloop()

def print_additional_date_window(stock_code, caller):
    
    window = Tk()
    window.title("Warning")
    window.geometry('400x300')
    
    Label(window, text="Please enter another date").pack()
    
    def proceed():
        window.destroy()
        # calendar_window(window, stock_code, caller)
        
    Button(window, text="Okay", command = proceed).pack()
    window.mainloop()

def print_inform_done_window(stock_code, caller):
    
    window = Tk()
    window.title("Warning")
    window.geometry('400x300')
    
    Label(window, text="If you have two dates entered, please press 'done' to proceed").pack()
    
    def proceed():
        window.destroy()
        # calendar_window(window, stock_code, caller)
        
    Button(window, text="Okay", command = proceed).pack()
    window.mainloop()

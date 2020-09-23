import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
from scipy.stats import linregress
import matplotlib as mpl
import tkinter 



from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import company_stock_info

#Adjusting matplotlib
mpl.rc('figure', figsize=(8,7))
style.use('ggplot')


def getStockData():
    stock = input("What Stock would you like to analyze")
    
    start_year = int(input("What year would you like as start year?"))
    end_year = int(input("What year would you like as end year?"))
    
    start_time = datetime.datetime(start_year, 1, 1)
    end_time = datetime.datetime(end_year, 1, 1)
    
    #Download Apple stocks from Yahoo API for the given times
    df = web.DataReader(stock, 'yahoo', start_time, end_time)
    print(list(df.columns))
    print("THE DATAFRAME")
    print(df.head())
    print(df.info())
    
    #print(df)
    return df

def raw_time_series(dates, stock_code):
    df = company_stock_info.filter_dataset(dates, stock_code)
    
    close_px = df['adjusted_close']
    x_label = "Raw Time Series"
    
    draw_graph(dates, df['timestamp'], close_px, x_label)
    

#Rolling Mean/Moving Average smooths out price data by creating a constantly updated average price
#The moving average acts as resistance meaning from the downtrend and uptrend of stocks you could expect it will follow the trend and will be less likely to deviate from resistance point
def moving_average(dates, stock_code):#x is the list
    # df = self.getStockData()
    
    df = company_stock_info.filter_dataset(dates, stock_code)
    print(df.info())
    print("AT MOVING AVERAGE")
    close_px = df['adjusted_close']
 
    #window is the size of the moving window
    #Loops through the dataframe and gets the windows of size 100, calculates mean for each window
    #Moving average steadily rises over the window2012
    mavg = close_px.rolling(window =100).mean()
    #print(mavg)
    
    
######## Stephen's Input #############        
    
    x_label = "Closing Price"
    y_label = "Rolling Average"
    
    
    draw_graph(dates, df['timestamp'], close_px, x_label, mavg, y_label)

    
    
    
  ########## END of Stephen's Input ##############      
    
    #Moving average can be used to predict when to buy/sell stocks 
    #i.e. sell during downturn buy during upturn
    # close_px.plot(label = "AAPL")
    # mavg.plot(label="Moving Average")
    # plt.legend()

def weighted_moving_average(dates, stock_code):
    df = company_stock_info.filter_dataset(dates, stock_code)
    close_px = df['adjusted_close']
    # numOfDays = int(input("For what window (i.e. number of days) would you like a weighted moving average (WMA) calculated?"))
    #Adjust = False specifies that we want to use recursive calculation mode
    #EMA (Exponential Moving Average) reduces lag in traditional MA by putting more weight on recent observations
    #Span is provided by the user and the function automatically generates the decay
    
    num_of_days = 50
    wmavg = close_px.ewm(span=num_of_days, adjust=False).mean()
    
    x_label = "Closing Price"
    y_label = "Weighted Moving Average"
    
    draw_graph(dates, df['timestamp'], close_px, x_label, wmavg, y_label)
#Calculate Moving Average Convergence Divergence
#MACD is a trend following momentumm indicator that shows the relationship between 2 moving averages of a security's price
#MACD Formula: 12 day EMA - 26 day EMA
def macd(dates, stock_code):
    df = company_stock_info.filter_dataset(dates, stock_code)
    close_px = df['adjusted_close']  
    df['12 ema'] = close_px.ewm(span=12, adjust=False).mean()
    df['26 ema'] = close_px.ewm(span=26, adjust=False).mean()
    
    df['MACD'] = (df['12 ema'] - df['26 ema'])
    x_label = "Closing Price"
    y_label = "MACD"
    
    draw_graph(dates, df['timestamp'], close_px, x_label, df['MACD'], y_label)


#Expected return measures the mean, or expected value, of the probability distribution of investment returns 
#Ideal stocks should return as high and stable as possible
def expected_returns(dates, stock_code):
    df = company_stock_info.filter_dataset(dates, stock_code)
    
    close_px = df['adjusted_close']
    x_label = "Closing Price"
    y_label = "Expected Returns"
    #df.shift(i) shifts the entire dataframe i units down
    #This gets return i/return i-1
    rets = close_px/close_px.shift(1) - 1
    draw_graph(dates, df['timestamp'], close_px, x_label, rets,  y_label)
    
#if __name__ =="__main__":
 #   displayOptions()


def draw_graph(dates, df, x, x_label, y=None, y_label=None):
    
    print("In the graph function")
    window = tkinter.Tk()
    window.wm_title("Resulting Graph")
    
    start_date = dates[0].strftime("%Y-%m-%d")
    end_date = dates[1].strftime("%Y-%m-%d")
    

    fig = Figure(figsize=(8, 8), dpi=100)
    # fig.add_subplot(111).plot(df, x, label=x_label)
    fig2 = fig.add_subplot(111)
    fig2.set_xlabel("From {} to {}".format(start_date, end_date))
    fig2.set_ylabel("Numerical Value for Stock")
    fig2.plot(df, x, label=x_label)
    
    
    
    if(type(y) is Series):
        if (y.empty == False) & (y_label != None):
             fig3 = fig.add_subplot(111)
             fig3.set_xlabel("From {} to {}".format(start_date, end_date))
             fig3.set_ylabel("Numerical Value for Stock")
             fig3.plot(df, y, label=y_label)
        
    if(type(y) is None):
        if y_label != None:
            fig3 = fig.add_subplot(111)
            fig3.set_xlabel("From {} to {}".format(start_date, end_date))
            fig3.set_ylabel("Numerical Value for Stock")
            fig3.plot(df, y, label=y_label)
            
    fig.legend()
    
    picture = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    picture.draw()
    picture.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    button1 = tkinter.Button(master=window, text="Quit", command= window.destroy)
    button1.pack(side=tkinter.BOTTOM)
    
    

    tkinter.mainloop()
    
    
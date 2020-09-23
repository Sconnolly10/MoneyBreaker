# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:36:00 2019

@author: steph
"""

# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn import neighbors
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
import company_stock_info
from pandas import Series, DataFrame

import tkinter 



from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


#mpl.rcParams['backend'] = "qt4agg"
#mpl.rcParams['backend.qt4'] = "PySide"


#Must have the self variable as a parameter  as this is a class method not a free function
#Self is an instance of the class
#To call this method we must first instantiate an object of the class
def displayOptions():
    choice = input("What would you like to do 1. Linear Regression \n Q to quit")
    if(choice=="1"):
        self.linearRegression()
    elif(choice=="2"):
        self.SVM()
    elif(choice.upper()=="Q"):
        print("You have exited the system")
    else:
        print("Incorrect input, must be in range specified")


def getStockData(x, stock_code):
    
    start_time = x[0]
    end_time = x[1]
    
    #Download Apple stocks from Yahoo API for the given times
    df = web.DataReader(stock_code, 'yahoo', start_time, end_time)
    print(list(df.columns))
    print("THE DATAFRAME")
    print(df.head())
    print(df.info())
    
    #print(df)
    return df



def preProcessData(forecast_out):
    df['Prediction'] = df['Adj Close'].shift(-forecast_out)
    
    #Create independent data set X
    #This dataset will be used for training the model
    #Converts the df to a numpy array
    X = np.array(df.drop(['Prediction'], 1))
    #Remove last n rows 
    X = X[:-forecast_out]
    #print(X)
    
    #Create dependent data set Y
    #This is the target data which will hold price predictions
    #It is a typical convention within ML programming to denote X as the features as y as coreesponding labels
    y = np.array(df['Prediction'])
    #Remove NaN values i.e. last n rows 
    #returns everything except the last n items
    y = y[:-forecast_out]
    
    #Split the data into 85% train and 15% test
    #Model will train by taking input train_x and learning to match to train_y
    #Then the model will attempt to predict an accurate test_y based on train y
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)
    
    return X_train, X_test, y_train, y_test

def linearRegression(dates, stock_code, num_days):
    # df = self.getStockData()
    df = getStockData(dates, stock_code)
    df = df.apply(pd.to_numeric, errors='coerce')
    
    close_px = df['Adj Close']
    #determines how far in the future we will predict values for i.e. n = 30 would be 30 days
    # forecast_out = int(input("How many days in the future would you like predicted?"))
    #Create 'Prediction' datafram colume which stores the predicted price for the stock n days in the future
    #Date remains as index
    df['Prediction'] = df['Adj Close'].shift(-num_days)
    print(df.head())
    #Create independent data set X
    #This dataset will be used for training the model
    #Converts the df to a numpy array
    X = np.array(df.drop(['Prediction'], 1))
    #Remove last n rows 
    X = X[:-num_days]
    #Create dependent data set Y
    #This is the target data which will hold price predictions
    #It is a typical convention within ML programming to denote X as the features as y as coreesponding labels
    y = np.array(df['Prediction'])
    #Remove NaN values i.e. last n rows 
    #returns everything except the last n items
    y = y[:-num_days]
    
    
    #Split the data into 85% train and 15% test
    #Model will train by taking input train_x and learning to match to train_y
    #Then the model will attempt to predict an accurate test_y based on train y
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)
    
    lr = LinearRegression()
    
    #train model
    print("X_train:")
    print(X_train)
    print(y_train)
    print("Y_train: ")
    lr.fit(X_train, y_train)
    
    #crossValScore = cross_validate(estimator=svr, X=X_train, y=y_test,cv=10)
    #Calculated co-efficient of determinanation i.e. r squared
    #Score function compares predictions for X_test with y_test and return r squared value
    confidenceScore = lr.score(X_test, y_test)
    print("R squared score for this model is: ", confidenceScore)
    
    y_predict = lr.predict(X_test)
    #Calculate model Root Mean Squared Error (RMSE)
    #RMSE answers the question: how similar are the numbers in list 1 to list 2 on average
    #In this case we want to get the similarity between the values predicted by the model on test data y_test and the actual data
    print("RMSE is ", np.sqrt(metrics.mean_squared_error(y_test, y_predict)))

    
    #Gets last forecast_out numbers in array
    x_forecast = np.array(df.drop(['Prediction'], 1))[-num_days:]
    lr_prediction = lr.predict(x_forecast)
    for counter, value in enumerate(lr_prediction):
        print("Day: ", counter)
        print("Expected stock price: ", value)
    
    
    x_label = "Linear Regression Prediction"
    draw_graph(dates, df, lr_prediction, x_label)
    #lr_prediction.plot(label="Predicted stock prices")
    #plt.legend()




def draw_graph(dates, df, x, x_label, y=None, y_label=None):
    
    print("In the graph function")
    window = tkinter.Tk()
    window.wm_title("Resulting Graph")

    start_date = dates[0].strftime("%Y-%m-%d")
    end_date = dates[1].strftime("%Y-%m-%d")
    

    fig = Figure(figsize=(8, 8), dpi=100)
    # fig.add_subplot(111).plot(df, x, label=x_label)
    fig2 = fig.add_subplot(111)
    fig2.set_xlabel("From {} to {}, indicating the number of days".format(start_date, end_date))
    fig2.set_ylabel("Numerical Value for Stock")
    fig2.plot(x, label=x_label)
    
    
    
    
    if(type(y) is Series):
        if (y.empty == False) & (y_label != None):
             fig3 = fig.add_subplot(111)
             fig3.set_xlabel("From {} to {}, indicating the number of days".format(start_date, end_date))
             fig3.set_ylabel("Numerical Value for Stock")
             fig3.suptitle("Test Title")
             fig3.plot(y, label=y_label)
             
        
    if(type(y) is None):
        if y_label != None:
            fig3 = fig.add_subplot(111)
            fig3.set_xlabel("From {} to {}, indicating the number of days".format(start_date, end_date))
            fig3.set_ylabel("Numerical Value for Stock")
            fig3.suptitle("Test Title")
            fig3.plot(y, label=y_label)
            
            
    fig.legend()
    
    picture = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    picture.draw()
    picture.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    button1= tkinter.Button(master=window, text="Quit", command= window.destroy)
    button1.pack(side=tkinter.BOTTOM)
    
    

    tkinter.mainloop()
    











    

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:07:29 2022

@author: Majid Majeed


"""
"""
Wealth Accounts of Top Countries
Code Formating:
Used "Black" for PEP-8 Python Style Formating

Table of Contents:
Importing Dataset
Checking Datatypes
Defining Bar Chart Function
Defining Function for Bar Chart
Bar Chart of Countries by Wealth
Defining Pie Chart Function
Defining Function for Pie Chart
Pie Chart of Countries by Wealth
Line plot of countries by Wealth and Years
"""
# Imporitng Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing Dataset
file = pd.read_csv("World_Wealth.csv", index_col=0 )
file

# Checking Datatypes of all columns
file.info()


#Defining Function for Top Countries Graph (Bar Chart)

'''
x = Takes  All value of top columns e:g country names ( India , china , Russia ,UK and USA)
Y = firstly Takes the value of Row 23 and columns 1 value , secondly row 23 and colums 2
 thirdly row 23 columns 3 ,then row 23 columns 4 and lastly row 23 and colums 5
color = Highlight the colour of bars 
x_label = show that what is in X-axis
y_label  = show  that what is in Y-axis
title = Show  that what is main purpose of over plot and what we want to show

'''

def topten_barchart(x, y, color, x_label, y_label, title):
    plt.barh(x, y, color=color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    
# Assigning values for Wealth to variables for the function

y = [file.iloc[23,1],file.iloc[23,2],file.iloc[23,3],file.iloc[23,4],file.iloc[23,5]]
x = file.columns[1:]
color = "maroon"
x_label = "Wealth (Trillion x e^2)"
y_label = "Country"
title = "Top Countries by Wealth"

# Using Function
topten_barchart(x, y, color, x_label, y_label, title)

# Top Countries by Wealth (Pie Chart)

'''
x = firstly Takes the value of Row 23 and columns 1 value , secondly row 23 and colums 2
  thirdly row 23 columns 3 ,then row 23 columns 4 and lastly row 23 and colums 5
y= Takes  All value of top columns e:g country names ( India , china , Russia ,UK and USA)
'''

def piechart(x, y):
    plt.pie(x, labels=y,autopct='%1.1f%%')
    plt.show()

x = [file.iloc[23,1],file.iloc[23,2],file.iloc[23,3],file.iloc[23,4],file.iloc[23,5]]
y = file.columns[1:]

# # Using Function
piechart(x, y)


# Lineplot showing multiple line 

fig ,ax = plt.subplots()
# fig.set_facecolor("black")
ax.plot(file["Year"],file.iloc[:,1:])  # Plotting X (Years) and Y (Countries) 
legend = ax.legend(["UK","US","RUS","CHI","IND"])
title = ax.set_title("World's Wealth 1995 - 2018")
x_label = ax.set_xlabel("Year")
y_label = ax.set_ylabel("Wealth (Trillions)")
ax.yaxis.set_major_formatter(lambda x, pos: f'{x / 1e13:.1f}') # Rounds the numbers in Y-axis into Tens




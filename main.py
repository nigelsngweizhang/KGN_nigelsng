#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <...>
#Group Name: <...>
#Class: <...>
#Date: <...>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pie chart
import matplotlib.pyplot as pit
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)


  #display a specific country (United Kingdom, Germany, France, Italy, Netherlands, Greece, Belgium & Luxembourg, Switzerland, Austria, Scandinavia, CIS & Eastern Europe) in column #20,21,22,23,24,25,26,27,28,29 and 30

  country_label1 = df.columns[20]
  print("\n" + country_label1 + "was selected.")
  country_label2 = df.columns[21]
  print("\n" + country_label2 + "was selected.")
  country_label3 = df.columns[22]
  print("\n" + country_label3 + "was selected.")
  country_label4 = df.columns[23]
  print("\n" + country_label4 + "was selected.")
  country_label5 = df.columns[24]
  print("\n" + country_label5 + "was selected.")
  country_label6 = df.columns[25]
  print("\n" + country_label6 + "was selected.")
  country_label7 = df.columns[26]
  print("\n" + country_label7 + "was selected.")
  country_label8 = df.columns[27]
  print("\n" + country_label8 + "was selected.")
  country_label9 = df.columns[28]
  print("\n" + country_label9 + "was selected.")
  country_label10 = df.columns[29]
  print("\n" + country_label10+ "was selected.")
  country_label11 = df.columns[30]
  print("\n" + country_label11 + "was selected.")

  #reading columns 
  df.columns

  #sorting dataframe (rows and columns)
  print("\nThe following dataframe are read as follows: \n")
  SortedDF = (df[['Year','Month',' United Kingdom ',' Germany ',' France ',' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']][218:348])


#Printing the data

  print(SortedDF)


  # This will convert dtypes from object to int
  SortedDF[' United Kingdom '] = SortedDF[' United Kingdom '].astype(int)
  SortedDF[' Germany '] = SortedDF[' Germany '].astype(int)
  SortedDF[' France '] = SortedDF[' France '].astype(int)
  SortedDF[' Italy '] = SortedDF[' Italy '].astype(int)
  SortedDF[' Netherlands '] = SortedDF[' Netherlands '].astype(int)
  SortedDF[' Greece '] = SortedDF[' Greece '].astype(int)
  SortedDF[' Belgium & Luxembourg '] = SortedDF[' Belgium & Luxembourg '].astype(int)
  SortedDF[' Switzerland '] = SortedDF[' Switzerland '].astype(int)
  SortedDF[' Austria '] = SortedDF[' Austria '].astype(int)
  SortedDF[' Scandinavia '] = SortedDF[' Scandinavia '].astype(int)
  SortedDF[' CIS & Eastern Europe '] = SortedDF[' CIS & Eastern Europe '].astype(int)






  #Removing unwanted Columns
  New = SortedDF.drop(['Year','Month'], axis=1)
  # Add up the total amount of visitors
  total = New.sum()

    #Sorting on descending order
  Sortedvalue = total.sort_values(ascending=False)

  #Sorting toward top 3 countries
  print("The Top 3 countries of visitors to Singapore from the span of 10 years are: ")
  print(Sortedvalue.head(n=3))  


  #pie chart
  activities = ['United Kingdom', 'Germany', 'Scandinavia']
  slices = [4621235, 17555613, 940294]
  colours = ['r', 'g', 'm']

  pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0),
        autopct='%1.2f%%')

  pit.legend(loc="upper left")

  pit.show()

















  return

#########################################################################
#FUNCTION Branch: End of Code
#########################################################################
#Pie chart



  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################
  
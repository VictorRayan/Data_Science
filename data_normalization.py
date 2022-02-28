#pandas library to handle dataframes and numpy to handle maths operations including in arrays
from array import array
from tkinter import ALL
import pandas as pandas
import numpy as numpy

#imports the database into dataframe without headers or column names
csv_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
dataf = pandas.read_csv(csv_path, header=None)

'''
    print("\n", dataf.head(10))
    To visualize data from dataframe, use the variable explorer

'''

#below, creates column names and insert it into dataframe
column_names= ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

dataf.columns = column_names

#it's will to replace the ? (that means missing value) to NaN symbol in secondary dataframe
new_dataf = dataf.replace('?',numpy.NaN)

#it's will drop the every line that contains missing values in specified fields in original dataframe
dataf = new_dataf.dropna(subset=['normalized-losses', 'price'], axis=0)

'''
    you can use it to see the column names:
    print(dataf.columns)
'''
'''
***Everything related with Log view of program status and stage,
   you can put the log methods into variables and see it in variable explorer from
   Spyder IDE, or VsCode executing this code in Interactive View

   But this will delay your processing and execution
'''

#save dataframe as csv file to works locally
dataf.to_csv("automobile.csv", index=False)

#to visualize data types from dataframe:
dataf_dtypes = dataf.dtypes

'''
    to gets the standard deviation, type, count and column mean value,
    use the describe method:
''' 
dataf_describe = dataf.describe()



'''
to show including object type columns, use:
describe(include="all")

and to show from specific columns, use 
dataf[['column1', 'column2', 'column3']].describe(include="all")

'''



#show a summary with some informations from dataframe on the console
dataf_info = dataf.info()


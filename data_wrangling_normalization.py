import pandas as pd
import matplotlib.pylab as plt
import numpy as np

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

dataframe_base = pd.read_csv(filepath, names=headers)
#dataframe_base.head()    #to reads the dataframe


#below, is used the arg 'inplace=True' to prints multiple lines in data visualization
dataframe_base = dataframe_base.replace("?", np.NaN, inplace=True)
missing_data = dataframe_base.isnull()

for column in missing_data.columns.values.tolist():
        
    ''' #you can optionally print 
        print(column)
        print(missing_data[column].value_counts())
        print("")
        
    '''  
    #using variable to visualize in the variable explorer
    missing_data_count = missing_data[column].value_counts()
    
''' to normalize data and trate issues related the missing values in the database, we 
can use many forms to do it:
1 - simply delete the whole row with a missing value
2 - replace the missing value by mean of their row
3 - replace by most frequent value in the row
'''
#first method:
dataframe_ln_drop = dataframe_base
dataframe_ln_drop.dropna(subset=['normalized-losses'], axis=0, inplace=True)
dataframe_base.reset_index(drop=True, inplace=True)
'''first we drop the whole row with missing values, and latter we refresh the index in dataframe
because we had removed a row.'''



#second method:
average_column_normalizedLosses = dataframe_base['normalized-losses'].astype("float").mean(axis=0)
dataframe_nl_mean = dataframe_base
dataframe_nl_mean['normalized-losses'].replace(np.nan, average_column_normalizedLosses, inplace=True)
#its will calculate the mean of normalized-losses column and replace all values that contains NaN putted previoulsy



#last method:
frequent_normalizedLosses = dataframe_base['normalized-losses'].value_counts.idxmax()
dataframe_nl_frequent = dataframe_base
dataframe_nl_frequent['normalized-losses'].replace(np.nan, frequent_normalizedLosses, inplace=True)
'''its will use the idxmax with value_counts to we see the most frequent value in this column and replace it 
in original dataframe'''



#Changing the data type of the columns from dataframe to correct format
#first we see the most appropriate data type for each column from dataframe_base
'''we can do it using print(dataframe_base.dtypes)
or seeing it by variable explorer looking for 'dataframe_dtypes'
'''
dataframe_dtypes = dataframe_base.dtypes

#and now we will to convert to the correct types
dataframe_base[["bore", "stroke"]] = dataframe_base[["bore", "stroke"]].astype("float")
dataframe_base[["normalized-losses"]] = dataframe_base[["normalized-losses"]].astype("int")
dataframe_base[["price"]] = dataframe_base[["price"]].astype("float")
dataframe_base[["peak-rpm"]] = dataframe_base[["peak-rpm"]].astype("float")







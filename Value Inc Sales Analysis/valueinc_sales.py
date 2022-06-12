# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 17:56:05 2022

@author: paulh
"""

import pandas as pd


data = pd.read_csv('transaction.csv', sep=';')

#Summary of the data
data.info()

#CostPerTransaction Column Calculation

#CostPerTRansaction = CostPerItem * NumberofItemsPurchases

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SalesPerTransaction = CostPerItem * NumberOfItemsPurchased
#adding a new column to a DF

data['CostPerTransaction'] = CostPerTransaction

#Sales Per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']


data['Markup'] = (data['ProfitPerTransaction'] ) / data['CostPerTransaction']

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#combining data fields

my_name = 'Peedee'+'Sneedee'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#my_date = data['Day']+'-'

#checking columns data type

#print(data['Day'].dtype)

#Change columns Type
day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #first 5 rows

data.iloc[:,2] #all rows in the 2nd column

data.iloc[4,2] #4th row from 2nd column

#using split to split the client keywords field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand=True)

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#using the lower function to change itm to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()


#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)






















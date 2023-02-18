import numpy as np
import pandas as pd
# data set
# Create random matrix 2x3 with values between 10 and 50
arr_2 = np.random.randint(10, 50, size=(2, 3))

# Create DF with data, row labels & column labels
df_1 = pd.DataFrame(arr_2, ['A', 'B'], ['C', 'D', 'E'])
# Create a DF from multiple series in a dict
# If series are of different lengthes extra spaces are NaN
dict_3 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df_2 = pd.DataFrame(dict_3)

# Grab a column
test = df_1['C']
print(test)
# Get multiple columns
test1 = df_1[['C', 'E', 'D']]
print(test1, "this is test 1")

# Grabb a row as a series
test2 = df_1.loc['A']
print(test2, "this is test 2")
# Grab row by index position
test3 = df_1.iloc[1]
print(test3, "this is test 3")
# Grab cell with Row & Column
df_1.loc['A', 'C']
# Grab multiple cells by defining rows wanted & the
# columns from those rows
print(df_1.loc[['A', 'B'], ['D', 'E']])

# Make new column
df_1['Total'] = df_1['C'] + df_1['D'] + df_1['E']
print(df_1)

# You can perform multiple calculations
df_2['mult'] = df_2['one'] * df_2['two']
df_2

# Make a new row by appending
dict_2 = {'C': 44, 'D': 45, 'E': 46}
new_row = pd.Series(dict_2, name='F')
df_1 = df_1.append(new_row)

# Delete column and set inplace to True which is required
# because Pandas tries to help you not delete data
# by accident
df_1.drop('Total', axis=1, inplace=True)
df_1
# Delete a row
df_1.drop('B', axis=0, inplace=True)
df_1

# Create a new column and make it the index
df_1['Sex'] = ['Men', 'Women']
df_1.set_index('Sex', inplace=True)

# You can reset index values to numbers
#df_1.reset_index(inplace=True)
df_1

# Assign can be used to create a column while leaving the
# original DF untouched
df_2.assign(div=df_2['one'] / df_2['two'])

# You can pass in a function as well
df_2.assign(div=lambda x: (x['one'] / x['two']))

# Combine DataFrames while keeping df_3 data unless
# there is a NaN value
df_3 = pd.DataFrame({'A': [1., np.nan, 3., np.nan]})
df_4 = pd.DataFrame({'A': [8., 9., 2., 4.]})
df_3.combine_first(df_4)
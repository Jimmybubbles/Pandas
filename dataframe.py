import numpy as np
import pandas as pd
from numpy import random


# Create random matrix 2x3 with values between 10 and 50
arr_2 = np.random.randint(10, 50, size=(2, 3))

# Create DF with data, row labels & column labels
df_1 = pd.DataFrame(arr_2, ['A', 'B'], ['C', 'D', 'E'])
print(df_1)
# Create a DF from multiple series in a dict
# If series are of different lengthes extra spaces are NaN
dict_3 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df_2 = pd.DataFrame(dict_3)
print(df_2)

# from_dict accepts a column labels and lists
df_3 = pd.DataFrame.from_dict(dict([('A', [1,2,3]), ('B', [4,5,6])]))
print(df_3)

# You can assign the keys as row labels and column labels separate
# with orient='index'
df_4 = pd.DataFrame.from_dict(dict([('A', [1,2,3]), ('B', [4,5,6])]),
                      orient='index', columns=['one','two','three'])
print(df_4)

# Get number of rows and columns as tuple
print(df_1.shape)
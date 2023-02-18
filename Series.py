import numpy as np
import pandas as pd

# Pandas uses something called a dataframe. It is a 
# 2D data structure that can hold multiple data types.
# Columns have labels.

# Series are built on top of NumPy arrays. 
# Create a series by first creating a list
list_1 = ['a', 'b', 'c', 'd']
# I can define that I want the series indexes to be the
# provided labels
labels = [1, 2, 3, 4]
ser_1 = pd.Series(data=list_1, index=labels)

# You can also add a NumPy array
arr_1 = np.array([1, 2, 3, 4])
ser_2 = pd.Series(arr_1)

# You can quickly add labels and values with a dictionary
dict_1 = {"f_name": "Derek", 
              "l_name": "Banas", 
              "age": 44}
ser_3 = pd.Series(dict_1)

# Get data by label
ser_3["f_name"]

# You can get the datatype
ser_2.dtype

# You can perform math operations on series
ser_2 + ser_2
ser_2 - ser_2
ser_2 * ser_2
ser_2 / ser_2

# You can pass them into NumPy methods
# See NumPy tutorial for more math methods
np.exp(ser_2)

# The difference between Series and ndarray is that operations
# align by labels
# Create a series from a dictionary
ser_4 = pd.Series({4: 5, 5: 6, 6: 7, 7: 8})
# If labels don't align you will get NaN
ser_2 + ser_4

# You can assign names to series
ser_4 = pd.Series({8: 9, 9: 10}, name='rand_nums')
ser_4.name

print(ser_3)
print(ser_2 + ser_2)
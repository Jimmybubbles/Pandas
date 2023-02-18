import numpy as np
import pandas as pd

arr_2 = np.random.randint(10, 50, size=(2, 3))
df_1 = pd.DataFrame(arr_2, ['A', 'B'], ['C', 'D', 'E'])
print(df_1)

# You can use conditional operators to retrieve a table
# based on the condition
print("Greater than 40\n", df_1 > 40.0)

# You can use comparison operater functions as well like
# gt, lt, ge, le, eq, ne
print("Greater than 45\n", df_1.gt(45.0))

# You can place conditions in brackets as well
bool_1 = df_1 >= 45.0
bool_2 = df_1[bool_1]
print(bool_2)

# Get bools for a column
df_1['E'] > 40

# Return a row if cell value in column matches a condition
df_1[df_1['E']>30]

# You can focus on a column based on resulting dataframe
df_2 = df_1[df_1['E']>30]
df_2['C']

# You can stack these commands
print(df_1[df_1['E']>20]['C'])
print()

# You can also grab multiple columns
print(df_1[df_1['E']>20][['C', 'D']])
print()

# You can use multiple conditions
arr_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_2 = pd.DataFrame(arr_3, ['A', 'B', 'C'], ['X', 'Y', 'Z'])
print(df_2, "\n")
# You can use or | to combine conditions as well
df_5 = [(df_2['X']>3) & (df_2['X']<7)]
print(df_5)
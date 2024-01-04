import pandas as pd
# SERIES ONE DIMENTIONAL
# data = [1,2,3,4]
# series = pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(series)
# print(type(series))

# DATAFRAME TWO DIMENTIONAL
# data1 =[1,2,3,4,5]
# df = pd.DataFrame(data1)
# print(df)

# dic = {'fruits':['apple', 'banana', 'orange', 'grapes'], 'count':[10,20,30,40]}
# df = pd.DataFrame(dic)
# print(df)

# data = pd.Series([1,2,3,4],index=['a','b','c','d'])
# df = pd.DataFrame(data)
# print(df)

# data = pd.Series({'Students':['Nabeed', 'talha', 'Awwab'], 'course':['Pl','FIT','DS']})
# df = pd.DataFrame(data)
# print(df)

import numpy as np
# numpyarray = np.array([['Nabeed', 'Talha'], [50000,60000]])
# data = pd.DataFrame({'Names': numpyarray[0], "Salary": numpyarray[1]})
# print(data)

player = ['Nabeed','Abyaz','Awwab']
point = [10,9,8]
title = ['Game1','Game2','Game3']
df1 = pd.DataFrame({'Players':player, 'Points':point, 'Title':title})
# print(df1)

player = ['Karim','Ashan','Ayan']
power = ['punch','kick','elbow']
title = ['Game1','Game2','Game6']
df2 = pd.DataFrame({'Players':player,'Power':power,'Title':title})
# print(df2)

x = df1.merge(df2, on='Title', how='inner')
# y = df1.merge(df2, on='Title', how='outer')
print(x)

player = ['Nabeed','Abyaz','Awwab']
point = [10,9,8]
title = ['Game1','Game2','Game3']
df1 = pd.DataFrame({'Players':player, 'Points':point, 'Title':title})
# print(df1)

player = ['Nabeed','Ashan','Ayan']
power = ['punch','kick','elbow']
title = ['Game1','Game2','Game6']
df2 = pd.DataFrame({'Players':player,'Power':power,'Title':title})
# print(df2)

x = df1.merge(df2, on='Players', how='inner')
x = df1.merge(df2)


# x = df1.merge(df2, on='Players', how='left')
# x = df1.merge(df2, on='Players', how='right')
# x = df1.merge(df2, on='Players', how='outer')
print(x)
# print(y)

# IN merge both dataset must contain atleast one common attribute name
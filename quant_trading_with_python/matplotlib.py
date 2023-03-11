import pandas_datareader.data as pdr

df_apple = pdr.DataReader('AAPL',
                       'quandl',
                       '2011-01-01',
                       '2020-09-30',
                       api_key='yuqp72Y_-GpAsrjQEXfL')

# First five rows
print(df_apple.head())

# Information about the dataframe
print(df_apple.info())

print(df_apple.describe())

import matplotlib.pyplot as plt

fig = plt.figure()
plt = df_apple['AdjClose'].plot()
fig.savefig('close_plot.png')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv("https://raw.githubusercontent.com/dswh/python_fundamentals/master/images/apple_stock_eod_prices.csv",
                parse_dates=True, header=0, index_col=0)

df['simple_return'] = df['Adj_Close'].pct_change()
df['log_return'] = np.log(df['Adj_Close']/df['Adj_Close'].shift(1))
print("Look for Simple and Log return columns")
print(df.head())

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv("https://raw.githubusercontent.com/dswh/python_fundamentals/master/images/apple_stock_eod_prices.csv",
                parse_dates=True, header=0, index_col=0)

# Isolate the adjusted closing prices into a series
adj_close_px = df['Adj_Close']

# Calculate the moving average - let's try it for a short period of # 40 days
moving_avg = adj_close_px.rolling(window=40).mean()

# Inspect the result
print(moving_avg)

# Short moving window rolling mean
df['sma_40'] = adj_close_px.rolling(window=40).mean()

# Long moving window rolling mean - 252 days
df['sma_252'] = adj_close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
fig, ax = plt.subplots( nrows=1, ncols=1 )
df[['Adj_Close', 'sma_40', 'sma_252']].plot(figsize=(12,8),ax=ax)
fig.savefig('moving_avg.png')
# Cumulative moving average
df['cma'] = adj_close_px.expanding().mean()

# Plot the adjusted closing price, the short and long windows of rolling means
fig, ax = plt.subplots( nrows=1, ncols=1 )
df[['Adj_Close', 'cma']].plot(figsize=(12,8),ax=ax)
fig.savefig('cumulative_moving_avg.png')
# Short moving window rolling mean
df['ewma_alpha_0.1'] = adj_close_px.ewm(alpha=0.1, adjust=False).mean()

# Long moving window rolling mean - 252 days
df['ewma_alpha_0.5'] = adj_close_px.ewm(alpha=0.5, adjust=False).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
# Plotting from January 2018 for clearer visualization
fig, ax = plt.subplots( nrows=1, ncols=1 )
df.loc['2018-01-01':,['Adj_Close', 'ewma_alpha_0.1', 'ewma_alpha_0.5']].plot(figsize=(12,8),ax=ax)
fig.savefig('exp_moving_avg.png')

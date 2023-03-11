import pandas as pd
import yfinance as yf

df_apple = yf.download('AAPL',
                       start='2011-01-01',
                       end='2020-09-30',
                       progress=False)

# the head method with default arguments prints the first five rows
print(df_apple.head())
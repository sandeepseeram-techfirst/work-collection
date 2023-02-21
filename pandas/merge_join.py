$ python
Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.


>>> import pandas as pd

>>> df_stock = pd.read_csv("msft_stock_price.csv")

>>> print(df_stock.head())
      Date       Open       High        Low      Close  Adj Close    Volume
0  2/23/15  36.560001  37.000000  35.730000  35.790001  31.962156  42295900
1   3/2/15  35.639999  36.650002  34.959999  35.529999  31.729961  50144100
2   3/9/15  35.529999  37.220001  34.779999  36.349998  32.462257  59722900
3  3/16/15  36.549999  36.970001  35.689999  36.500000  32.596218  51212100
4  3/23/15  36.439999  36.660000  35.000000  35.830002  31.997883  43698600
>>> 

>>> df_trends = pd.read_csv("msft_google_trends.csv")

>>> print(df_trends.head())
      Week  microsoft
0   3/1/15         80
1   3/8/15         80
2  3/15/15         79
3  3/22/15         78
4  3/29/15         76
>>> 

>>> df_stock['Date'] = pd.to_datetime(df_stock['Date'])

>>> df_stock['Year'] = df_stock['Date'].dt.year

>>> df_stock['Week Number'] = df_stock['Date'].dt.week

>>> print(df_stock.head())
        Date       Open       High        Low      Close  Adj Close    Volume  Year  Week Number
0 2015-02-23  36.560001  37.000000  35.730000  35.790001  31.962156  42295900  2015            9
1 2015-03-02  35.639999  36.650002  34.959999  35.529999  31.729961  50144100  2015           10
2 2015-03-09  35.529999  37.220001  34.779999  36.349998  32.462257  59722900  2015           11
3 2015-03-16  36.549999  36.970001  35.689999  36.500000  32.596218  51212100  2015           12
4 2015-03-23  36.439999  36.660000  35.000000  35.830002  31.997883  43698600  2015           13
>>> 
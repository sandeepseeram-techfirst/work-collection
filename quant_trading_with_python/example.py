 
from pandas_datareader import data as pdr
def test_yfinance():
    for symbol in [‘AAPL’, 'MSFT', 'VFINX','BTC-USD']:
        print(">>", symbol, end=' … ')
        data = pdr.get_data_yahoo(symbol,start='2020-09-25', end='2020-10-02')
        print(data)
if __name__ == "__main__":
    test_yfinance() 
 
import yfinance as yf

def get_stock_data(stock_name):

    data = yf.download(stock_name, period="1y")

    return data
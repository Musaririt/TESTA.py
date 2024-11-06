import yfinance as yf
import pandas as pd

# Define the ticker symbol and date range
symbol = 'TSLA'
sdate = '2021-01-01'
edate = '2024-06-30'

# Download the data using yfinance
tsla_data = yf.download(symbol, start=sdate, end=edate, interval='1d')

# Calculate daily percentage change
tsla_data['Daily_Change'] = tsla_data['Adj Close'].pct_change() * 100

# Display the data
pd.options.display.max_rows = None  # To display all rows
print(tsla_data[['Adj Close', 'Daily_Change']])

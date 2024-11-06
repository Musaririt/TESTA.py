import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime

def track_tesla_stock():
  # Define the ticker symbol
  tickerSymbol = 'TSLA'

  # Get data on this ticker
  tickerData = yf.Ticker(tickerSymbol)

  # Get the historical prices for this ticker (last 30 days for demonstration)
  today = datetime.date.today()
  start_date = today - datetime.timedelta(days=30)  
  tickerDf = tickerData.history(period='1d', start=start_date, end=today)

  # Create a plot of the closing price
  plt.figure(figsize=(12, 6))
  plt.plot(tickerDf['Close'], label='Close Price', color='blue')
  plt.title('Tesla Stock Price (Last 30 Days)')
  plt.xlabel('Date')
  plt.ylabel('Price (USD)')
  plt.grid(True)
  plt.legend()
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

# prompt: give a code to follow tesla price stock day by day with graph

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the ticker symbol
tickerSymbol = 'TSLA'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2023-1-1', end='2024-1-1')

# Show the data
print(tickerDf)

# Create a plot of the closing price
plt.figure(figsize=(12, 6))  # Adjust figure size for better readability
plt.plot(tickerDf['Close'], label='Close Price', color='blue')
plt.title('Tesla Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)  # Add a grid for better visualization
plt.legend()
plt.xticks(rotation=45) # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()

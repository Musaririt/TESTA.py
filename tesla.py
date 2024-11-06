symbol = 'TSLA'
sdate = '2021-01-01'
edate = '2024-06-30'

# Download the data using yfinance
tsla_data = yf.download(symbol, start=sdate, end=edate, interval='1d')

# Plot the daily adjusted closing price
plt.figure(figsize=(12, 6))  # Adjust figure size if needed
plt.plot(tsla_data.index, tsla_data['Adj Close'], marker='o', linestyle='-')  # Added markers for data points

# Customize the plot
plt.title('Tesla (TSLA) Daily Stock Price')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price (USD)')
plt.grid(True)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility

# Display the plot
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()

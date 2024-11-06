
symbol = 'TSLA'
sdate = '2021-01-01'
edate = '2024-06-30'

plt.figure(figsize=(12, 6))  # Adjust figure size if needed
plt.plot(tsla_data.index, tsla_data['Adj Close'], marker='o', linestyle='-')  # Added markers for data points

plt.title('Tesla (TSLA) Daily Stock Price')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price (USD)')
plt.grid(True)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility


plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()

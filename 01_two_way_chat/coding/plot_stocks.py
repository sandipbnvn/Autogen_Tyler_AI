# filename: plot_stocks.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch the historical stock data
tickers = ['META', 'TSLA']
data = yf.download(tickers, start='2022-01-01', end='2023-12-31')['Close']

# Plotting the stock prices
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(data[ticker], label=ticker)

plt.title('Stock Prices of META and TESLA (2022-2023)')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.show()
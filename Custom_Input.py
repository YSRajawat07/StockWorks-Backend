import yfinance as yf
import matplotlib.pyplot as plt
# Define the symbol and date range


def function_test(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    print(data)
    return data

# symbol = "SBIN.NS"  # Use "SBIN.BO" for BSE or "SBIN.NS" for NSE
# start_date = "2023-10-01"
# end_date = "2023-10-23"

# Fetch historical data


# data = yf.download(symbol, start=start_date, end=end_date)
# print(data)
# # Plot the closing prices
# plt.figure(figsize=(10, 6))
# plt.plot(data['Close'])
# plt.title(f'{symbol} Stock Price')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')
# plt.grid(True)
# plt.show()
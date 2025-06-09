import yfinance as yf
import pandas as pd

# Choose your stock (example: Reliance Industries NSE)
ticker = yf.Ticker("RELIANCE.NS")

# Fetch historical data
data = ticker.history(period="6mo", interval="1d")

# Save to CSV
data.to_csv("reliance_stock_data.csv")

print("Data saved successfully.")

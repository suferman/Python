# Crypto Screener

A cryptocurrency screener that connects to your exchange account (API), filters market data for USDT-denominated spot-traded coins, and calculates key metrics such as spread percentage and average candle size. The data is exported to a CSV file for further analysis. Check for volatile coins for possible day-trading.

## Table of Contents
1. [Features](#features)
- Fetches market data for USDT, spot-traded pairs from selected exchange (currently using OKX as an example).
- Calculates the bid-ask spread percentage.
- Calculates the average candle length as a percentage of the low price (Volatility).
- Exports the data to a CSV file for further analysis.

2. [Installation](#installation)
- Install required packages:
  pandas, ccxt
- Connect to your API keys (details in [API Keys](#api-keys) section).

3. [Usage](#usage)
-  

4. [Example](#example)
5. [API Keys](#api-keys)
6. [File Output](#file-output)

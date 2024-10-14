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
-  Connect to your API keys.
-  The output will be saved in the specified directory as a CSV file.

4. [Example](#example)
Symbols	Bid	Ask	Spread %	Average Candle Length %
DORA/USDT	0.06623	0.06655	0.48%	14.02%
DEGEN/USDT	0.010043	0.01007	0.27%	12.83%
TURBO/USDT	0.0087297	0.0087368	0.08%	9.98%
SLERF/USDT	0.239	0.2392	0.08%	9.95%
DIA/USDT	0.8168	0.8187	0.23%	9.79%


5. [API Keys](#api-keys)
6. [File Output](#file-output)

import ccxt
import pandas as pd

# Connect to exchange and turn on RateLimit
exchange = ccxt.okx({   # Using okx exchange. (e.g. for binance: "ccxt.binance")
    "apiKey": "Paste your API Key here",   # Get your API Key from your exchange account
    "secret": "Paste your API Secret Key here",   # Get your Secret Key from your exchange account
    "password": "Paste your Pass Phrase here",   # okx requires pass phrase. Delete this line if not required by your selected exchange
    "enableRateLimit": True,
})

def filter_coins(exchange):
    markets = exchange.load_markets()  # Load market data
    filtered = {}  # This is an empty dictionary to store results
    for symbol in markets:  # For every symbol found in markets
        if symbol.endswith('USDT') and markets[symbol]['spot']:  # filter and only return USDT-denominated and spot-traded coins
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d', limit = 11)  # Fetch OHLCV data for all symbol
            bid_ask = exchange.fetch_ticker(symbol)  # Fetch bid/ask data

            candle_lengths = [((candle[1]-candle[2])/candle[2]) * -1 for candle in ohlcv[:-1]]  # Get % movement of candles
            average_candle_length = sum(candle_lengths)/len(candle_lengths) if candle_lengths else 0  # Average the candle movement in % 

            spread_percentage = ((bid_ask['ask'] - bid_ask['bid']) / bid_ask['bid'])  # Calculate spread in %

            filtered[symbol] = {  # Return the following data
                'ohlcv': ohlcv,
                'bid': bid_ask['bid'],
                'ask': bid_ask['ask'],
                'spread': spread_percentage,
                'average_candle_length': average_candle_length
            }
    return filtered

result = filter_coins(exchange)

table_data = []  # Empty list to store data
for symbol, data in result.items():
    table_data.append([symbol, data['bid'], data['ask'], data['spread'], data['average_candle_length']])  # List the data

df = pd.DataFrame(table_data, columns=['Symbols', 'Bid', 'Ask', 'Spread %', 'Average Candle Length %'])  # Name the columns

output_file = r'C:\Users\Desktop\Folder\USDT_Spot.csv'  # Set output location
df.to_csv(output_file, index=False)  # Export data as csv

print(f'Exported Successfully.\nLocation: {output_file}')

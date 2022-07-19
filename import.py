# Import candles from a directory of csv files containing OHLCV data into Jesse

# directory contains csv files with filename {symbol}-1m.csv, e.g. BTC-USD-1m.csv
# csv column order is 'timestamp', 'open', 'high', 'low', 'close', 'volume'
# jesse expects each row to be 1m candlestick

import os
import pandas as pd
import numpy
from jesse import research


DIRECTORY = 'data/FTX/'
EXCHANGE = 'FTX'


def flow_from_df(dataframe: pd.DataFrame, chunk_size: int = 10):
    for start_row in range(0, dataframe.shape[0], chunk_size):
        end_row  = min(start_row + chunk_size, dataframe.shape[0])
        yield dataframe.iloc[start_row:end_row, :]

    
for file in os.listdir(DIRECTORY):
     filename = os.fsdecode(file)
     if filename.endswith(".csv"): 
        symbol = filename.split('-1m.csv').pop(0)
        
        # We need to convert *-PERP to *-USD otherwise backtests will fail later
        symbol = symbol.replace('-PERP', '-USD')
        
        print ("importing " + symbol)
        
        # Read the file into a pandas dataframe 
        df = pd.read_csv(os.path.join(DIRECTORY, filename))
        df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

        # Reorder columns as jesse expects candles to be in format:
        # 'timestamp', 'open', 'close', 'high', 'low', volume'
        df = df[['timestamp', 'open', 'close', 'high', 'low', 'volume']]
        
        # Import them candles in batches
        for chunk in flow_from_df(df, 1000):
            candles = chunk.to_numpy()
            research.store_candles(candles, EXCHANGE, symbol)
                
     else:
         print ("ignoring " + filename)
         continue

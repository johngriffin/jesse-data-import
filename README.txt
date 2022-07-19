# Jesse Data Import

  

This is a simple script that can be used to bulk import OHLCV data to candles in [Jesse](https://github.com/jesse-ai/jesse).

## Prerequisites 
* CSV files that contain 1 minute OHLCV data.  These can be downloaded with CCXT or similar.  
* Filenames should be in the format: 
```{symbol}-1m.csv``` e.g. BTC-USD-1m.csv
* Column order is 'timestamp', 'open', 'high', 'low', 'close', 'volume'

## Usage
* Add csv files to the data directory or update the data directory path in ```import.py```
* Ensure that Jesse is running 
* Run ```python import.py```

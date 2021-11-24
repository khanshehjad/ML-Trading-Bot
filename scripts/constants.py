'''
Constants for the Project
'''

# dates
START_DATE = 1506816000000
END_DATE = 1515888000000
MARCH_1_2018_12AM = 1519862400000
MARCH_30_2018_12AM = 1522368000000


# kline interval
KLINE_INTERVAL_MAR1_MAR30 = '1_mar1_mar30'

# time
MINUTE = 60000

# exchange symbols
ETH_USDT = 'ETHUSDT'

# table names
ONE_MINUTE = 'OneMinute'
THREE_MINUTES = 'ThreeMinutes'
FIVE_MINUTES = 'FiveMinutes'
FEATURES_INT10 = 'features_int10'
FEATURES_INT10_MAR1_MAR30 = 'features_int10_mar1_mar30'

# interval size
INTERVAL10 = 10

# training ratio
TRAINING_RATIO = 0.8


Features = {
    'RSI':'rsi',
    'MFI':'mfi',
    'PROC':'proc',
    'TOTAL_QUOTE_VOLUME':'total_quote_volume',
    'BUY_QUOTE_VOLUME':'buy_quote_volume',
    'BUY_BASE_VOLUME':'buy_base_volume',
    'HIGH':'high',
    'LOW':'low',
    'CLOSE':'close',
    'LSMA':'lsma',
    'SSMA':'ssma',
    'NUM_TRADES':'num_trades'
}

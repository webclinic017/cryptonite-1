from binance import Client
import config
import datetime
import pandas as pd

output_dir = "data"
date_to_go_back_to = datetime.datetime(2020, 1, 1)

#interval = Client.KLINE_INTERVAL_5MINUTE
#symbol = "ETHAUD"
symbols = ["ADAAUD", "ETHAUD", "BTCAUD"]
intervals = [Client.KLINE_INTERVAL_15MINUTE, Client.KLINE_INTERVAL_5MINUTE]


def save_data(symbol, interval, date):
    print(f"getting {interval} {symbol} data")
    date = int(date.strftime("%s"))
    client = Client(config.BINANCE_API_KEY, config.BINANCE_API_SECRET)
    klines = client.get_historical_klines(symbol, interval, date)

    columns = [
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
        'ignore'
    ]

    df = pd.DataFrame(klines, columns=columns)
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    df = df.drop(columns=['close_time','quote_asset_volume', 'number_of_trades','taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume','ignore'])
    df = df.set_index('open_time')

    filename = f"{output_dir}/{symbol}-{interval}.csv"
    print("saving", filename)
    df.to_csv(filename)


if __name__ == "__main__":
    for interval in intervals:
        for symbol in symbols:
            try:
                save_data(symbol, interval, date_to_go_back_to)
            except Exception as e:
                print(e)

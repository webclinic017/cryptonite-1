import backtrader as bt
import datetime
from strategies import BuyAndHold

symbol = "ETHAUD"
interval = "5m"

cerebro = bt.Cerebro()

# create a data feed
data = bt.feeds.GenericCSVData(
    dataname=f'data/{symbol}-{interval}.csv',
    fromdate=datetime.datetime(2022, 1, 1),
    dtformat=('%Y-%m-%d %H:%M:%S'),

    datetime=0,
    high=2,
    low=3,
    open=1,
    close=4,
    volume=5,
)

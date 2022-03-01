import backtrader as bt
import pandas as pd
import datetime
from strategies.buyandhold import BuyAndHold

symbol = "ETHAUD"
interval = "5m"
folder = "../data"
STARTING_CASH = 100000

cerebro = bt.Cerebro()

# create a data feed
filename = f"{folder}/{symbol}-{interval}.csv"
df = pd.read_csv(filename, index_col=0, parse_dates=True)
data = bt.feeds.PandasData(
    dataname=df,
    fromdate=datetime.datetime(2021,7,1)
)


cerebro.adddata(data)

cerebro.run()
cerebro.plot()
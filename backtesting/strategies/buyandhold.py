import backtrader as bt

class BuyAndHold(bt.Strategy):
    # this is a simple strategy that simply buys the asset at the start of the strategy and holds it until the end of the strategy
    def __init__(self, data):
        pass

    def next(self):
        if self.position.size == 0:
            size = int(self.broker.getcash() / self.data)
            self.buy(size=size)


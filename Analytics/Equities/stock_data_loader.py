# A simple yfinance data loader
# https://pypi.org/project/yfinance/

import yfinance as yf
import matplotlib.pyplot as plt

class StockDataLoader:
    def __init__(self, tickers):
        self.tickers = tickers

    def loadData(self):
        return yf.download(tickers = self.tickers, period = '1d', interval = '1m')


if __name__ == '__main__':
    tickers = 'AAPL'
    sdLoader = StockDataLoader(tickers)

    tickersDf = sdLoader.loadData()
    print(tickersDf[-20:])

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    tickersDf['Open'].plot(ax=ax, label='Open', title=tickers, lw=1.0)
    ax.legend(loc='best')
    plt.show()

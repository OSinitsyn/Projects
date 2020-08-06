# A simple yfinance data loader
# https://pypi.org/project/yfinance/

# Plotting data using the mplfinance libray
# https://pypi.org/project/mplfinance/

import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

class StockDataLoader:
    def __init__(self, tickers, period, interval):
        self.tickers = tickers
        self.period = period
        self.interval = interval
        self.tickersDf = None

    def loadData(self):
        self.tickersDf = yf.download(tickers = self.tickers, period = self.period, interval = self.interval, group_by = 'ticker')
        return self.tickersDf

    def tickerData(self, ticker):
        if ticker in self.tickers:
            return self.tickersDf[ticker]

class StockDataPlot:
    def __init__(self):
        pass

    def plotData(self, tickerDf):
        mpf.plot(tickerDf, type = 'candle', style = 'yahoo')
        plt.show()


if __name__ == '__main__':
    tickers = ['AAPL', 'MS']
    sdLoader = StockDataLoader(tickers, '1d', '1m')

    tickersDf = sdLoader.loadData()
    print(tickersDf.shape)
    #tickersDf

    print(tickersDf[-20:])

    tickerDf = sdLoader.tickerData('MS')
    print(tickerDf[-20:])

    sdPlot = StockDataPlot()
    sdPlot.plotData(tickerDf)

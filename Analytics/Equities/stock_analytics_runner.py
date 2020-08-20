import matplotlib.pyplot as plt
import logging
from config import HistDataConfig
from hist_data_loader import HistDataFetcher
from hist_returns import HistReturns
from data_visualizer import TimeSeriesPlot


def main():
    tickers = ['AAPL', 'MS', 'GS']
    #Logger.createLog('Loading data for the following tickers: '+ str(tickers))
    hdFetcher = HistDataFetcher(tickers, **HistDataConfig.getParams())

    tickersDf = hdFetcher.fetchData()
    print(tickersDf.shape)
    #tickersDf

    print(tickersDf[-20:])
    print(tickersDf.memory_usage())

    tickerDf = hdFetcher.tickerData('GS')
    print(tickerDf[-20:])

    #hdFetcher.exportTickerDataToCSV('MS')

    #hdPlot = TimeSeriesPlot()
    #hdPlot.plotData(tickerDf)

    hReturns = HistReturns()
    hReturns.calcReturns(tickerDf)
    print(tickerDf[-20:])

    tickerDf.hist('Return', bins = 25)
    plt.show()

    print(hReturns.calcReturnsSTD(tickerDf))
    print(hReturns.calcReturnsMean(tickerDf))

if __name__ == '__main__':
    main()

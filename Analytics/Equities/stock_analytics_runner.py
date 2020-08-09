from logger import Logger
from stock_data_loader import StockDataLoader
from stock_data_loader import StockDataPlot

def main():
    tickers = ['AAPL', 'MS']
    Logger.createLog('Loading data for the following tickers: '+ str(tickers))
    sdLoader = StockDataLoader(tickers, '1d', '1m')

    tickersDf = sdLoader.loadData()
    print(tickersDf.shape)
    #tickersDf

    print(tickersDf[-20:])

    tickerDf = sdLoader.tickerData('MS')
    print(tickerDf[-20:])

    sdLoader.exportTickerDataToCSV('MS')

    sdPlot = StockDataPlot()
    sdPlot.plotData(tickerDf)


if __name__ == '__main__':
    main()

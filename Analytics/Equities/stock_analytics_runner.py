import logger
from config import HistDataConfig
from stock_data_loader import HistDataFetcher
from data_visualizer import TimeSeriesPlot

lgr = logger.getLogger(__name__)

def main():
    tickers = ['AAPL', 'MS']
    #Logger.createLog('Loading data for the following tickers: '+ str(tickers))
    hdFetcher = HistDataFetcher(tickers, **HistDataConfig.getParams())

    tickersDf = hdFetcher.fetchData()
    print(tickersDf.shape)
    #tickersDf

    print(tickersDf[-20:])

    tickerDf = hdFetcher.tickerData('MS')
    print(tickerDf[-20:])

    hdFetcher.exportTickerDataToCSV('MS')

    hdPlot = TimeSeriesPlot()
    hdPlot.plotData(tickerDf)


if __name__ == '__main__':
    main()

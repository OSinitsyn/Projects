# A simple yfinance data loader
# https://pypi.org/project/yfinance/

import yfinance as yf
import pandas as pd
import logger

lgr = logger.getLogger(__name__)

class HistDataFetcher:
    def __init__(self, tickers = [], **kwargs):
        self.tickers = tickers

        self.period = kwargs.get('period', '1d')
        self.interval = kwargs.get('interval', '1m')
        self.group_by  = kwargs.get('group_by', 'ticker')
        self.auto_adjust = kwargs.get('auto_adjust', False)
        self.prepost = kwargs.get('prepost', False)
        self.threads = kwargs.get('threads', True)

        self.export_data_path = kwargs.get('export_data_path', None)
        self.sep = kwargs.get('sep', ',')
        self.na_rep = kwargs.get('na_rep', '')
        self.header = kwargs.get('header', True)

        self.tickersDf = None

    def fetchData(self):
        lgr.logInfo('Fetching historical data for tickers: {}'.format(self.tickers))
        self.tickersDf = yf.download(tickers = self.tickers,
                                     period = self.period,
                                     interval = self.interval,
                                     group_by = self.group_by,
                                     auto_adjust = self.auto_adjust,
                                     prepost = self.prepost,
                                     threads = self.threads)

        return self.tickersDf


    def tickerData(self, ticker):
        if ticker in self.tickers and self.group_by == 'ticker':
            return self.tickersDf[ticker]

    def exportTickerDataToCSV(self, ticker, filePath = None):
        if ticker in self.tickers and self.group_by == 'ticker':
            tickerDf = self.tickerData(ticker)
            if not filePath:
                fileName = ticker + '_' + tickerDf.index.min().strftime('%Y_%m_%d_%H_%M_%S') + '__' + tickerDf.index.max().strftime('%Y_%m_%d_%H_%M_%S') + '.csv'
                filePath = self.export_data_path + fileName
            tickerDf.to_csv(filePath, sep = self.sep, na_rep = self.na_rep, header = self.header)

    def loadTickerDataFromCSV(self, filePath):
        pass

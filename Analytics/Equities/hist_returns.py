import numpy as np

class HistReturns:
    def __init__(self):
        self.logReturns = True
        self.colName = 'Adj Close' #

    def calcReturns(self, tickerDf):
        if self.logReturns:
            tickerDf['Return'] = np.log(tickerDf[self.colName]/tickerDf[self.colName].shift(1))
        else:
            tickerDf['Return'] = tickerDf[self.colName].pct_change()

        return tickerDf

    def calcReturnsMean(self, tickerDf):
        if 'Return' in tickerDf:
            return tickerDf['Return'].mean()

    def calcReturnsSTD(self, tickerDf):
        if 'Return' in tickerDf:
            return tickerDf['Return'].std()

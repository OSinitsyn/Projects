import numpy as np

class HistReturns:
    def __init__(self):
        self.logReturns = True
        self.colName = 'Adj Close' #

    def Calculate(self, tickerDf):
        if self.logReturns:
            tickerDf['Return'] = np.log(tickerDf[self.colName]/tickerDf[self.colName].shift(1))
        else:
            tickerDf['Return'] = tickerDf[self.colName].pct_change()

        return tickerDf

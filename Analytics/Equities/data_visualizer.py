# Plotting data using the mplfinance libray
# https://pypi.org/project/mplfinance/

import matplotlib.pyplot as plt
import mplfinance as mpf
import logger

class TimeSeriesPlot:
    def __init__(self):
        pass

    def plotData(self, tickerDf):
        mpf.plot(tickerDf, type = 'candle', style = 'yahoo')
        plt.show()

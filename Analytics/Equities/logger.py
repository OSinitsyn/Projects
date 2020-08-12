from datetime import datetime

class Logger:
    def __init__(self):
        self.loggerType = ''

    def logInfo(self, info):
        print('{} {}: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.loggerType, info))

class StockDataLoaderLogger(Logger):
    def __init__(self):
        self.loggerType = 'Stock data loader'

class StockAnalyticsRunnerLogger(Logger):
    def __init__(self):
        self.loggerType = 'Stock analytics runner'

class DataVisualizerLogger(Logger):
    def __init__(self):
        self.loggerType = 'Data visualizer'


def getLogger(loggerType):
    if loggerType == 'stock_data_loader':
        return StockDataLoaderLogger()
    elif loggerType == 'stock_analytics_runner':
        return StockAnalyticsRunnerLogger()
    elif loggerType == 'data_visualizer':
        return DataVisualizerLogger()
    else:
        return Logger()

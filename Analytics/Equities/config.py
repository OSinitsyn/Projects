class HistDataConfig:
    ### Historical data loader ###
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    @staticmethod
    def getParams():
        return {'period' : '1d',
                'interval' : '1m',
                'group_by' : 'ticker',
                'auto_adjust' : False,
                'prepost' : False,
                'threads' : True ,
                'export_data_path' : '/Users/Oleks/Documents/Python/Projects/Analytics/Equities/TempData/',
                'sep' : ',',
                'na_rep' : '',
                'header' : True }


class HistReturnsConfig:
    ### Historical returns ###
    # 
    @staticmethod
    def getParams():
        return {'logReturns' : True,
                'calcColName' : 'Adj Close'}

class LoggerConfig:
    ### Logger config ####
    @staticmethod
    def getParams():
        return {'write_log_files' : True,
                'log_data_path' : '/Users/Oleks/Documents/Python/Projects/Analytics/Equities/LogData/'}

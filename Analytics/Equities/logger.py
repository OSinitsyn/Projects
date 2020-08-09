import datetime as dt
from config import StockDataConfig as sdConfig

class Logger:
    def __init__(self):
        pass

    @staticmethod
    def createLog(message):
        print(__name__)
        print(dt.datetime.now(), ' : ', message)

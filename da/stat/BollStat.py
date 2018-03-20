import numpy as np
import da.odbc.MysqlConnect as mysqlDB
if __name__=="__main__":
    sql="SELECT symbol,open,close,high,low,vol,count FROM kline_1_min LIMIT 1000"
    kline1MinResult=mysqlDB.getMysqlData(sql);
    t = np.dtype([('symbol', str, 40), ('open', float), ('close', float), ('high', float), ('low', float), ('vol', float), ('count', int)])
    klineItem = np.array(kline1MinResult,dtype=t)
    print(klineItem["symbol"])
    pass
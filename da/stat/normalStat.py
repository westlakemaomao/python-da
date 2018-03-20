import numpy as np
import da.odbc.MysqlConnect as mysqlDB


def vwapStat(klineItem):
    """"volume-weighted average price"""
    vwap = np.average(klineItem["close"], weights=klineItem["vol"])
    return vwap


def rateOfReturn(klineItem):
    returns = np.diff(klineItem["close"]) / klineItem["close"][:-1]
    return returns


def rateOfLogReturn(klineItem):
    return np.diff(np.log(klineItem["close"]))


def volatilityRate(klineItem, recyle=1):
    """recyle个周期的波动率"""
    logReturns = rateOfLogReturn(klineItem)
    volatility = np.std(logReturns) / np.mean(logReturns)
    return volatility / np.sqrt(1. / recyle)


def artValue(klineItem, recyle=1):
    """Average TRUE range 真实波动幅度均值"""
    h = klineItem["high"][-recyle:]
    l = klineItem["low"][-recyle:]
    previousclose = klineItem["close"][-recyle - 1:-1]
    truerange = np.maximum(h - l, h - previousclose, previousclose - l)
    atr = np.zeros(recyle)
    atr[0] = np.mean(truerange)
    for i in range(1, recyle):
        atr[i] = (recyle - 1) * atr[i - 1] + truerange[i]
        atr[i] /= recyle
    return atr


def sma(klineItem, recyle=1):
    """simple moving average"""
    weights = np.ones(recyle) / recyle
    close = klineItem["close"]
    return np.convolve(weights, close)[recyle - 1:-recyle + 1]


def ema(klineItem, recyle=1):
    """exponential moving average"""
    weights = np.exp(np.linspace(-1., 0., recyle))
    weights /= weights.sum()
    c = klineItem["close"]
    emaValue = np.convolve(weights, c)[recyle - 1:-recyle + 1]
    return emaValue


def bollingerBand(klineItem, recyle=1):
    """"bolling band"""
    weights = np.ones(recyle) / recyle
    c = klineItem["close"]
    sma = np.convolve(weights, c)[recyle - 1:-recyle + 1]
    deviation = []
    C = len(klineItem)
    for i in range(recyle - 1, C):
        if i + recyle < C:
            dev = c[i:i + recyle]
        else:
            dev = c[-recyle:]
        averages = np.zeros(recyle)
        averages.fill(sma[i - recyle - 1])
        dev = dev - averages
        dev = dev ** 2
        dev = np.sqrt(np.mean(dev))
        deviation.append(dev)
    deviation = 2 * np.array(deviation)
    upperBB = sma + deviation
    lowerBB = sma - deviation
    return (lowerBB, sma, upperBB)


if __name__ == "__main__":
    sql = "SELECT symbol,open,close,high,low,vol,count FROM kline_1_min LIMIT 10"
    kline1MinResult = mysqlDB.getMysqlData(sql);
    t = np.dtype(
        [('symbol', str, 40), ('open', float), ('close', float), ('high', float), ('low', float), ('vol', float),
         ('count', int)])
    klineItem = np.array(kline1MinResult, dtype=t)
    # vwap=np.average(klineItem["close"],weights=klineItem["vol"])
    vwap = vwapStat(klineItem);
    print(vwap)
    returns = rateOfReturn(klineItem);
    print(returns)
    logReturns = rateOfLogReturn(klineItem);
    print(logReturns)
    # 7分钟波动率
    vol = volatilityRate(klineItem, 7)
    print(vol)
    # 真实波动率
    art = artValue(klineItem, 5)
    print(art)
    ma = sma(klineItem, 3)
    print(ma)
    emaValue = ema(klineItem, 3)
    print(emaValue)
    boll = bollingerBand(klineItem, 5)
    print(boll)

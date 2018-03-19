#
import numpy as np

if __name__ == "__main__":
    print("name")
    print(np.arange(20))
    range = np.arange(20)
    reshape = range.reshape(4, 5)
    print(reshape)
    print(np.arange(20).reshape(4, 5))
    t = np.dtype([('symbol', str, 40), ('open', float), ('close', float)])
    itemz = np.array([('btcusdt', 43.2, 3.14), ('htusdt', 2.3, 2.5)],dtype=t)
    print(t)
    print(itemz[1]["symbol"])
    print(itemz[0])
    print(range[::5])
    print(itemz["open"])
    print(itemz.ravel())#
    a=np.arange(20).reshape(4,5)
    b=np.hsplit(a,5)
    print(np.array(np.arange(5)).tolist())
    np.loadtxt()
    # print(b)

class Facade:
    def operations(self, rate):
        mxn = mxn_rate(rate)
        usd = usd_rate(rate)

        return mxn, usd
    
    
def mxn_rate(rate):
    return rate['rates']['MXN']
    
def usd_rate(rate):
    return rate['rates']['USD']
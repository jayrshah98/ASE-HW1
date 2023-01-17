import math

class SYM:
    def __init__(i) -> None:
        i.n   = 0
        i.has = {}
        i.most = 0
        i.mode = None 
        pass

    def add(i,x):
        if x:
            i.n = i.n + 1 
            i.has[x] = 1 + (i.has[x] if i.has[x] else 0)
            if i.has[x] > i.most:
                i.most = i.has[x]
                i.mode = x
        return x

    def mid(i):
        return i.mode
    
    def div(i, fun, e):
        def fun(p):
            return p * math.log(p,2)
        e = 0
        for j in j.has.keys():
            e = e + fun(i.has[j]/i.n)
        return -e


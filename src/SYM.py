import math
import collections

class SYM:
    def __init__(i) -> None:
        i.n   = 0
        i.has = collections.defaultdict(int)
        i.most = 0
        i.mode = None 
        pass

    def add(i,x):
        if x:
            i.n = i.n + 1 
            i.has[x] = i.has[x] + 1
            if i.has[x] > i.most:
                i.most = i.has[x]
                i.mode = x
        return x

    def mid(i):
        return i.mode
    
    def div(i):
        def fun(p):
            return p * math.log(p,2)
        e = 0

        for j in list(i.has.keys()):
            e = e + fun(i.has[j]/i.n)
        return -e

# obj = SYM()
# mid_res = obj.mid()
# div_res = obj.div()
# add_res = obj.add(9)
# print(mid_res, div_res, add_res)

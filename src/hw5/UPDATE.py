from COLS import COLS
from LIB import LIB
import random
import config

lib = LIB()

rand = lib.rand
rint = lib.rint

class UPDATE:

    def __init__(self) -> None:
        pass
    
    def add(self,col,x,n=1):
    
        if x != '?':
            col.n += n
            if hasattr(col, "isSym") and col.isSym:
                col.has[x] = n + (col.has.get(x, 0))
                if col.has[x] > col.most:
                    col.most = col.has[x]
                    col.mode = x
            else:
                x = float(x)
                col.lo = min(x,col.lo)
                col.hi = max(x,col.hi)
                all = len(col.has)
                if all < config.the["Max"]:
                    pos = all + 1
                elif random.random() < config.the["Max"] / col.n:
                    pos = rint(1,11)
                else:
                    pos = None
                if pos:
                    if isinstance(col.has,dict):
                        col.has[pos] = x
                    else:
                        col.has.append(x)
                    col.ok = False

    def adds(self, col, t):
        for value in t or []:
            self.add(col, value)
        return col            


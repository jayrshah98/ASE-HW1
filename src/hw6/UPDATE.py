import debugpy
from COLS import COLS
from LIB import LIB
import random
import config
lib = LIB()

rand = lib.rand
rint = lib.rint


def __init__(self) -> None:
        pass


def add(col, x, n = None):
    def sym(t):
        t[x] = n + (t.get(x, 0))
        if t[x] > col.most:
            col.most, col.mode = t[x], x

    def num(t):
        col.lo, col.hi = min(x, col.lo), max(x, col.hi)
        if len(t) < config.the["Max"]:
            col.ok = False
            t.append(x)
        elif lib.rand() < config.the["Max"] / col.n:
            col.ok = False
            t[lib.rint(0, len(t) - 1)] = x      
    if x != "?":
        n = n or 1
        col.n += n
        if hasattr(col, "isSym") and col.isSym:
            sym(col.has)
        else:
            x = float(x)
            num(col.has)  
    # def add(self,col,x,n=1):
    
    #     if x != '?':
    #         col.n += n
    #         if hasattr(col, "isSym") and col.isSym:
    #             col.has[x] = n + (col.has.get(x, 0))
    #             if col.has[x] > col.most:
    #                 col.most = col.has[x]
    #                 col.mode = x
    #         else:
    #             x = float(x)
    #             col.lo = min(x,col.lo)
    #             col.hi = max(x,col.hi)
    #             all = len(col.has)
    #             if all < config.the["Max"]:
    #                 pos = all + 1
    #             elif random.random() < config.the["Max"] / col.n:
    #                 pos = rint(1,11)
    #             else:
    #                 pos = None
    #             if pos:
    #                 if isinstance(col.has,dict):
    #                     col.has[pos] = x
    #                 else:
    #                     col.has.append(x)
    #                 col.ok = False

def adds(col, t):
    for value in t or []:
        add(col, value)
    return col            


def row(data, t):
    if data.cols:
        data.rows.append(t)
        for cols in [data.cols.x, data.cols.y]:
            for col in (cols): 
                add(col.col, t[col.col.at]) 
    else: 
        data.cols = COLS(t)  
    return data

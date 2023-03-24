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

def extend(range, n, s):
    range.lo = min(n, range.lo)
    range.hi = max(n, range.hi)
    add(range.y, s)
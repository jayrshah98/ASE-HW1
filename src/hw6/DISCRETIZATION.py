from copy import deepcopy
import math
from COL import COL
import UPDATE as update
from RANGE import *
from LIB import LIB
import UPDATE as update
import config
lib = LIB()


def bins(cols, Rows):
    res = []
    for col in cols:
        ranges = {}
        for y, rows in Rows.items():
            for row in rows:
                if (isinstance(col, COL)):
                    col = col.col
                x = row[col.at]
                if x != "?":
                    k = int(bin(col, float(x) if x != "?" else x))
                    ranges[k] = ranges[k] if k in ranges else RANGE(col.at, col.txt, float(x) if x != "?" else x)
                    update.extend(ranges[k], float(x), y)
        ranges = {key: value for key, value in sorted(ranges.items(), key=lambda x: x[1].lo)}
        newRanges = {}
        i = 0
        for key in ranges:
            newRanges[i] = ranges[key]
            i += 1
        newRangesList = []
        if hasattr(col, "isSym") and col.isSym:
            for item in newRanges.values():
                newRangesList.append(item)
        res.append(newRangesList if hasattr(col, "isSym") and col.isSym else merges(newRanges))
    return res

def bin(col, x):

    if x=="?" or hasattr(col, "isSym"):
        return x
    tmp = (col.hi - col.lo)/(config.the["bins"] - 1)
    return 1 if col.hi == col.lo else math.floor(x / tmp + 0.5) * tmp


def merges(ranges0):
    def noGaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j-1].hi
        t[0].lo = -float("inf")
        t[-1].hi = float("inf")
        return t
    ranges1, j = [], 0
    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j+1] if j + 1 < len(ranges0) else None
        if right:
            y = merged(left.y, right.y)
            if y:
               j = j+1
               left.hi, left.y = right.hi, y
        ranges1.append(left)
        j += 1
    return noGaps(ranges0) if len(ranges1)==len(ranges0) else merges(ranges1)


def merged(col1, col2):
    new = merge(col1, col2)
    if lib.div(new) <= (lib.div(col1)*col1.n + lib.div(col2)*col2.n)/new.n:
        return new
    

def merge(col1, col2):
    new = deepcopy(col1)
    if hasattr(col1, "isSym") and col1.isSym:
        for x, n in col2.has.items():
            update.add(new, x, n)
    else:
        for n in col2.has:
            update.add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new
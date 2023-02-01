from main import main
from lib import LIB
from ROW import ROW
from COLS import COLS

lib = LIB()
csv = lib.csv
rnd = lib.rnd
kap = lib.kap

class DATA:
    
    def __init__(self, src = main.the["file"]):
        self.rows = []
        self.cols = None
        if type(src) == str:
            csv(src, self.add)

        elif src:
            for x in src:
                self.add(x)

    def add(self, t):
        if self.cols:
            t = t if hasattr(t, 'cells') else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)

    def clone(self, passed_fields):
        data = DATA(self.cols.names)
        for row in passed_fields:
            self.add(row)
        return data

    def stats(self, nPlaces, what = "mid", cols = None):
        def fun(k, col):
            return rnd(getattr(col, what or 'mid')(), nPlaces), col.txt
        return kap(cols or self.cols.y, fun)


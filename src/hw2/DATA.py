#from main import main
from lib import LIB
from ROW import ROW
from COLS import COLS
import config

lib = LIB()
csv = lib.csv
rnd = lib.rnd
kap = lib.kap

class DATA:
    
    def __init__(self, src):
        self.rows = []
        self.cols = None
        if type(src) == str:
            lib.csv(src, self.add)

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

    def clone(self,init, passed_fields):
        data = DATA(self.cols.names)
        map(init or {}, data.add(passed_fields))
        return data

    def stats(self, nPlaces, what, cols = None):
        # print(self.rows)
        # print("Yesha")
        def fun(k, col):
            mid = getattr(col,what or "mid")
            rounded = round(float(mid()),nPlaces)
            return (rounded,col.txt)
        return kap(cols or self.cols.y,fun)


from LIB import LIB
from COLS import COLS
from ROW import ROW
import config
from NUM import NUM
num = NUM()
row = ROW
lib = LIB()
csv = lib.csv
class DATA:
    def __init__(self, src = None, cols=None, rows=None):
        self.rows = []
        self.cols = cols
        if type(src) == str:
            csv(src, self.add)

        elif src:
            for x in src:
                self.add(x)

    def new(self):
        return {"rows": [], "cols": None}


    def add(self,row):
        for t in COLS.x, COLS.y:
            for col in t:
                col.add(row.cells[col.at])

    def clone(self,data, ts):
        data1 = DATA(None,data.cols,None)
        def fun(t):
            self.row(data1, t)
        for row in ts: 
            fun(row)
        return data1
    
    def read(self,sfile,data = None):
        data = DATA()
        def fun(t):
            self.row(data, t)
        lib.csv(sfile, fun)
        return data

    def row(self, data, t):
        if data.cols:
            data.rows.append(t)
            for cols in [data.cols.x, data.cols.y]:
                for col in (cols): 
                    lib.add(col.col, t[col.col.at]) 
        else: 
            data.cols = COLS(t)  
        return data

    def dist(self, data, t1, t2, cols = None):
    
        def dist1(col, x, y):
            if x == "?" and y == "?":
                return 1
            if hasattr(col, "isSym"):
                return 0 if x == y else 1
            else:
                x, y = num.norm(col,x), num.norm(col,y)
                if x == "?":
                    x = 1 if y < 0.5 else 1
                if y == "?":
                    y = 1 if x < 0.5 else 1

                    
                return abs(x - y)

        d, n = 0, 1 / float("inf")
        cols = cols or data.cols.x
        for col in cols:
            n += 1
            d += dist1(col.col, t1[col.col.at], t2[col.col.at]) ** config.the['p']
            
        return (d / n)**(1 / config.the['p'])
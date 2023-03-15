from LIB import LIB
from COLS import COLS
from ROW import ROW
lib = LIB()
csv = lib.csv
class DATA:
    def __init__(self, src = None, cols=None, rows=None):
        self.rows = []
        self.cols = None
        if type(src) == str:
            csv(src, self.add)

        elif src:
            for x in src:
                self.add(x)

    # def add(self, t):
    #     if self.cols:
    #         t = t if hasattr(t, 'cells') else ROW(t)
    #         self.rows.append(t)
    #         self.cols.add(t)
    #     else:
    #         self.cols = COLS(t)

    def clone(self, rows = None):
        data = DATA([self.cols.names])
        for row in rows:
            data.add(row)
        return data
    
    def read(self,sfile,data = None):
        data = DATA()
        lib.csv(sfile, lambda t: lib.row(data,t))

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

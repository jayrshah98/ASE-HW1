from LIB import LIB
from COLS import COLS
from ROW import ROW
from UPDATE import UPDATE
import config
from NUM import NUM
update = UPDATE()
num = NUM()
row = ROW
lib = LIB()
class DATA:
    def __init__(self, src = None, cols=None, rows=None):
        rows = {}
        cols = []
        add = lambda x: update.row(self,x)
        self.rows = []
        self.cols = cols
        if type(src) == str:
            lib.csv(src, add)

        elif src:
            self.cols = COLS(src.cols.names)
            if rows:
                for row in rows:
                    add(row)
        

    def new(self):
        return {"rows": [], "cols": None}


    # def add(self,row):
    #     for t in COLS.x, COLS.y:
    #         for col in t:
    #             col.add(row.cells[col.at])

    def clone(self,data, ts):
        data1 = DATA(None,data.cols,ts)
        def fun(t):
            update.row(data1, t)
        for row in ts: 
            fun(row)
        return data1
    
    def read(self,sfile,data = None):
        data = DATA()
        callback = lambda t: update.row(data, t)
        lib.csv(sfile, callback)
        return data

    # def row(self, data, t):
    #     if data.cols:
    #         data.rows.append(t)
    #         for cols in [data.cols.x, data.cols.y]:
    #             for col in (cols): 
    #                 update.add(col.col, t[col.col.at]) 
    #     else: 
    #         data.cols = COLS(t)  
    #     return data

    def dist(self, data, t1, t2, cols = None):
    
        def dist1(col, x, y):
            if x == "?" and y == "?":
                return 1
            if hasattr(col, "isSym"):
                return 0 if x == y else 1
            else:                
                if x == "?":
                    y = float(y)
                    x = 1 if y < 0.5 else 1
                elif y == "?":
                    x = float(x)
                    y = 1 if x < 0.5 else 1 
                # print("col:",col)
                # print("x",float(x))
                else:
                    x = float(x)
                    y = float(y)
                    x, y = num.norm(col,x), num.norm(col,y)
                return abs(x - y)

        d, n = 0, 1 / float("inf")
        cols = cols or data.cols.x
        for col in cols:
            n += 1
            d += dist1(col.col, t1[col.col.at], t2[col.col.at]) ** config.the['p']
            
        return (d / n)**(1 / config.the['p'])
    


    def around(self,row1,rows=None,cols=None):

        if rows == None:
            rows = self.rows

        if cols == None:
            cols = self.cols.x

        def fun(row2):
            return {'row': row2, 'dist':self.dist(row1,row2,cols)}

        return sorted(list(map(fun, rows)), key=lambda x: x['dist'])


    def half(self, data, rows=None, cols=None, above=None):
        left, right = [], []

        def gap(r1, r2):
            return self.dist(data, r1, r2, cols)

        def cos(a, b, c):
            return (a ** 2 + c ** 2 - b ** 2) / (2 * c)

        def proj(r):
            return {'row': r, 'x': cos(gap(r, A), gap(r, B), c)}

        rows = rows or self.rows
        some = lib.many(rows, config.the["Halves"])
        A = above if config.the["Reuse"] else any(some)
        def fun(r):
            return [{'row': r, "d":gap(r, A)}]
        tmp  = sorted( map(fun, some), key=lambda x: x["d"])
        far = tmp[(len(tmp)) * config.the["Far"]]
        B, c = far["row"], far["d"]

        for n, two in enumerate(sorted(map(proj, rows), key=lambda x: x["x"])):
            if n + 1 <= (len(rows) / 2):
                left.append(two["row"])
            else:
                right.append(two["row"])

        return left, right, A, B, 
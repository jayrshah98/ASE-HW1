from UPDATE import UPDATE
from LIB import LIB
from NUM import NUM
from SYM import SYM

import math
from UPDATE import UPDATE
import config

num = NUM()
update = UPDATE()
lib = LIB()
kap = lib.kap
cosine = lib.cosine
class DATA:

    def __init__(self):
        self.rows = []
        self.cols = None

    def read(sfile,data):
        data = DATA()
        lib.csv(sfile, lambda t: lib.row(data,t))

        def fun(t):
            update.row(data, t)
        lib.csv(sFile, fun)
        return data

    def clone(self, data, ts = None):

        d = DATA()
        data1 = update.row(d, data.cols.names)
        for _, t in enumerate(ts or []):
            update.row(data1, t)
        return data1
    
    def dist(self, data, t1, t2, cols = None):
    
        def dist1(col, x, y):
            if x == "?" and y == "?":
                return 1
            if hasattr(col, "isSym"):
                return 0 if x == y else 1
            else:
                x, y = num.norm( x), num.norm( y)
                if x == "?":
                    x = 1 if y < 0.5 else 1
                if y == "?":
                    y = 1 if x < 0.5 else 1
                return abs(x - y)

        d, n = 0, 1 / float("inf")
        cols = cols or data.cols.x
        for col in cols:
            n += 1
            d += dist1(col, t1[col.col.at], t2[col.col.at]) ** config.the['p']
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

        return left, right, A, B, c

    def cluster(self, rows=None,cols=None, above=None):

        if rows == None:
            rows = self.rows

        if cols == None:
            cols = self.cols.x

        node = {'data': self.clone(rows)} 

        if len(rows) >= 2:
            left, right, node["A"], node["B"], node["mid"], node["C"] = self.half(rows,cols,above)
            node["left"]  = self.cluster(left,cols, node["A"])
            node["right"] = self.cluster(right,cols, node["B"])
        return node 


    def better(self,row1,row2,s1,s2,ys,x,y):
        s1,s2,ys,x,y = 0,0,self.cols.y

        for _,col in enumerate(ys):
            x  = col.norm( row1.cells[col.at] )
            y  = col.norm( row2.cells[col.at] )
            s1 = s1 - math.exp(col.w * (x-y) / len(ys))
            s2 = s2 - math.exp(col.w * (y-x) / len(ys))
        return s1/len(ys) < s2/len(ys)

    def tree(self, rows=None, cols=None, above=None, here = None):
        rows = rows if rows else self.rows
        here = {"data": self.clone(self, rows)}

        if (len(rows)) >= 2 * ((len(self.rows)) ** config.the['min']):
            left, right, A, B = self.half(rows, cols, above)
            here["left"] = self.tree(left, cols, A)
            here["right"] = self.tree(right, cols, B)
        return here
    
  
from UPDATE import UPDATE
from LIB import LIB
from NUM import NUM
from SYM import SYM

import math
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

    def read(self, sFile):
        data = DATA()
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
                if x == "?":
                    y = float(y)
                    x = 1 if y < 0.5 else 1
                elif y == "?":
                    x = float(x)
                    y = 1 if x < 0.5 else 1 
                
                else:
                    x = float(x)
                    y = float(y)
                    x, y = num.norm(col,x), num.norm(col,y)
                return abs(x - y)

        d, n = 0, 1 / float("inf")
        cols = cols if cols else data.cols.x

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
        A = above if above else lib.any(some)
        tmp = sorted([{"row": r, "d": gap(r, A)} for r in some], key=lambda x: x["d"])
        far = tmp[int((len(tmp)) * config.the["Far"])]
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
    

    # def better(self, data, row1, row2):

    #     s1, s2, ys = 0, 0, data.cols.y
    #     print("ys", ys)
    #     for col in ys:
    #         n1 =  float(row1[col.col.at]) if row1[col.col.at] != "?" else row1[col.col.at]
    #         n2 = float(row2[col.col.at]) if row2[col.col.at] != "?" else row2[col.col.at]
    #         x = lib.norm(NUM,col.col, n1)
    #         y = lib.norm(NUM,col.col, n2)

    #         s1 -= math.exp(col.col.w * (x-y)/len(ys))
    #         s2 -= math.exp(col.col.w * (y - x)/len(ys))

    #     return s1/len(ys) < s2 / len(ys)


    def tree(self, data, rows = None, cols = None, above = None):
        rows = rows if rows else data.rows
        here = {"data" : data.clone(data, rows)}
        if len(rows) >= 2 * (len(data.rows) ** config.the['min']):
            left, right, A, B, _ = self.half(data, rows, cols, above)
            here["left"] = self.tree(data, left, cols, A)
            here["right"] = self.tree(data, right, cols, B)
        return here

    def showTree(self, tree, lvl=0):
        if tree:
            print("{}[{}] ".format(("|.. ") * lvl, len(tree['data'].rows)), end="")
            if lvl == 0 or not "left" in tree:
                print(lib.stats(tree["data"]))
            else:
                print("")
            self.showTree(tree["left"] if "left" in tree else None, lvl + 1)
            self.showTree(tree["right"] if "right" in tree else None, lvl + 1)

 
    def better(self,data, row1, row2, s1=0, s2=0, ys=None, x=0, y=0):

        s1, s2, ys = 0, 0, data.cols.y
        for col in ys:
            n1 =  float(row1[col.col.at]) if row1[col.col.at] != "?" else row1[col.col.at]
            n2 = float(row2[col.col.at]) if row2[col.col.at] != "?" else row2[col.col.at]
            x = NUM.norm(NUM,col.col, n1)
            y = NUM.norm(NUM,col.col, n2)

            s1 -= math.exp(col.col.w * (x-y)/len(ys))
            s2 -= math.exp(col.col.w * (y - x)/len(ys))

        return s1/len(ys) < s2 / len(ys)

    def sway(self, data, cols = None):

        def worker(rows, worse, above=None):
            if len(rows) <= len(data.rows) ** config.the["min"]:
                return rows, lib.many(worse, config.the['rest'] * len(rows))
            else:
                l, r, A, B, _ = self.half(data, rows, cols, above)

                if self.better(data, B, A):
                    l, r, A, B = r, l, B, A

                for x in r:
                    worse.append(x)
                return worker(l, worse, A)

        best, rest = worker(data.rows, [])

        return self.clone(data, best), self.clone(data, rest)

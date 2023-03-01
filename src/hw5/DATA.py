from UPDATE import UPDATE
from LIB import LIB
import math
from UPDATE import UPDATE
import config

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
    
    def stats(self, nPlaces, what, cols = None):
        def fun(k, col):
            mid = getattr(col,what or "mid")
            rounded = round(float(mid()),nPlaces)
            return (rounded,col.txt)
        return kap(cols or self.cols.y,fun)

    def dist(self,row1,row2,cols=None):
        n,d = 0,0
        if cols == None:
            cols = self.cols.x
        for _,col in enumerate(cols):
            n = n + 1
           
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**config.the['p']
            
        return (d/n)**(1/config.the['p'])

    def around(self,row1,rows=None,cols=None):

        if rows == None:
            rows = self.rows

        if cols == None:
            cols = self.cols.x

        def fun(row2):
            return {'row': row2, 'dist':self.dist(row1,row2,cols)}

        return sorted(list(map(fun, rows)), key=lambda x: x['dist'])


    def half(self,rows=None,cols=None,above=None):

        def project(row):
            x, y = cosine(dist(row,A), dist(row,B), c)
            row.x = row.x or x
            row.y = row.y or y
            return {"row": row, "x": x, "y": y}

        def dist(row1,row2):
            return self.dist(row1,row2,cols)

        if rows == None:
            rows = self.rows
        A  = above or any(rows)
        B = self.furthest(A, rows)['row']
        c  = dist(A,B)

        left, right = [], []

        res = [project(row) for row in rows]
        sorted_res = sorted(res, key=lambda x: x["x"])
        for n,tmp in enumerate(sorted_res):
            if (n+1) <= len(rows) // 2: 
                left.append(tmp["row"])
                mid = tmp["row"]
            else: 
                right.append(tmp["row"])
        return left, right, A, B, mid, c

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

    def furthest(self, row1=None, rows=None, cols=None):
        t = self.around(row1,rows,cols)
        return t[len(t) - 1]


    def better(self,row1,row2,s1,s2,ys,x,y):
        s1,s2,ys,x,y = 0,0,self.cols.y

        for _,col in enumerate(ys):
            x  = col.norm( row1.cells[col.at] )
            y  = col.norm( row2.cells[col.at] )
            s1 = s1 - math.exp(col.w * (x-y) / len(ys))
            s2 = s2 - math.exp(col.w * (y-x) / len(ys))
        return s1/len(ys) < s2/len(ys)

    def sway(self,rows=None,min=None,cols=None,above=None):

        rows = rows if rows else self.rows

        min  = min or len(rows) ** config.the['min']

        cols = cols if cols else self.cols.x

        node = {'data': self.clone(rows)} 

        if len(rows) > 2 * min :
            left, right, node["A"], node["B"], node["mid"], _ = self.half(rows,cols,above)
            if self.better(node["B"],node["A"]):
                left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
            node["left"]  = self.sway(left,  min, cols, node["A"]) 
        
        return node 
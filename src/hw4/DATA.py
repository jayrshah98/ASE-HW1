from typing import Union, List, Dict
from LIB import LIB
from ROW import ROW
from COLS import COLS
import math
import copy
import config

lib = LIB()
csv = lib.csv
rnd = lib.rnd
kap = lib.kap
cosine = lib.cosine
many = lib.many
any = lib.any
dofile = lib.dofile
copy = lib.copy

class DATA:
    
    def __init__(self, src):
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

    def clone(self, rows = None):
        data = DATA([self.cols.names])
        for row in rows:
            data.add(row)
        return data


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
        # print("This is row 1")
        # print(row1.cells)
        # print("This is row2")
        # print(row2.cells)
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


def repCols(cols):
    cols = copy(cols)
    for col in cols:
        col[len(col)-1] = str(col[0]) + ":" + str(col[len(col)-1])
        for j in range(1,len(col)):
            col[j-1] = col[j] 
        col.pop()
    cols.insert(0,["Num" + str(j) for j in range(len(cols[0]))])
    cols[0][len(cols[0]) - 1] = "thingX"
    return DATA(cols)
        

def repRows(t, rows):
    rows = copy(rows)
    for j,s in enumerate(rows[-1]):
        rows[0][j] = str(rows[0][j]) + ":" + str(s)
    del rows[-1]
    for n,row in enumerate(rows):
        if n==0:
            row.append("thingX")
        else:
            u = t["rows"][len(t["rows"]) - n]
            row.append(u[-1])
    return DATA(rows)

    # def repPlace(self, data, n, g, maxx, maxy, x, y, c):
    #     n,g = 20,{}
    #     for i in range(0,n):
    #         g[i] = []
    #         for j in range(0,n):
    #             g[i][j]=" "
    #     maxy=0
    #     print("")
    #     for r,row in enumerate(data.rows):
    #         c = str(chr(64+r))
    #         print(c, (row.cells[-1]))
    #         x, y= row.x*n//1, row.y*n//1
    #         maxy = math.max(maxy,y)
    #         g[y][x] = c
    #     print("")
    #     for y in range(0, maxy):
    #         self.oo(g[y])

    # def repgrid(self, sFile):
    #     t = lib.dofile(sFile) 
    #     rows = self.repRows(t, lib.transpose(t.cols)) 
    #     cols = self.repCols(t.cols)
    #     lib.show(rows.cluster())
    #     lib.show(cols.cluster())
    #     self.repPlace(rows)
        
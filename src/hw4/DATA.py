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
    
    def __init__(self, src = config.the["file"]):
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
        data_1 = self
        data_1.row = passed_fields
        return data_1

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
            # print("row1", row1.cells)
            # print("row2", row2.cells)
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**float(config.the['p'])
        return (d/n)**(1/float(config.the['p']))

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
            return {'row': row, 'dist': cosine(dist(row,A), dist(row,B), c)}

        def dist(row1,row2):
            return self.dist(row1,row2,cols)

        if rows == None:
            rows = self.rows
        some = many(rows,int(config.the['Sample']))

        A  = above if above!=None else any(some)
        B  = self.around(A,some)[int(config.the['Far'] * len(rows))//1].row
        c  = dist(A,B)

        left, right = [], []
        for n,tmp in enumerate(sorted(map(rows, project), "dist")):
            if   n <= len(rows)//2: 
                left.append(tmp.row)
                mid = tmp.row
            else: right.append(tmp.row)
        return left, right, A, B, mid, c

    def cluster(self, rows, min, cols, above):

        if rows == None:
            rows = self.rows

        min  = min or (len(rows))**(config.the['min'])

        if cols == None:
            cols = self.cols.x

        node = {'data': self.clone(rows)} 

        if len(rows) > 2 * min:
            left, right, node.A, node.B, node.mid = self.half(rows,cols,above)
            node.left  = self.cluster(left,  min, cols, node.A)
            node.right = self.cluster(right, min, cols, node.B)

        return node 

    def furthest(self, row1, rows, cols, t):
        t = self.around(row1,rows,cols)
        return t[len(t)]

    def repCols(self,cols):
        cols = copy(cols)
        for _,col in enumerate(cols):
            col[len(col)-1] = col[0] + ":" + col[len(col)-1]
            for j in range(1,len(col)-1):
                col[j-1] = col[j] 
            col[len(col)]= None 
        cols.insert(cols, 1, self.kap(cols[1], lambda k,v: "Num" + k))
        cols[1][len(cols[1])] = "thingX"
        return DATA(cols)
        

    def repRows(self, t, rows):
        rows = copy(rows)
        print(rows)
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

    def repPlace(self, data, n, g, maxx, maxy, x, y, c):
        n,g = 20,{}
        for i in range(0,n):
            g[i] = []
            for j in range(0,n):
                g[i][j]=" "
        maxy=0
        print("")
        for r,row in enumerate(data.rows):
            c = str(chr(64+r))
            print(c, (row.cells[-1]))
            x, y= row.x*n//1, row.y*n//1
            maxy = math.max(maxy,y)
            g[y][x] = c
        print("")
        for y in range(0, maxy):
            self.oo(g[y])

    def repgrid(self, sFile):
        t = lib.dofile(sFile) 
        rows = self.repRows(t, lib.transpose(t.cols)) 
        cols = self.repCols(t.cols)
        lib.show(rows.cluster())
        lib.show(cols.cluster())
        self.repPlace(rows)
        
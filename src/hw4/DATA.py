from main import main
from typing import Union, List, Dict
from LIB import LIB
from ROW import ROW
from COLS import COLS
import math
import copy

lib = LIB()
csv = lib.csv
rnd = lib.rnd
kap = lib.kap
cosine = lib.cosine
many = lib.many
any = lib.any

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
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**float(main.the['p'])
        return (d/n)**(1/float(main.the['p']))

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
        some = many(rows,int(main.the['Sample']))

        A  = above if above!=None else any(some)
        B  = self.around(A,some)[int(main.the['Far'] * len(rows))//1].row
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

        min  = min or (len(rows))**(main.the['min'])

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
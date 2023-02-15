from typing import Union, List, Dict
from LIB import LIB
from ROW import ROW
from COLS import COLS
import math
import copy
import config
from collections.abc import Iterable

lib = LIB()
csv = lib.csv
rnd = lib.rnd
kap = lib.kap
cosine = lib.cosine
many = lib.many
any = lib.any

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

    def clone(self, rows=None):
        data = DATA([self.cols.names])
        for row in rows:
            data.add(row)
        return data


    def stats(self, what,cols,nPlaces):
        def fun(k, col):
            return rnd(getattr(col, what or 'mid')(), nPlaces), col.txt
        return kap(cols or self.cols.y, fun)
        

    def better(self,row1,row2):
        s1, s2, ys = 0, 0, self.cols.y

        for _,col in enumerate(ys):
            x  = col.norm( row1.cells[col.at] )
            y  = col.norm( row2.cells[col.at] )
            s1 = s1 - math.exp(col.w * (x-y) / len(ys))
            s2 = s2 - math.exp(col.w * (y-x) / len(ys))
        return s1/len(ys) < s2/len(ys)

    def dist(self,row1,row2,cols=None):
        n,d = 0,0
        cols = (cols if cols else self.cols.x)
        for _,col in enumerate(cols):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**(config.the['p'])
        return (d/n)**(1/(config.the['p']))

    def around(self,row1,rows=None,cols=None):

        rows = (rows if rows else self.rows)
        cols = (cols if cols else self.cols.x)
        def fun(row2):
            return {'row': row2, 'dist':self.dist(row1,row2,cols)}
        return sorted(list(map(fun, rows)), key=lambda x: x['dist'])


    def half(self,rows=None,cols=None,above=None):

        
        def dist1(row1,row2):
            return self.dist(row1,row2,cols)

        def project(row):
            return {'row': row, 'dist': cosine(dist1(row,A), dist1(row,B), c)}

        if not rows:
            rows = self.rows

        some = many(rows,config.the['Sample'])

        A  = above or any(some)
        
        B = self.around(A, some)[int((config.the["Far"] * len(rows)) // 1)]["row"]
        c  = dist1(A,B)
        left, right = [], []
        result = [project(row) for row in rows]
        sorted(result,key = lambda x: x["dist"])
        
        for n,tmp in enumerate(result):
            if n <= len(rows) // 2: 
                left.append(tmp["row"])
                mid = tmp["row"]                
            else: 
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    def cluster(self, rows = None, min = None, cols = None, above = None):

        if rows == None:
            rows = self.rows

        min = min if min else len(rows)**(config.the['min'])
        if cols == None:
            cols = self.cols.x

        node = {'data': self.clone(rows)} 

        if len(rows) > 2 * min:

            left, right, node["A"], node["B"], node["mid"],_ = self.half(rows,cols,above)
            node["left"]  = self.cluster(left,  min, cols, node["A"])
            node["right"] = self.cluster(right, min, cols, node["B"])

        return node 

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
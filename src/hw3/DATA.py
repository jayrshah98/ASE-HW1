from main import main
from LIB import LIB
from ROW import ROW
from COLS import COLS
import math

lib = LIB()
csv = lib.csv
rnd = lib.rnd
kap = lib.kap

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
        data = DATA(self.cols.names)
        for row in passed_fields:
            self.add(row)
        return data

    def stats(self, nPlaces, what = "mid", cols = None):
        def fun(k, col):
            return rnd(getattr(col, what or 'mid')(), nPlaces), col.txt
        return kap(cols or self.cols.y, fun)

    def better(self,row1,row2,s1,s2,ys,x,y):
        s1, s2, ys, x, y = 0, 0, self.cols.y
        for _,col in ys:
            x  = col.norm( row1.cells[col.at] )
            y  = col.norm( row2.cells[col.at] )
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)

    def dist(self,row1,row2,cols,n,d):
        n,d = 0,0
        for _,col in (cols or self.cols.x):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**main.the['p']
        return (d/n)**(1/main.the['p'])

    def around(self,row1,rows,cols):
        def fun(row2):
            return {'row': row2, 'dist':self.dist(row1,row2,cols)}
        return sorted(map(rows or self.rows)), fun,"dist"


    def half(self,rows,cols,above):

        def project(row):
            return {'row': row, 'dist': cosine(dist(row,A), dist(row,B), c)}

        def dist(row1,row2):
            return self.dist(row1,row2,cols)

        rows = rows or self.rows
        some = many(rows,main.the['Sample'])

        A    = above or any(some)
        B    = self.around(A,some)[(main.the['Far'] * len(rows))//1].row
        c    = dist(A,B)

        left, right = {}, {}
        for n,tmp in enumerate(sorted(map(rows, project), "dist")):
            if   n <= len(rows//2): 
                left.append(tmp.row)
                mid = tmp.row
            else: right.append(tmp.row)
        return left, right, A, B, mid, c
    

    def cluster(self, rows, min, cols, above):

        rows = rows or self.rows
        min  = min or (len(rows))**(main.the['min'])
        cols = cols or self.cols.x
        node = {'data': self.clone(rows)} 
        if len(rows) > 2 * min:
            left, right, node.A, node.B, node.mid = self.half(rows,cols,above)
            node.left  = self.cluster(left,  min, cols, node.A)
            node.right = self.cluster(right, min, cols, node.B)

        return node 

    def sway(self,rows,min,cols,above):
        rows = rows or self.rows
        min  = min or (len(rows)) ** (main.the['min'])
        cols = cols or self.cols.x
        node = {'data': self.clone(rows)} 
        if len(rows) > 2 * min :
            left, right, node.A, node.B, node.mid = self.half(rows,cols,above)
            if self.better(node.B,node.A):
                left, right, node.A, node.B = right, left, node.B, node.A
            node.left  = self.sway(left,  min, cols, node.A) 
        return node 
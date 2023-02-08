import math
import random
import re
import sys
from pathlib import Path
from DATA import DATA
from LIB import LIB
lo = float('inf') 
hi = float('-inf')
seed = 937162211 

class LIB:

    def __init__(self):
        pass

    def rint(self, lo, hi):
        return math.floor(0.5 + random.Random(lo,hi))

    def rand(self,lo =0, hi =1):
        global seed
        seed = (16807 * seed) % 2147483647
        return lo + (hi-lo) * seed / 2147483647

    def rnd(self, n, nPlaces = 3):
        mult = 10**(nPlaces)
        return math.floor(n * mult + 0.5) / mult   

    def coerce(self,s):
        def fun(s1):
            if s1 == "true" or s1 == "True":
                return True
            elif s1 == "false" or s1 == "False":
                return False
            else:
                return s1
        if type(s) == bool:
            return s
        try:
            result = int(s)
        except:
            try:
                result = float(s)
            except:
                result = fun(re.match("^\s*(.+)\s*$", s).string)
        return result

    def csv(self,sFilename,fun):
        filePath = Path(sFilename)
        filePath = filePath.absolute()
        filePath = filePath.resolve()
        f = open(filePath,"r")
        readLines = f.readlines()
        f.close()
        for line in readLines:
            t = []
            for s1 in re.findall("([^,]+)", line):
                t.append(self.coerce(s1))
            fun(t)
    
    def kap(self, t, fun):
        u = {}
        for k, v in enumerate(t):
            v, k = fun(k, v)
            u[k or len(u)+1] = v
        return u
    
    # def o():
    #     return

    def many(self,t,n, u):
        u={}
        for _ in range(1,n):
            u[ 1 + len(u)] = self.any(t)
        return u    


    def transpose(self, t, u):
        u = []
        for i in range(0, len(t[0])):
            u[i] = []; 
            for j in range(0, len(t)):
                u[i][j] = t[j][i]
        return u 

    def repCols(self,cols):
        cols = self.copy(cols)
        for _,col in enumerate(cols):
            col[len(col)-1] = col[0] + ":" + col[len(col)-1]
            for j in range(1,len(col)-1):
                col[j-1] = col[j] 
            col[len(col)]= None 
        cols.insert(cols, 1, self.kap(cols[1], lambda k,v: "Num" + k))
        cols[1][len(cols[1])] = "thingX"
        return DATA(cols)
        

    def repRows(self, t, rows, u):
        rows = self.copy(rows)

        for j,s in enumerate(rows[len(rows)]):
            rows[1][j] = rows[1][j] + ":" + s
        rows[len(rows)] = None

        for n,row in enumerate(rows):
            if n==1:
                row.append("thingX")
            else:
                u = t.rows[len(t.rows) - n + 2]
                row.append(u[len(u)])
        return  DATA(rows)

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

    def dofile(filename):
        file = open(filename, 'r')
        return file.read()

    def repgrid(self, sFile,t,rows,cols):
        t = self.dofile(sFile) 
        rows = self.repRows(t, self.transpose(t.cols)) 
        cols = self.repCols(t.cols)
        self.show(rows.cluster())
        self.show(cols.cluster())
        self.repPlace(rows)
        

    def settings(self,s):
        t={}
        res = re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s)
        for k,v in res:
             t[k] = self.coerce(v)
        return t
    
    def cli(self,options):
        for k,v in options.items():
            v = str(v)
            for n, x in enumerate(sys.argv):
                if x== "-" + k[0] or x == "--" + k:
                  v = (sys.argv[n + 1] if n + 1 < len(
                        sys.argv) else False) or v == "False" and "true" or v == "True" and "false"
                options[k] = self.coerce(v)
        return options

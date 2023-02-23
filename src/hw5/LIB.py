import math
import random
import re
import sys
import json
from pathlib import Path
import config

lo = float('inf') 
hi = float('-inf')


class LIB:
    def __init__(self):
        self.seed = 937162211

    def rint(self, lo=None, hi=None):
        return math.floor(0.5 + self.rand(lo,hi))
    
    def seed_set(self,v):
        self.seed = v

    def rand(self,lo=None, hi=None):
        lo, hi = lo or 0, hi or 1
        self.seed = (16807 * self.seed) % 2147483647
        return lo + (hi-lo) * self.seed / 2147483647

    def cosine(self, a,b,c):
        x1 = (a**2 + c**2 - b**2) / (2**c)
        x2 = max(0,min(1,x1))
        y = (abs(a**2 - x2**2))**(0.5)
        return (x2, y)

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


    def many(self,t,n, u):
        u = []
        for i in range(1, n + 1):
         u.append(self.any(t))
        return u  

    
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

    
    def last(self,t):
        return t[-1]

    def show(self,node,what=None,cols=None,nPlaces=None,lvl=0):
        if node:
            lvl = lvl or 0
            print("|.. " * lvl, end="")
            if ("left" not in node):
                print(self.last(self.last(node["data"].rows).cells))
            else:
                print(str(int(100 * node["C"])))
            self.show(node.get("left", None), what,cols, nPlaces, lvl+1)
            self.show(node.get("right", None), what,cols,nPlaces, lvl+1)

    def oo(self,t):
        td = t.__dict__
        td['a'] = t.__class__.__name__
        td['id'] = id(t)
        print(dict(sorted(td.items())))

    def has(self, col):
        if not hasattr(col, "isSym") and not hasattr(col, "ok"):
            self.sorted(col.has) 
        return col.has

    def per(self, t, p):
        p = math.floor((( p or .5 ) * len(t) ) + .5)
        return t[max(1, min(len(t), p))]

    def mid(self, col):
        return col.mode if hasattr(col, "isSym") else self.per(self.has(col), 0.5)

    def div(self, col):
        if hasattr(col, "isSym"):
            e = 0
            for n in col.has.values():
                e = e - n/col.n * math.log(n/col.n, 2)
            return e
        else:
            return (self.per(self.has(col),.9) - self.per(self.has(col), .1)) /2.58

    def stats(self, data, nPlaces, fun = None, cols = None):
        cols = cols if cols else data.cols.y

        def fun(col):
            return self.rnd((fun if fun else self.mid)(col), nPlaces), col.txt

        tmp = self.kap(cols, fun)
        tmp["N"] = len(data.rows)
        return tmp, map(self.mid, cols)
    
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

    def row(data,t):
        if data.cols:
            t.push(data.rows)
    
import math
import random
import re
import sys
from pathlib import Path
import config

lo = float('inf') 
hi = float('-inf')
seed = 937162211 

class LIB:

    def __init__(self):
        pass

    def rint(self, lo, hi):
        return math.floor(0.5 + self.rand(lo,hi))

    def rand(self,lo, hi):
        global seed
        lo, hi = lo or 0, hi or 1
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
        for k,v in enumerate(t):
            v, k = fun(k,v) 
            u[k or len(u)+1] = v
        
        return u
    
    def o(self):
        return
    
    def cosine(self, a,b,c):
        x1 = (a**2 + c**2 - b**2) / (2**c)
        x2 = max(0,min(1,x1))
        y = (abs(a**2 - x2**2))**(0.5)
        return (x2, y)

    def any(self, t):
       rintVal = self.rint(None, len(t) - 1)
       return t[rintVal]

    def many(self,t,n):
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

    def show(self,node,what,cols,nPlaces,lvl=None):
        if node:
             lvl = lvl or 0
             print("| " * lvl + str(len(node["data"].rows)) + " ", end="")
             if ("left" not in node) or lvl == 0:
                print(node["data"].stats("mid", node["data"].cols.y, nPlaces))
             else:
                print("")
             self.show(node.get("left", None), what, cols, nPlaces, lvl+1)
             self.show(node.get("right", None), what, cols, nPlaces, lvl+1)

import math
import random
import re
import sys
from pathlib import Path
import copy
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

        try:
            return int(s)
        except:
            try:
                return float(s)
            except:
                pass

        if s == "true" or s == "True":
            return True
        elif s == "false" or s == "False":
            return False
        else:
            return s       

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

    def map(self, t, fun, u):
        u = {}
        for k,v in t.items():
            v,k = fun(v)
            if u.get(k) is not None:
                u[k] = v
            else:
                u[len(u)+1] = v

    def transpose(self, t, u):
        u = []
        for i in range(0, len(t[0])):
            u[i] = []; 
            for j in range(0, len(t)):
                u[i][j] = t[j][i]
        return u 

    def cosine(self, a,b,c):
        x1 = (a*a + c*c - b*b) / (2*c + 0.00001)
        x2 = max(0,min(1,x1))
        y = (abs(a*a - x2*x2))**(0.5)
        return (x2, y)    

    def any(self, t):
        rVal = self.rint(None, len(t)-1)
        return t[rVal]
    
    def many(self,t,n):
        u = []
        for i in range(1, n+1):
            u.append(any(t))
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

    def copy(self,t):
        return copy.deepcopy(t)

    def dofile(self,filename):
        file = open(filename, 'r')
        return file.read()

    def last(self,t):
        return t[len(t)]

    def show(self,node,what,cols,nPlaces,lvl):
        if node:
            lvl = lvl if lvl else 0
            print(("|.. ").rep(lvl))
            print(self.o(self.last(self.last(node.data.rows).cells)) if not node.left else self.rnd(100*node.c))
            self.show(node.left, what,cols, nPlaces, lvl+1)
            self.show(node.right, what,cols,nPlaces, lvl+1)


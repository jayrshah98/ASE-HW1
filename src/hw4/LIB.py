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

    def copy(t):
        return copy.deepcopy(t)


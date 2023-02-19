import math
import random
import re
import sys
import json
from pathlib import Path
import copy
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
        mult = math.pow(10,nPlaces)
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
        u = []
        for i in range(1, n + 1):
         u.append(self.any(t))
        return u  

    # def map(self, t, fun, u):
    #     u = {}
    #     for k,v in t.items():
    #         v,k = fun(v)
    #         if u.get(k) is not None:
    #             u[k] = v
    #         else:
    #             u[len(u)+1] = v

    def transpose(self, t):
        u = []
        for i in range(0, len(t[0])):
            u.append([])
            for j in range(0, len(t)):
                u[i].append(t[j][i])
        return u 

    def cosine(self, a,b,c):
        x1 = (a*a + c*c - b*b) / (2*c or 1)
        x2 = max(0,min(1,x1))
        y = (abs(a*a - x2*x2))**(0.5)
        return (x2, y)    

    def any(self, t):
        rVal = self.rint(0, len(t)-1)
        return t[rVal]
    
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

    def dofile(self,filepath):
        filepath = (Path(__file__).parent / filepath).resolve()
        file = open(filepath,"r",encoding = "utf-8")
        temp = (
        re.findall(r"(?<=return )[^.]*", file.read())[0]
        .replace("{", "[")
        .replace("}", "]")
        .replace("=", ":")
        .replace("[\n", "{\n")
        .replace(" ]", " }")
        .replace("'", '"')
        .replace("_", '"_"')
        )
        file.close()
        f = json.loads(re.sub(r"(\w+):", r'"\1":', temp)[:-2] + "}")
        return f


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


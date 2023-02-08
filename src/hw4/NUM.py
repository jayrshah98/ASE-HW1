import re
import math
from LIB import LIB
lib = LIB()
rnd = lib.rnd

class NUM:
    def __init__(self,at=0,txt=""):
        self.at = at
        self.txt = txt
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float('inf') 
        self.hi = float('-inf')
        x = re.search('-$',txt)
        if(x==None):
            self.w = 1
        else:
            self.w = -1

    def add(self, n):
        if n != 0:
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d* (n - self.mu)
            self.lo = min(n,self.lo)
            self.hi = max(n,self.hi)
    
    def mid(self):
        return self.mu

    def div(self):
        return 0 if (self.m2 < 0 or self.n < 2) else (self.m2/(self.n-1))**0.5
   
    def rnd(self,x,n):
        return x if x == "?" else rnd(x,n)
    
    def dist(self,n1,n2):

        if n1 == "?" and n2 == "?":
            return 1 

        n1,n2 = self.norm(n1), self.norm(n2)

        if n1 == "?":
            n1 = 1 if n2<.5 else 0

        if n2 == "?":
            n2 = 1 if n1<.5 else 0 

        return math.abs(n1 - n2)  

    def norm(self,n):
	    return n if n == '?' else (n-self.lo) / (self.hi - self.lo + 1e-32)

    
    
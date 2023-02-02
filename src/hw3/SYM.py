import math
import collections

class SYM:

    def __init__(self,at = 0, txt = ""):
        self.at = at
        self.txt = txt
        self.n = 0
        self.has = collections.defaultdict(int)
        self.most = 0
        self.mode = None 
        pass

    def add(self,x):
        if x:
            self.n = self.n + 1 
            self.has[x] = self.has[x] + 1
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x
        return x
    
    def mid(self):
        return self.mode
    
    def div(self):
        def fun(p):
            return p * math.log(p,2)
        e = 0

        for j in list(self.has.keys()):
            e = e + fun(self.has[j]/self.n)
        return -e

    def rnd(i, x):
        return x
    
    def dist(self,s1,s2):
        if s1 == s2 == '?':
            return 1
        elif s1 == s2:
            return 0
        return 1

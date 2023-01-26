import re
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

    def add(self, n, d):
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
    
    # def rnd(self, x, n):
    #     Mathf.round


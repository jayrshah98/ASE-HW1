class NUM:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float('inf') 
        self.hi = float('-inf')


    def add(self, n):
        if n != 0:
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.mu = self.mu + d* (n - self.mu)
            self.lo = min(n,self.lo)
            self.hi = max(n,self.hi)


    def mid(self,x):
        return self.mu

    def div(self,x):
        return 0 if (self.m2 < 0 or self.n < 2) else (self.m2/(self.n-1))**0.5    
    
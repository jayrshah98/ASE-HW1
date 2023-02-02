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
import re

class NUM: 
    
    def __init__(self, n=0 , s="") -> None:
        self.at = n if n else 0
        self.txt = s if s else ""
        self.n = 0
        self.hi = float('-inf')
        self.lo= float('inf')
        self.ok= True
        self.has= []
        self.w = -1 if self.txt.endswith("-") else 1
    
    def norm(self,n):
        return n if n == "?" else (n - self.lo) / (self.hi - self.lo + 1 / float("inf"))
        
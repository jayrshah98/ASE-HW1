import re
from NUM import NUM
from SYM import SYM

class COLS:
    def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None
    
        for n,s in enumerate(t):
            if re.findall("^[A-Z]+", s): col = NUM(n,s)
            else: col = SYM(n,s)
            self.all.append(col)
            if not re.findall("X$", s):
                if re.findall("!$", s):
                    self.klass = col
                self.y.append(col) if re.findall("[!+-]$", s) else self.x.append(col)
            
    def add(self,row):
        for t in self.x, self.y:
            for col in t:
                col.add(row.cells[col.at])

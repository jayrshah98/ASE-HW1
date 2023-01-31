import re
from NUM import NUM
from SYM import SYM

class COLS:
    def __init__(self, t, col, cols):
        self.names = t
        self.all = {}
        self.x = {}
        self.y = {}
        self.klass = None
    
    def assign_cols(self):
        for n,s in enumerate(t):
            col = NUM(n,s) if re.findall("^[A-Z]+", s) else SYM(n,s)
            self.all.append(col)
            if not re.find("X$", s):
                if re.find("!$", s):
                    self.klass = col
                self.all.append ( self.y if re.find("[!+-]$", s) else self.x, col)
            
    def add(self,row):
        for _,t in self.x, self.y:
            for _,col in t.items():
                col.append(row.cells[col.at])
        

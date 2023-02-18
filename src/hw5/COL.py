import re
from NUM import NUM
from SYM import SYM

class COL:
    
    def __init__(self,n,s,col) -> None:
        col = NUM(n,s) if re.match("^[A-Z]", s) else SYM(n,s) 
        self.isIgnored  = re.match("X$", self.col.txt)
        self.isKlass    = re.match("!$", self.col.txt) 
        self.isGoal     = re.match("[!+-]$", self.col.txt)

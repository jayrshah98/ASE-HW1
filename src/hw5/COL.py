from NUM import NUM
from SYM import SYM

class COL:
    
    def __init__(self,n,s) -> None:
        
        self.col = NUM(n, s) if s[0].isupper() else SYM(n, s)
        self.isIgnored  = self.col.txt.endswith("X")
        self.isKlass    = self.col.txt.endswith("!") 
        self.isGoal     = self.col.txt.rstrip().rstrip('\n')[-1] in ["!", "+", "-"]
        # print(self.col.txt[-1], self.isGoal)

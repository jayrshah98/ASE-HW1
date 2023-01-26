class COLS:
    def __init__(self, t, col, cols):
        self.names = t
        self.all = {}
        self.x = {}
        self.y = {}
        self.klass = null
    for n,s in enumerate(t):
        col = s:find"^[A-Z]+" if NUM(n,s) else SYM(n,s)
        self.all.append(col)
        if not s:find"X$":
            if s:find"!$":
                self.klass = col
            push(s:find"[!+-]$" if self.y else self.x, col)
        
    def add(self,row):
        for _,t in self.x, self.y:
            for _,col in t.items():
                col.append(row.cells[col.at])
    
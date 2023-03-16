from COL import COL

class COLS:
    
    def __init__(self, ss):
        self.names = ss
        self.all = []
        self.x = []
        self.y = []

        for n,s in enumerate(ss):
            col = COL(n, s)
            self.all.append(col)

            if not col.isIgnored:
                if hasattr(col, 'isKlass'):
                    self.klass = col
                
                self.y.append(col) if col.isGoal else self.x.append(col)
                    
    def add(self,row):
        for t in self.x, self.y:
            for col in t:
                col.add(row.cells[col.at])
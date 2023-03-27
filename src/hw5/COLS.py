from COL import COL

class COLS:
    
    def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []

        for n,s in enumerate(t):
            col = COL(n, s)
            self.all.append(col)
            if not col.isIgnored:
                if hasattr(col, 'isKlass') and col.isKlass:
                    self.klass = col
                if(col.isGoal):
                    self.y.append(col)
                else:
                    self.x.append(col)
                    
from LIB import LIB
from COLS import COLS
import UPDATE
import config
from NUM import NUM

num = NUM()
lib = LIB()
class DATA:
    def __init__(self, src, rows=None):
        self.rows = []
        self.cols = None
        add = lambda x: UPDATE.row(self,x)
        if isinstance(src, str):
                lib.csv(src, add)
        else:
                self.cols = COLS(src.cols.names)
                if rows:
                    for row in rows:
                        add(row)
        

    def new(self):
        return {"rows": [], "cols": None}
    
    def read(self,sfile,data = None):
        data = DATA()
        callback = lambda t: UPDATE.row(data, t)
        lib.csv(sfile, callback)
        return data

    def dist(self, data, t1, t2, cols = None):
    
        def dist1(col, x, y):
            if x == "?" and y == "?":
                return 1
            if hasattr(col, "isSym"):
                return 0 if x == y else 1
            else:                
                if x == "?":
                    y = float(y)
                    x = 1 if y < 0.5 else 1
                elif y == "?":
                    x = float(x)
                    y = 1 if x < 0.5 else 1 
                # print("col:",col)
                # print("x",float(x))
                else:
                    x = float(x)
                    y = float(y)
                    x, y = num.norm(col,x), num.norm(col,y)
                return abs(x - y)

        d, n = 0, 1 / float("inf")
        cols = cols or data.cols.x
        
        for col in cols:
            n += 1
            d += dist1(col.col, t1[col.col.at], t2[col.col.at]) ** config.the['p']
            
        return (d / n)**(1 / config.the['p'])
    


    def around(self,row1,rows=None,cols=None):

        if rows == None:
            rows = self.rows

        if cols == None:
            cols = self.cols.x

        def fun(row2):
            return {'row': row2, 'dist':self.dist(row1,row2,cols)}

        return sorted(list(map(fun, rows)), key=lambda x: x['dist'])


    def half(self, data, rows=None, cols=None, above=None):
        left, right = [], []

        def gap(r1, r2):
            return self.dist(data, r1, r2, cols)

        def cos(a, b, c):
            return (a ** 2 + c ** 2 - b ** 2) / (2 * c)

        def proj(r):
            return {'row': r, 'x': cos(gap(r, A), gap(r, B), c)}

        rows = rows or self.rows
        some = lib.many(rows, config.the["Halves"])
        A = above if config.the["Reuse"] else lib.any(some)
        tmp = sorted([{"row": r, "d": gap(r, A)} for r in some], key=lambda x: x["d"])
        far = tmp[int((len(tmp)) * config.the["Far"])]
        B, c = far["row"], far["d"]

        for n, two in enumerate(sorted(map(proj, rows), key=lambda x: x["x"])):
            if n + 1 <= (len(rows) / 2):
                left.append(two["row"])
            else:
                right.append(two["row"])
        evals = 1 if (hasattr(config.the, "Reuse") and above) else 2
        return left, right, A, B,c, evals
    

    def tree(self,data,rows = None,cols = None,above = None):
        rows = rows or data.rows
        here = {"data" : DATA(data, rows)}
        left, right, A, B, _,_= self.half(data, rows, cols, above)
        if len(rows)>=2*(len(data.rows) ** config.the['min']):
            left, right, A, B, _,_= self.half(data, rows, cols, above)
            here["left"] = self.tree(data, left, cols, A)
            here["right"] = self.tree(data, right, cols, B) 
        return here
    
    def showTree(self,tree,lvl=0):
        if tree:
            print("{}[{}]".format("|.. " * lvl, len(tree["data"].rows)), end="")
            if lvl == 0 or not "left" in tree:
                print(lib.stats(tree["data"]))
            else:
                print("")
            self.showTree(tree["left"] if "left" in tree else None, lvl + 1)
            self.showTree(tree["right"] if "right" in tree else None, lvl + 1)

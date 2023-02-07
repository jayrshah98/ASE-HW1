from SYM import SYM
from NUM import NUM
from DATA import DATA
from lib import LIB
import config

lib = LIB()
sym = SYM()
num = NUM()
data = DATA(config.the["file"])

rnd = lib.rnd
rand = lib.rand
csv = lib.csv
o = lib.o

def sym_test():
    pairs = ["a","a","a","a","b","b","c"]
    for x in pairs: 
        sym.add(x)
    res = "a" == sym.mid() and 1.379 == rnd(sym.div())
    return res

def num_test():
    pairs = [1,1,1,1,2,2,3]
    for x in pairs:
        num.add(x) 
    res = 11/7 == num.mid() and 0.787 == rnd(num.div())
    return res

def the_test():
    print(str(config.the))

def csv_test():
    global n
    n = 0
    def fu(t):
        global n
        n += len(t)
    csv(config.the["file"],fu)
    res = 8*399 == n
    return res

def data_test(): 
   return len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[0].at == 0 and len(data.cols.x) == 4

def stats_test():
  pairs = { 'y': data.cols.y, 'x' : data.cols.x }
  for k,cols in pairs.items():
    print(k + "mid" + o(data.stats(2, "mid",cols)))
    print("" + "div" + o(data.stats(2, "div",cols)))


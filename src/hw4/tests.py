from SYM import SYM
from NUM import NUM
from DATA import DATA
from LIB import LIB
import config

lib = LIB()
sym = SYM()
num = NUM()
data = DATA(config.the["file"])

rnd = lib.rnd
rand = lib.rand
csv = lib.csv

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

def copy_test():
    t1 = {'a':1,'b':{'c':2,'d':{3}}}
    t2 = lib.copy(t1)
    t2.b.d[0] = 1000
    print("b4",t1,"\nafter",t2)

def repcols_test():
    t = lib.repCols(lib.dofile(config.the.file).cols)
    print(t.cols.all)
    print(t.rows)


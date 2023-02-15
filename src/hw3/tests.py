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


def test_clone():
    data1 = DATA(config.the["file"])
    data2 = data1.clone(data1.rows)

    return (
        len(data1.rows) == len(data2.rows)
        and data1.cols.y[1].w == data2.cols.y[1].w
        and data1.cols.x[1].at == data2.cols.x[1].at
        and len(data1.cols.x) == len(data2.cols.x)
    )

def stats_test():
  pairs = { 'y': data.cols.y, 'x' : data.cols.x }
  for k,cols in pairs.items():
    print(k + "\tmid\t" + str(data.stats("mid",cols,2)))
    print("" + "\tdiv\t" + str(data.stats("div",cols,2)))
  return True

def half_test():
    data = DATA(config.the['file'])
    left,right,A,B,mid,c = data.half()
    print(len(left),len(right),len(data.rows))
    print(A.cells,c)
    print(mid.cells)
    print(B.cells)
    return True

def cluster_test():
    data = DATA(config.the['file'])
    lib.show(data.cluster(),"mid",data.cols.y,1)


def test_around():
    data=DATA(config.the['file'])
    print(0,0,data.rows[0].cells)
    for n,t in enumerate(data.around(data.rows[0])):
        if (n+1) %50 ==0:
            print(n, rnd(t['dist'],2) ,t['row'].cells)

def test_optimize():
    data = DATA(config.the['file'])
    lib.show(data.sway(), "mid", data.cols.y, 1)
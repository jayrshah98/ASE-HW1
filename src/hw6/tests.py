import config
from LIB import LIB
from NUM import NUM
from SYM import SYM
from DATA import DATA
from UPDATE import *
import OPTIMIZATION
import DISCRETIZATION as discretization
lib = LIB()
num = NUM()
rint = lib.rint
rand = lib.rand
rnd = lib.rnd
mid = lib.mid

def the_test():
    print(str(config.the))

def test_rand():
    t = []
    for i in range(1, 1000 + 1):
        t.append(rint(100))
    u = []
    for i in range(1, 1000 + 1):
        u.append(rint(100))

    for k, v in enumerate(t):
        assert v == u[k]

def num_test():
    num1 , num2 = NUM(), NUM()
    for i in range(10000):
        add(num1, rand())
    for i in range(10000):
        add(num2, rand()**2)
    print(1, rnd(mid(num1),2),round(lib.div(num1), 2))
    print(2, rnd(mid(num2),2),round(lib.div(num2), 2))
    return 0.5 == rnd(mid(num1),1) and mid(num1) > mid(num2)


def sym_test():
   
    sym = adds(SYM(), ["a","a","a","a","b","b","c"])
    print (lib.mid(sym), lib.rnd(lib.div(sym)), 2)
    return 1.38 == lib.rnd(lib.div(sym), 2)

def some_test():
    config.the["Max"] = 32
    num1 = NUM()
    for i in range(1,10000+1):
        add(num1,i)
    #print(lib.has(num1))

def csv_test():
    global n
    n = 0
    def fun(t):
        global n
        n += len(t)
    lib.csv(config.the['file'], fun) 
    return 3192 == n

def data_test():
    data = DATA(config.the['file'])
    col = data.cols.x[1].col
    print(col.lo, col.hi, lib.mid(col), lib.div(col))
    print(lib.stats(data)) 

def clone_test():
    data1 = DATA(config.the['file'])
    data2 = DATA(data1, data1.rows)
    print("data1:",lib.stats(data1, 2))
    print("data2:",lib.stats(data2, 2))


def cliffs_test():

    assert(lib.cliffsDelta( {8,7,6,2,5,8,7,3}, {8,7,6,2,5,8,7,3}) == False, "1")
    assert(lib.cliffsDelta( {8,7,6,2,5,8,7,3}, {9,9,7,8,10,9,6}) == True, "2") 

    t1, t2= [], []

    for _ in range(0, 1000):
        (t1.append(lib.rand()))
    for _ in range(0, 1000):
        (t2.append(lib.rand() ** 0.5))

    assert(lib.cliffsDelta(t1,t1)  == False, "3") 
    assert(lib.cliffsDelta(t1,t2) == True, "4") 

    diff, j = False, 1.0

    while not diff :

        def fun(x):
            return x * j

        t3 = map(fun, t1)
        diff = lib.cliffsDelta(t1, list(t3))
        print(">", lib.rnd(j), diff) 
        j = j * 1.025 


def dist_test():
    data = DATA(config.the['file'])
    num1 = NUM()
    #print(data.rows)
    for row in data.rows:
        add(num1, data.dist(data, row, data.rows[0]))
    print({"lo": num1.lo, "hi": num1.hi, "mid": lib.rnd(lib.mid(num1)), "div": lib.rnd(lib.div(num1))})

def half_test():
    data = DATA(config.the['file'])

    left, right, A, B, c,evals = data.half(data)
    print(len(left), len(right))

    l, r = DATA(data, left), DATA(data, right)
    print("l", lib.stats(l))
    print("r", lib.stats(r))

def tree_test():
    data = DATA(config.the['file'])
    data.showTree(data.tree(data))

def sway_test():
    data = DATA(config.the['file'])
    best,rest,_ = OPTIMIZATION.sway(data)
    print("\nall ", lib.stats(data))
    print("    ",   lib.stats(data,None, lib.div))
    print("\nbest", lib.stats(best))
    print("    ",   lib.stats(best,None, lib.div))
    print("\nrest", lib.stats(rest))
    print("    ",   lib.stats(rest,None, lib.div))
    print("\nall ~= best?", lib.diffs(best.cols.y, data.cols.y))
    print("best ~= rest?", lib.diffs(best.cols.y, rest.cols.y))

def bins_test():
    data = DATA(config.the['file'])
    best,rest,_ = OPTIMIZATION.sway(data)
    b4 = None
    print("all","","","", "{best= " + str(len(best.rows)) + ", rest= " + str(len(rest.rows)) + "}")
    result = discretization.bins(data.cols.x, {"best": best.rows, "rest": rest.rows})
    for t in result:
        for range in t:
            if range.txt != b4: 
                print("")
            b4 = range.txt
            print(range.txt,
                  range.lo,
                  range.hi,
                  round(lib.value(range.y.has, len(best.rows), len(rest.rows), "best")),
                  range.y.has)
            

def xpln_test():
    data = DATA(config.the['file'])
    best, rest, evals = OPTIMIZATION.sway(data)
    rule, _ = discretization.xpln(data, best, rest)
    print("\n-----------\nexplain=", discretization.showRule(rule))
    data1 = DATA(data, discretization.selects(rule, data.rows))
    print("all        ", lib.stats(data), lib.stats(data, None, lib.div))
    print(f"sway with   {evals} evals", lib.stats(best), lib.stats(best, None, lib.div))
    print(f"xpln on     {evals} evals", lib.stats(data1), lib.stats(data1, None, lib.div))
    top, _ = lib.betters(data, len(best.rows))
    top = DATA(data, top)
    print(f"sort with {len(data.rows)} evals", lib.stats(top), lib.stats(top, None, lib.div))


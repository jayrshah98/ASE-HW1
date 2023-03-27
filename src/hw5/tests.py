from SYM import SYM
from NUM import NUM
from DATA import DATA
from LIB import LIB
import config
from UPDATE import UPDATE
from discretization import *

lib = LIB()
data = DATA()
update = UPDATE()
num = NUM()
rint = lib.rint
seed_set = lib.seed_set
add = update.add
mid = lib.mid
div = lib.div
oo = lib.oo


def test_the():
    print(str(config.the))


def test_rand():
   
    seed_set(1)
    t = []
    for _ in range(1, 1000 + 1):
        t.append(rint(100))
    seed_set(1)
    u = []
    for _ in range(1, 1000 + 1):
        u.append(rint(100))

    for k, v in enumerate(t):
        assert v == u[k]


def test_some():
    config.the["Max"] = 32
    num1 = NUM()
    for i in range(1,10000+1):
        add(num1,i)
    print(lib.has(num1))

def test_sym():
   
    sym = update.adds(SYM(), ["a","a","a","a","b","b","c"])
    print (lib.mid(sym), lib.rnd(lib.div(sym)), 2)
    return 1.38 == lib.rnd(lib.div(sym), 2)

def test_num():
    num1 , num2 = NUM(), NUM()
    for i in range(10000):
        add(num1, lib.rand())
    for i in range(10000):
        add(num2, lib.rand()**2)
    print(1, lib.rnd(mid(num1),2), lib.rnd(lib.div(num1), 2))
    print(2, lib.rnd(mid(num2),2), lib.rnd(lib.div(num2), 2))

    return 0.5 == lib.rnd(mid(num1),1) and mid(num1) > mid(num2)

def test_csv():
    global n
    n = 0
    def fun(t):
        global n
        n += len(t)
    lib.csv(config.the['file'], fun) 
    return 3192 == n

def test_data():
    d = DATA()
    data = d.read(config.the['file'])
    col = data.cols.x[1].col
    print(col.lo, col.hi, lib.mid(col), lib.div(col))
    (lib.stats(data, 2)) 

def test_clone():
    d = DATA()
    data1 = d.read(config.the['file'])
    data2 = data1.clone(data1, data1.rows) 
    (lib.stats(data1, 2))
    (lib.stats(data2, 2))

def test_cliffs():

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

def test_dist():
    d = DATA()
    data = d.read(config.the['file'])
    for _,row in enumerate(data.rows):
        update.add(num, data.dist(data, row, data.rows[0]))
        
    print({"lo": num.lo, "hi": num.hi, "mid": lib.rnd(lib.mid(num)), "div": lib.rnd(lib.div(num))})

def test_half():
    d = DATA()
    data = d.read(config.the['file'])
    left, right, A, B, c = data.half(data)
    print(len(left), len(right))

    l, r = data.clone(data, left), data.clone(data, right)
   
    print("l", lib.stats(l))
    print("r", lib.stats(r))

def test_tree():
    data.showTree(data.tree(data.read(config.the['file'])))

def test_sway():
    d = DATA()
    data = d.read(config.the['file'])
    best, rest = data.sway(data)
    print("\nall ", lib.stats(data))
    print("    ",   lib.stats(data,None, lib.div))
    print("\nbest", lib.stats(best))
    print("    ",   lib.stats(best,None, lib.div))
    print("\nrest", lib.stats(rest))
    print("    ",   lib.stats(rest,None, lib.div))
    print("\nall ~= best?", lib.diffs(best.cols.y, data.cols.y))
    print("best ~= rest?", lib.diffs(best.cols.y, rest.cols.y))

def test_bins():
    d = DATA()
    data = d.read(config.the['file'])
    best,rest = data.sway(data)
    b4 = None
    print("all","","","", "{best= " + str(len(best.rows)) + ", rest= " + str(len(rest.rows)) + "}")
    result = bins(data.cols.x, {"best": best.rows, "rest": rest.rows})
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
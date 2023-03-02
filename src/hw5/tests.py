from SYM import SYM
from NUM import NUM
from DATA import DATA
from LIB import LIB
import config
from UPDATE import UPDATE

lib = LIB()
data = DATA()
update = UPDATE()
# sym = SYM()
num = NUM()
rint = lib.rint
seed_set = lib.seed_set
add = update.add
mid = lib.mid
div = lib.div
oo = lib.oo
def the_test():
    print(str(config.the))


def test_rand():
   
    seed_set(1)
    t = []
    for i in range(1, 1000 + 1):
        t.append(rint(100))
    seed_set(1)
    u = []
    for i in range(1, 1000 + 1):
        u.append(rint(100))

    for k, v in enumerate(t):
        assert v == u[k]

def test_some():
    config.the["Max"] = 32
    num1 = NUM()
    for i in range(1,10000+1):
        add(num1,i)
    print(lib.has(num1))




def sym_test():
   
    sym = update.adds(SYM(), ["a","a","a","a","b","b","c"])
    print (lib.mid(sym), lib.rnd(lib.div(sym)), 2)
    return 1.38 == lib.rnd(lib.div(sym), 2)

def num_test():
    
    num1, num2 = NUM(), NUM()

    for i in range(10000):
        add(num1, lib.rand())
    for i in range(10000):
        add(num2, lib.rand() ** 2)

    print(1, lib.rnd(lib.mid(num1), 1), lib.rnd(lib.div(num1), 1))
    print(2, lib.rnd(lib.mid(num2), 1), lib.rnd(lib.div(num2), 1))
    return .5 == lib.rnd(lib.mid(num1), 1) and lib.mid(num1) > lib.mid(num2)

def csv_test():
    global n
    n = 0
    def fun(t):
        global n
        n += len(t)
    lib.csv(config.the['file'], fun) 
    return 3192 == n

def data_test():
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
        update.add(num, d.dist(data, row, data.rows[0]))

    print({"lo": num.lo, "hi": num.hi, "mid": lib.rnd(lib.mid(num)), "div": lib.rnd(lib.div())})


def test_half():
    d = DATA()
    data = d.read(config.the['file'])

    left, right, A, B, c = data.half(data)
    print(len(left), len(right))

    l, r = d.clone(data, left), d.clone(data, right)
    print("l", lib.stats(l))
    print("r", lib.stats(r))

def test_tree():
    d = DATA()
    data = d.read(config.the['file'])
    lib.show(data.tree())

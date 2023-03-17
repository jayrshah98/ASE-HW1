import config
from LIB import LIB
from NUM import NUM
from SYM import SYM
from DATA import DATA
lib = LIB()
num = NUM()
seed_set = lib.seed_set
rint = lib.rint
rand = lib.rand
rnd = lib.rnd
mid = lib.mid

add = lib.add
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

def num_test():
    num1 , num2 = NUM(), NUM()
    seed_set(config.the['seed'])
    for i in range(1,10001):
        add(num1, rand())
    for i in range(1,10001):
        add(num2, rand()**2)
    print(1, rnd(mid(num1)),rnd(mid(num2)))
    return 0.5 == rnd(mid(num1)) and mid(num1) > mid(num2)


def sym_test():
   
    sym = lib.adds(SYM(), ["a","a","a","a","b","b","c"])
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
    d = DATA()
    data = d.read(config.the['file'])
    col = data.cols.x[1].col
    print(col.lo, col.hi, lib.mid(col), lib.div(col))
    (lib.stats(data, 2)) 

def clone_test():
    d = DATA()
    data1 = d.read(config.the['file'])
    data2 = data1.clone(data1,data1.rows) 
    (lib.stats(data1, 2))
    (lib.stats(data2, 2))


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
    d = DATA()
    data = d.read(config.the['file'])
  
    for _,row in enumerate(data.rows):
        lib.add(num, d.dist(data, row, data.rows[0]))
    print({"lo": num.lo, "hi": num.hi, "mid": lib.rnd(lib.mid(num)), "div": lib.rnd(lib.div(num))})

def test_half():
    d = DATA()
    data = d.read(config.the['file'])

    left, right, A, B, c = data.half(data)
    print(len(left), len(right))

    l, r = d.clone(data, left), d.clone(data, right)
    print("l", lib.stats(l))
    print("r", lib.stats(r))
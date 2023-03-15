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

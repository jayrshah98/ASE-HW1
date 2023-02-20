from SYM import SYM
from NUM import NUM
from DATA import DATA
from LIB import LIB
import config
from UPDATE import UPDATE

lib = LIB()
update = UPDATE()
# sym = SYM()
# num = NUM()
rint = lib.rint
seed_set = lib.seed_set
add = update.add

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
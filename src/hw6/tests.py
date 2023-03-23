import config
from LIB import LIB
from NUM import NUM
from SYM import SYM
from DATA import DATA
from UPDATE import UPDATE
lib = LIB()
num = NUM()
update = UPDATE()
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
        update.add(num1, rand())
    for i in range(10000):
        update.add(num2, rand()**2)
    print(1, rnd(mid(num1),2),round(lib.div(num1), 2))
    print(2, rnd(mid(num2),2),round(lib.div(num2), 2))
    return 0.5 == rnd(mid(num1),1) and mid(num1) > mid(num2)


def sym_test():
   
    sym = update.adds(SYM(), ["a","a","a","a","b","b","c"])
    print (lib.mid(sym), lib.rnd(lib.div(sym)), 2)
    return 1.38 == lib.rnd(lib.div(sym), 2)

def some_test():
    config.the["Max"] = 32
    num1 = NUM()
    for i in range(1,10000+1):
        update.add(num1,i)
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
    num = data.cols.x[1].col
    print(num.lo, num.hi, lib.mid(num), lib.div(num))
    print(lib.stats(data)) 

def clone_test():
    data1 = DATA(config.the['file'])
    data2 = data1.clone(data1,data1.rows) 
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
    for _,row in enumerate(data.rows):
        update.add(num, data.dist(data, row, data.rows[0]))
    print({"lo": num.lo, "hi": num.hi, "mid": lib.rnd(lib.mid(num)), "div": lib.rnd(lib.div(num))})

def half_test():
    data = DATA(config.the['file'])

    left, right, A, B, c,evals = data.half(data)
    print(len(left), len(right))

    l, r = data.clone(data, left), data.clone(data, right)
    print("l", lib.stats(l))
    print("r", lib.stats(r))

def tree_test():
    data = DATA(config.the['file'])
    data.showTree(data.tree(data),"mid",data.cols.y,1)
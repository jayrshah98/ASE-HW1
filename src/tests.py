from SYM import SYM
from NUM import NUM
from lib import LIB
from main import main
# from lib import seed
# from lib import rand
lib = LIB()
sym = SYM()
num = NUM()

rnd = lib.rnd
rand = lib.rand

egs = {}
def eg(key,str,func):
    egs[key] = func
    main.help = main.help + "  -g  %s\t%s\n" + key + str

def eg_sym():
    pairs = ["a","a","a","a","b","b","c"]
    for x in pairs: 
        sym.add(x)
    res = "a" == sym.mid() and 1.379 == rnd(sym.div())
    print("✅ pass:	sym" if res == True else "X fail:	sym")
    return res

def eg_num():
    pairs = [1,1,1,1,2,2,3]
    for x in pairs:
        num.add(x) 
    res = 11/7 == num.mid() and 0.787 == rnd(num.div())
    print("✅ pass:	num" if res == True else "X fail:	num")
    return res

def eg_rand():
    num1 = NUM()
    num2 = NUM()
    for i in range(1000):
        num1.add(rand(0,1))
    for i in range(1000):
        num2.add(rand(0,1))
    m1 = rnd(num1.mid(),10)
    m2 = rnd(num2.mid(),10)
    #print("m1",m1)
    #print("m2",m2)
    #print("rnd val",rnd(m1,1))
    res = m1==m2 and 0.5==rnd(m1,1)
    print("✅ pass:	rand" if res == True else "X fail:	rand")
    return res

eg_sym()
eg_num()
eg_rand()
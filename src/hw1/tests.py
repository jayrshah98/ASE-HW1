from SYM import SYM
from NUM import NUM
from lib import LIB
import config 

lib = LIB()
sym = SYM()
num = NUM()

rnd = lib.rnd
rand = lib.rand



def sym_test():
    pairs = ["a","a","a","a","b","b","c"]
    for x in pairs: 
        sym.add(x)
    res = "a" == sym.mid() and 1.379 == rnd(sym.div())
   # print("✅ pass:	sym" if res == True else "❌ fail:	sym")
    return res

def num_test():
    pairs = [1,1,1,1,2,2,3]
    for x in pairs:
        num.add(x) 
    res = 11/7 == num.mid() and 0.787 == rnd(num.div())
    #print("✅ pass:	num" if res == True else "❌ fail:	num")
    return res

def rand_test():
    num1 = NUM()
    num2 = NUM()
    for _ in range(1000):
        num1.add(rand(0,1))
    for _ in range(1000):
        num2.add(rand(0,1))
    m1 = rnd(num1.mid(),10)
    m2 = rnd(num2.mid(),10)
    print("m1",m1)
    print("m2",m2)
    print("rnd val",rnd(m1,1))
    res = abs(m1-m2)<0.1 and 0.5==rnd(m1,1)
   # print("✅ pass:	rand" if res == True else "❌ fail:	rand")
    return res

def the_test():
    print(str(config.the))
    


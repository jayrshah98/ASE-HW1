from SYM import SYM
from NUM import NUM
from DATA import DATA
from LIB import LIB
from main import main

lib = LIB()
sym = SYM()
num = NUM()
data = DATA(main.the["file"])

rnd = lib.rnd
rand = lib.rand
csv = lib.csv
o = lib.o

def eg_sym():
    pairs = ["a","a","a","a","b","b","c"]
    for x in pairs: 
        sym.add(x)
    res = "a" == sym.mid() and 1.379 == rnd(sym.div())
    print("✅ pass:	sym" if res == True else "❌ fail:	sym")
    return res

def eg_num():
    pairs = [1,1,1,1,2,2,3]
    for x in pairs:
        num.add(x) 
    res = 11/7 == num.mid() and 0.787 == rnd(num.div())
    print("✅ pass:	num" if res == True else "❌ fail:	num")
    return res

def eg_the():
    print(str(main.the))

eg_num()
eg_sym()
eg_the()
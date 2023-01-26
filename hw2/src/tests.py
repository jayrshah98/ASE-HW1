from SYM import SYM
from NUM import NUM
from lib import LIB
from main import main

lib = LIB()
sym = SYM()
num = NUM()

rnd = lib.rnd
rand = lib.rand
csv = lib.csv

def eg_sym():
    pairs = ["a","a","a","a","b","b","c"]
    for x in pairs: 
        sym.add(x)
    res = "a" == sym.mid() and 1.379 == rnd(sym.div())
    print("✅ pass:	sym" if res == True else "❌ fail:	sym")
    return res

# def eg_num():
#     pairs = [1,1,1,1,2,2,3]
#     for x in pairs:
#         num.add(x) 
#     res = 11/7 == num.mid() and 0.787 == rnd(num.div())
#     print("✅ pass:	num" if res == True else "❌ fail:	num")
#     return res

def eg_the():
    print(str(main.the))

def eg_csv():
    global n
    n = 0
    def fu(t):
        global n
        n += len(t)
    csv(main.the["file"],fu)
    res = 8*399 == n
    print("✅ pass:	csv" if res == True else "❌ fail:	csv")
    return res



eg_sym()
#eg_num()
eg_the()
eg_csv()

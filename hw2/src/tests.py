from SYM import SYM
# from NUM import NUM
from lib import LIB

lib = LIB()
sym = SYM()
# num = NUM()

rnd = lib.rnd
rand = lib.rand

def eg_sym():
    pairs = ["a","a","a","a","b","b","c"]
    for x in pairs: 
        sym.add(x)
    res = "a" == sym.mid() and 1.379 == rnd(sym.div())
    print("✅ pass:	sym" if res == True else "❌ fail:	sym")
    return res

eg_sym()

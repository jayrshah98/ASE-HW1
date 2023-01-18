from SYM import SYM
from NUM import NUM
from lib import rnd

def eg_sym():
    sym = SYM()
    pairs = ["a","a","a","a","b","b","c"]
    for x in pairs: 
        sym.add(x)
    return "a" ==sym.mid() and 1.379 == rnd(sym.div())

def eg_num():
    num = NUM()
    pairs = [1,1,1,1,2,2,3]
    for x in pairs:
        num.add(x) 
    return 11/7 == num.mid() and 0.787 == rnd(num.div())


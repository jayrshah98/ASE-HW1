from SYM import SYM
from NUM import NUM
from lib import rnd
from main import main
from lib import seed
from lib import rand
egs = {}
def eg(key,str,func):
    egs[key] = func
    main.help = main.help + "  -g  %s\t%s\n" + key + str

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

def eg_rand():
    num1 = NUM()
    num2 = NUM()
    for i in range(1000):
        num1.add(rand(0,1))
    for i in range(1000):
        num2.add(rand(0,1))
    m1 = rnd(num1.mid(),10)
    m2 = rnd(num2.mid(),10)
    return m1==m2 and 0.5==rnd(m1,1)



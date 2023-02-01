from SYM import SYM
from NUM import NUM
from DATA import DATA
from lib import LIB
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

def eg_data(): 
  print ( "✅ pass:	data" if len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[0].at == 0 and len(data.cols.x) == 4 else "❌ fail:	data"  )

def eg_stats():
  pairs = { 'y': data.cols.y, 'x' : data.cols.x }
  for k,cols in pairs:
    print(k + "mid" + o(data.stats(2, "mid",cols)))
    print("" + "div" + o(data.stats(2, "div",cols)))

eg_num()
eg_the()
eg_csv()
eg_data()
# eg_stats()
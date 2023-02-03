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

def eg_data():
    #data = DATA(main.the["file"])
    res = len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[0].at == 0 and len(data.cols.x) == 4
    print("✅ pass:	data" if res == True else "❌ fail:	data")
    return res

def eg_clone():
    
    data2 = data.clone(data.rows)
     
    res = len(data.rows) == len(data2.rows) and data.cols.y[1].w == data2.cols.y[1].w and data.cols.x[1].at == data2.cols.x[1].at and len(data.cols.x) == len(data2.cols.x)
    print("✅ pass:	clone" if res == True else "❌ fail:	clone")
    return res
    

def eg_around():
    print(0,0,data.rows[0].cells)
    for n,t in enumerate(data.around(data.rows[0])):
        if (n+1) %50 ==0:
           print(n, rnd(t['dist'],2) ,t['row'].cells)
    return True
    

def eg_the():
    print(str(main.the))

eg_num()
eg_sym()
eg_the()
eg_data()
print("✅ pass:	around" if eg_around() == True else "❌ fail:	around")
eg_clone()
# eg_half()
# eg_clone()
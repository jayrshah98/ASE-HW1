from SYM import SYM
from NUM import NUM
from DATA import DATA
from LIB import LIB
import config
from UPDATE import UPDATE

lib = LIB()
update = UPDATE()
# sym = SYM()
# num = NUM()
rint = lib.rint
seed_set = lib.seed_set
add = update.add

def the_test():
    print(str(config.the))


def test_rand():
   
    seed_set(1)
    t = []
    for i in range(1, 1000 + 1):
        t.append(rint(100))
    seed_set(1)
    u = []
    for i in range(1, 1000 + 1):
        u.append(rint(100))

    for k, v in enumerate(t):
        assert v == u[k]

def test_some():
    config.the["Max"] = 32
    num1 = NUM()
    for i in range(1,10000+1):
        add(num1,i)
    print(num1.has())
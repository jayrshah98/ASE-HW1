import config
import random
import LIB as lib
from NUM import NUM



#num = NUM()
samples = lib.samples
gaussian = lib.gaussian
cliffsDelta = lib.cliffsDelta
bootstrap = lib.bootstrap
RX = lib.RX
scottKnot = lib.scottKnot
tiles = lib.tiles

def ok_test():
     print(random.seed(1))

def sample_test():
     for i in range(10):
        print("", "".join(samples(["a", "b", "c", "d", "e"])))

def num_test():
    n = NUM([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(n.n, n.mu, n.sd)

def gauss_test():
    t = []
    for i in range(10 ** 4 + 1):
        t.append(gaussian(10, 2))
    n = NUM(t)
    print(n.n, n.mu, n.sd)


def boot_test():
    a, b = [], []
    for i in range(100):
        a.append(gaussian(10, 1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    mu = 10.0
    while mu <= 11.0:
        b.clear()
        for i in range(100):
            b.append(gaussian(mu, 1))
        cl = cliffsDelta(a, b)
        bs = bootstrap(a, b)
        print("", mu, 1, cl, bs, cl and bs)
        mu += 0.1

def basic_test():
        print("\t\ttruee", bootstrap([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]),
                        cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]))
        print("\t\tfalse", bootstrap([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]),
                        cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]))
        print("\t\tfalse", bootstrap([0.34, 0.49, 0.51, 0.6, 0.34, 0.49, 0.51, 0.6], [0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9]),
                        cliffsDelta([0.34, 0.49, 0.51, 0.6, 0.34, 0.49, 0.51, 0.6], [0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9]))


def pre_test():
    print("\neg3")
    d = 1
    for i in range(10):
        t1, t2 = [], []
        for j in range(32):
            t1.append(gaussian(10, 1))
            t2.append(gaussian(d * 10, 1))
        print("\t", d, "true" if d < 1.1 else "false", bootstrap(t1, t2), bootstrap(t1, t1))
        d += 0.05

def five_test():
    rx_test = [RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"), 
                     RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"), 
                     RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"), 
                     RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"), 
                     RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")]
    sk = scottKnot(rx_test)
    tiles_sk = tiles(sk)
    for rx in tiles_sk:
        print(rx["name"], rx["rank"], rx["show"])

def six_test():
    rx_test = [RX([101,100,99,101,99.5,101,100,99,101,99.5],"rx1"), 
                     RX([101,100,99,101,100,101,100,99,101,100],"rx2"), 
                     RX([101,100,99.5,101,99,101,100,99.5,101,99],"rx3"), 
                     RX([101,100,99,101,100,101,100,99,101,100],"rx4")]
    sk = scottKnot(rx_test)
    tiles_sk = tiles(sk)
    for rx in tiles_sk:
        print(rx["name"], rx["rank"], rx["show"])
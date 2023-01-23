import math
import random

lo = float('inf') 
hi = float('-inf')
seed = 937162211 

class LIB:

    def __init__(self):
        pass

    def rint(self, lo, hi):
        return math.floor(0.5 + random.Random(lo,hi))

    def rand(self,lo =0, hi =1):
        global seed
        seed = (16807 * seed) % 2147483647
        return lo + (hi-lo) * seed / 2147483647

    def rnd(self, n, nPlaces = 3):
        mult = 10**(nPlaces)
        return math.floor(n * mult + 0.5) / mult   
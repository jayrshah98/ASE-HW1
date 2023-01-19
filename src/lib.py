# import module
# NUM = module.NUM()

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

    ### Lists
    def map(self, t, fun, u):
        u = {}
        for k,v in t.items():
            v,k = fun(v)
            if u.get(k) is not None:
                u[k] = v
            else:
                u[len(u)+1] = v


    def kap(self, t, fun,u):
        u={}
        for k,v in t.items():
            v,k = fun(k,v)
            if u.get(k):
                u[k] = v
            else:
                u[len(u)+1] =  v

    
    def sort(self,t,fun):
        sorted(t,fun)
        
    #return sorted list of keys from the the table
    def keys(self, t):
        self.sort(t, lambda x,y : x)
        
    # def keys(t):
    # return sort(kap(t, def(k,_) return k end))


###String

    # def fmt()

    def o(self, t, isKeys, fun):
        if type(t) != dict or type(t) != list:
            return str(t)
        def fun(k, v):
            if not str(k):
                return print(": %s %s", self.o(k), self.o(v))
        
        return 

        # if type(t)~="table" then return tostring(t) end
        # fun= function(k,v) if not tostring(k):find"^_" then return fmt(":%s %s",o(k),o(v)) end end
        # return "{"..table.concat(#t>0 and not isKeys and map(t,o) or sort(kap(t,fun))," ").."}" end

    def oo(self, t):
        print(self.o(t))
        return t 
import random
import re
import config
import math


class NUM: 
    def __init__(self,t= []) -> None:
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        for x in t:
            self.add(x)

    def add(self, x):
        self.n += 1
        d = x - self.mu
        self.mu += d / self.n
        self.m2 += d * (x - self.mu)
        self.sd = 0 if self.n < 2 else math.sqrt(self.m2 / (self.n - 1))
import collections

class SYM:
    
    def __init__(self, n = 0, s = ""):
        self.n = 0
        self.at = n
        self.txt = s
        self.mode = None
        self.most = 0
        self.isSym = True
        self.has = collections.defaultdict(int)
        self.mode = None
        self.isSym = True
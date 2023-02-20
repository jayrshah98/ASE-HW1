import collections

class SYM:
    
    def __init__(self, n, s):
        self.at = n if n else 0
        self.txt = s if s else ""
        self.n = 0
        self.mode = None
        self.most = 0
        self.isSym = True
        self.has = collections.defaultdict(int)
        self.mode = None
        self.isSym = True
from SYM import SYM

class RANGE:

    def __init__(self, at, txt, lo, hi) -> None:
       self.at = at
       self.txt = txt
       self.lo = lo
       self.hi = lo if lo else hi or lo
       self.y = SYM()
       
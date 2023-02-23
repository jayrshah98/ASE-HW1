from LIB import LIB
lib = LIB()
class DATA:

    def __init__(self):
        self.rows = []
        self.cols = None

    def read(sfile,data):
        data = DATA()
        lib.csv(sfile, lambda t: lib.row(data,t))

    def clone(self, rows = None):
        data = DATA([self.cols.names])
        for row in rows:
            data.add(row)
        return data

    

class Club(object):
    def __init__(self):
        self.gs = 0
        self.ga = 0
        self.wi = 0
        self.dr = 0
        self.lo = 0

    @property
    def goalDifference(self):
        return self.gs - self.ga

    @property
    def points(self):
        return self.wi * 3 + self.dr

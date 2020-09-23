class Segtreemin:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [0] * (self.size * 2 - 1)
 
    def helper_set(self, i, v, x, lx, rx):
        if rx - lx == 1:
            self.tree[x] = v
            return
        m = lx + rx >> 1
        if i >= m:
            self.helper_set(i, v, 2 * x + 2, m, rx)
        else:
            self.helper_set(i, v, 2 * x + 1, lx, m)
        self.tree[x] = min(self.tree[2 * x + 1], self.tree[2 * x + 2])
 
    def set(self, i: int, v: int):
        self.helper_set(i, v, 0, 0, self.size)
 
    def helper_get(self, l, r, x, lx, rx):
        if lx >= r or rx <= l:
            return 100000000001
        if lx >= l and rx <= r:
            return self.tree[x]
        m = lx + rx >> 1
        s1 = self.helper_get(l, r, 2 * x + 1, lx, m)
        s2 = self.helper_get(l, r, 2 * x + 2, m, rx)
        return min(s1, s2)
 
    def get_min(self, l, r):
        return self.helper_get(l, r, 0, 0, self.size)

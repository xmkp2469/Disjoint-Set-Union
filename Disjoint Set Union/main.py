class Union_find:
    def __init__(self, n):
        self.par: list[int] = [x for x in range(n + 1)]
        self.rank: list[int] = [0] * (n + 1)

    def root(self, x) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])  # 路径压缩
            return self.par[x]

    def union(self, x, y) -> None:
        if self.root(x) == self.root(y):
            return None
        else:
            if self.rank[x] >= self.rank[y]:
                self.par[self.root(y)] = self.par[self.root(x)]
            else:
                self.par[self.root(x)] = self.par[self.root(y)]


n, q = map(int, input().split())
uf = Union_find(n)
for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        uf.union(u, v)
    else:
        if uf.root(u) == uf.root(v):
            print(1)
        else:
            print(0)

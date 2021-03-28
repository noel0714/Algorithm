import sys
sys.stdin = open("sample_input.txt")


class DisjointSet:
    def __init__(self, N):
        self.N = N
        self.p, self.rank = self.make_set()

    def make_set(self):
        return [i for i in range(self.N+1)], list([0] * (self.N+1))

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])

        return self.p[x]

    def link(self, x, y):
        if self.rank[x] >= self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y

        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))


def kruskal(G, N):
    mst = []

    dis_joint = DisjointSet(N)

    G.sort(key=lambda x:x[2])

    mst_cost = 0

    while len(mst) < N:
        u, v, val = G.pop(0)

        if dis_joint.find_set(u) != dis_joint.find_set(v):
            dis_joint.union(u, v)
            mst.append((u, v))
            mst_cost += val

    return mst_cost


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    G = []
    for _ in range(E):
        G.append(list(map(int, input().split())))

    print(f"#{t} {kruskal(G, V)}")
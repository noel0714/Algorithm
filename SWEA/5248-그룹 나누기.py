import sys
sys.stdin = open("sample_input.txt")


class Group:
    def __init__(self, N):
        self.p = [i for i in range(N + 1)]

    def find_set(self, x):
        if x != self.p[x]:
            return self.find_set(self.p[x])

        return x

    def union(self, x, y):
        self.p[self.find_set(y)] = self.find_set(x)

    def count_head(self, N):
        ret = []
        for i in range(N):
            ret.append(self.find_set(i))

        return len(set(ret)) - 1


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    group = Group(N)

    for i in range(0, M):
        group.union(arr[i * 2], arr[i * 2 + 1])

    print(f"#{t} {group.count_head(N)}")
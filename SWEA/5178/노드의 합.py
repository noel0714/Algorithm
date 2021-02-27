import sys
sys.stdin = open("input.txt")


import math


class Tree:
    def __init__(self, M, N):
        self.tree = [0] * (M + 1)
        self.N = N

        for _ in range(N):
            i, v = map(int, input().split())
            self.tree[i] = v

    def calculate(self, index):
        while index != 1:
            parent_index = math.floor(index / 2)
            self.tree[parent_index] += self.tree[index]
            index -= 1

    def getValue(self, L):
        return self.tree[L]


T = int(input())
for t in range(1, T + 1):
    M, N, L = map(int, input().split())

    tree = Tree(M, N)
    tree.calculate(M)

    print(f"#{t} {tree.getValue(L)}")
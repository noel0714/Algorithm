import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self, num=""):
        self.next = None
        self.num = num


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    start = Node()
    cur = start
    for num in arr:
        cur.next = Node(num)
        cur = cur.next

    for _ in range(M):
        I, V = map(int, input().split())

        cur = start
        for i in range(I):
            cur = cur.next

        tmp = Node(V)
        tmp.next = cur.next
        cur.next = tmp

    cur = start
    for _ in range(L+1):
        cur = cur.next

    print(f"#{t} {cur.num}")
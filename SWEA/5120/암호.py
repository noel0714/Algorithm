import sys
sys.stdin = open("input.txt", 'r')


class Vertex:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())

    start = Vertex(-1)
    current = start

    L = list(map(int, input().split()))
    for l in L:
        tmp = Vertex(l)

        current.next = tmp
        tmp.prev = current

        current = tmp

    current.next = start.next
    start.next.prev = current

    current = start.next
    for k in range(K):
        for m in range(M):
            current = current.next

        tmp = Vertex(current.prev.value + current.value)
        tmp.prev = current.prev
        tmp.next = current

        current.prev.next = tmp
        current.prev = tmp
        current = tmp


    current = start.next
    total_len = 0
    if N+K < 10:
        total_len = N+K
    else:
        total_len = 10

    print(f"#{t}", end=" ")
    for i in range(total_len):
        current = current.prev
        print(f"{current.value}", end=" ")

    print()
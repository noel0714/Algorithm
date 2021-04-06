import sys
sys.stdin = open("sample_input.txt")


from collections import deque


def min_move_distance(arr, cost):
    Q = deque()
    Q.append(0)

    while True:
        if len(Q) == 0:
            break

        s = Q.popleft()
        for e, w in arr[s]:
            tmp_cost = cost[s] + w

            if cost[e] > tmp_cost:
                cost[e] = tmp_cost
                Q.append(e)


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    arr = list([] for _ in range(N+1))
    cost = [9999999] * (N + 1)

    cost[0] = 0

    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s].append([e, w])

    min_move_distance(arr, cost)

    print(f"#{t} {cost[N]}")
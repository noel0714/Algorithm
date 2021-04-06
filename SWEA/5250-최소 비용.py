import sys
sys.stdin = open("sample_input.txt")


from collections import deque


def min_cost(arr, cost, N):
    Q = deque()
    Q.append((0, 0))

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while True:
        if len(Q) == 0:
            break

        tmp = Q.popleft()
        x = tmp[0]
        y = tmp[1]

        for d in directions:
            i = d[0] + x
            j = d[1] + y

            i_con = i < 0 or i == N
            j_con = j < 0 or j == N
            if i_con or j_con:
                continue

            height = 0
            if arr[x][y] < arr[i][j]:
                height = arr[i][j] - arr[x][y]

            tmp_cost = cost[x][y] + height + 1
            if tmp_cost < cost[i][j]:
                cost[i][j] = tmp_cost

                Q.append((i, j))

    return cost


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    cost = []

    for _ in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp.copy())
        cost.append([9999999] * N)

    cost[0][0] = 0
    cost = min_cost(arr, cost, N)

    print(f"#{t} {cost[N-1][N-1]}")


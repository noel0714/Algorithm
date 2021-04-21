import sys
sys.stdin = open("sample_input.txt")


def put_item(items, memo, N, M):
    for i in range(M + 1):
        memo[i][0] = 0

    for w in range(N + 1):
        memo[0][w] = 0

    for i in range(1, M + 1):
        for w in range(1, N + 1):
            if items[i][0] > w:
                memo[i][w] = memo[i - 1][w]
            else:
                memo[i][w] = max(memo[i - 1][w - items[i][0]] + items[i][1],
                                 memo[i - 1][w])

    return memo[M][N]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    memo = [[-1] * (N + 1) for _ in range(M + 1)]
    items = [[0, 0]]

    for _ in range(M):
        tmp = list(map(int, input().split()))
        items.append(tmp)

    print(f"#{t} {put_item(items, memo, N, M)}")



import sys
sys.stdin = open("sample_input.txt")


def bino(n, k):
    global B

    if k == 0 or k == n:
        return 1

    if B[n][k] != -1:
        return B[n][k]

    B[n][k] = bino(n-1, k) + bino(n-1, k-1)
    return B[n][k]


T = int(input())
for t in range(1, T+1):
    n, a, b = map(int, input().split())

    B = [[-1] * (n+1) for _ in range(n+1)]

    print(f"#{t} {bino(n, a)}")
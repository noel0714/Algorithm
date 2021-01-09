import sys
sys.stdin = open("sample_input.txt", "r")


def find(sum, n):
    global result, N, isVisit, arr

    if n == N:
        result = min(sum, result)
        return

    if sum > result:
        return

    for i in range(N):
        if isVisit[i]:
            continue

        isVisit[i] = True
        sum += arr[n][i]

        if sum < result:
            find(sum, n+1)

        isVisit[i] = False
        sum -= arr[n][i]


isVisit = []
arr = []
N = 0
result = 999999
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    isVisit = [False] * N
    arr = []
    result = 999999

    for i in range(N):
        tmp = input().split()
        arr.append([int(i) for i in tmp])

    find(0, 0)

    print(f"#{test_case} {result}")
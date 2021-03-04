import sys
sys.stdin = open("input.txt")


def calculate(N):
    global arr, arr_score

    for i in range(N):
        for j in range(N):
            arr_score[i+1][j] = min(arr_score[i][j] + arr[i+1][j], arr_score[i+1][j])
            arr_score[i][j + 1] = min(arr_score[i][j] + arr[i][j + 1], arr_score[i][j + 1])

arr = []
arr_score = []
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    arr_score = []

    for n in range(N):
        tmp = list(map(int, input().split()))
        tmp.append(0)

        arr.append(tmp)
        arr_score.append([99999] * (N + 1))
    arr.append([0] * (N + 1))
    arr_score.append([99999] * (N + 1))
    arr_score[0][0] = arr[0][0]

    calculate(N)
    print(f"#{t} {arr_score[N-1][N-1]}")
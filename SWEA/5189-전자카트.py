import sys
sys.stdin = open("input.txt")


def calculate(N):
    global sequence, arr, way_cost

    tmp_cost = 0
    for i in range(N):
        departure = sequence[i]
        destination = sequence[i + 1]
        tmp_cost += arr[departure][destination]

    way_cost = min(way_cost, tmp_cost)


def makeWay(N, k):
    if N == k:
        calculate(N)

        return

    for i in range(k, N):
        sequence[k], sequence[i] = sequence[i], sequence[k]
        makeWay(N, k + 1)
        sequence[k], sequence[i] = sequence[i], sequence[k]

way_cost = 9999999
arr = []
sequence = []
T = int(input())
for t in range(1, T + 1):
    N = int(input())

    arr = []
    sequence = [n for n in range(N)]
    sequence.append(0)
    way_cost = 9999999

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    makeWay(N, 1)

    print(f"#{t} {way_cost}")
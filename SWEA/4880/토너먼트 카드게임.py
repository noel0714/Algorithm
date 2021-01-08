import sys

sys.stdin = open("input.txt", "r")

def rule(i, j):
    flag = (arr[i] == 1 and arr[j] == 2) or \
           (arr[i] == 2 and arr[j] == 3) or \
           (arr[i] == 3 and arr[j] == 1)

    if flag:
        return j
    else:
        return i


def RSP(i, j):
    if i == j:
        return rule(i, j)

    middle = (i + j) // 2
    return rule(RSP(i, middle), RSP(middle+1, j))


arr = []
stack = []
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] * (N+1)
    tmp = map(int, input().split())
    arr[1:] = tmp
    stack = []
    result = RSP(1, N)

    print(f"#{test_case} {result}")
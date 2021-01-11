import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = input().split()

    result = M % N

    print(f"#{test_case} {arr[result]}")
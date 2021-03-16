import sys
sys.stdin = open("sample_input.txt")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    print(f"#{t} {arr[N//2]}")
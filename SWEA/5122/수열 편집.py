import sys

sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(input().split())

    try:
        for m in range(M):
            tmp = list(input().split())
            tmp[1] = int(tmp[1])

            if tmp[0] == 'I':
                arr.insert(int(tmp[1]), tmp[2])
            elif tmp[0] == 'C':
                arr[tmp[1]] = tmp[2]
            else:
                arr[tmp[1]] = -1
                arr.remove(-1)

        print(f"#{t} {arr[L]}")
    except:
        print(f"#{t} -1")

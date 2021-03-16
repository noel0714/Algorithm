import sys
sys.stdin = open("sample_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    N1 = sorted(list(map(int,input().split())))
    M1 = list(map(int, input().split()))

    cnt = 0
    for num in M1:
        start = 0
        end = N-1

        flag = 0
        while start <= end:
            mid = (start + end) // 2

            if num >= N1[mid]:
                if num == N1[mid]:
                    cnt += 1
                    break

                start = mid + 1
                if flag == 1: break
                flag = 1

            elif num < N1[mid]:
                end = mid - 1
                if flag == -1: break
                flag = -1

    print('#%d %d'%(tc, cnt))
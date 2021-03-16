import sys
sys.stdin = open("sample_input.txt")


def mergesort(start, end):
    global count, arr

    n = end - start
    if n == 1:
        return

    mid = n // 2 + start
    mergesort(start, mid)
    mergesort(mid, end)

    if arr[mid - 1] > arr[end - 1]:
        count += 1

    change = []
    index_left = start
    index_right = mid
    while True:
        if index_left == mid:
            change = change + arr[index_right:end]
            break
        elif index_right == end:
            change = change + arr[index_left:mid]
            break

        ele_l = arr[index_left]
        ele_r = arr[index_right]
        if ele_l > ele_r:
            change.append(ele_r)
            index_right += 1
        else:
            change.append(ele_l)
            index_left += 1

    arr[start:end] = change


count = 0
arr = []
N = 0
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0

    mergesort(0, N)

    print(f"#{t} {arr[N//2]} {count}")
import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self, num=-1):
        self.num = num
        self.next = None
        self.prev = None

    def is_next_None(self):
        return self.next == None


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    start = Node()

    for _ in range(M):
        arr = list(map(int, input().split()))
        cur_start = start
        perm = Node(arr[0])

        while True:
            if perm.num >= cur_start.num:
                if cur_start.is_next_None():
                    cur_start.next = perm
                    perm.prev = cur_start

                    for n in range(1, N):
                        tmp = Node(arr[n])

                        perm.next = tmp
                        tmp.prev = perm
                        perm = tmp

                    break
                else:
                    cur_start = cur_start.next
            else:
                # 새로 들어온 애가 더 작으면 앞에 채워 넣어야지
                cur_start.prev.next = perm
                perm.prev = cur_start.prev

                for n in range(1, N):
                    tmp = Node(arr[n])

                    perm.next = tmp
                    tmp.prev = perm
                    perm = tmp

                perm.next = cur_start
                cur_start.prev = perm

                break

    cur_start = start
    for _ in range(N * M):
        cur_start = cur_start.next

    print(f"#{t}", end=' ')
    for i in range(9):
        print(cur_start.num, end=' ')
        cur_start = cur_start.prev

    print(cur_start.num)
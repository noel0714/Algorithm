import sys
sys.stdin = open("input.txt", 'r')


def subtree(index, count=0):
    global input_list

    count = count + 1

    for i in input_list[index]:
        count = subtree(i, count)

    return count


input_list = []
T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))
    input_list = [[] for _ in range(E+2)]

    for i in range(0, E * 2, 2):
        input_list[tmp[i]].append(tmp[i+1])

    print(f"#{t} {subtree(N)}")
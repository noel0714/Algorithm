import sys
sys.stdin = open("sample_input.txt")


def partial_sum(K, integers):
    potential = sum(integers)

    if potential < K:
        return 0
    elif potential == K:
        return 1
    else:
        last_ele = integers[-1]

        if last_ele == K:
            return 1 + partial_sum(K, integers[:-1])
        else:
            if K - last_ele > 0:
                return partial_sum(K - last_ele, integers[:-1]) + partial_sum(K, integers[:-1])
            else:
                return partial_sum(K, integers[:-1])


for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    integers = [i for i in range(1, N + 1)]
    result = partial_sum(K, integers)
    print(f'#{t} {result}')
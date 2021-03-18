import sys
sys.stdin = open("sample_input.txt")


def start():
    global totalBusStop, busStop

    ret = [999999] * (totalBusStop + 1)
    ret[1] = 0

    for i in range(1, totalBusStop):
        for length in range(1, busStop[i] + 1):
            go = i + length
            if go <= totalBusStop:
                ret[go] = min(ret[go], ret[i] + 1)

    return ret


busStop = []
totalBusStop = None

T = int(input())
for t in range(1, T+1):
    busStop = []
    totalBusStop = None

    busStop = list(map(int, input().split()))
    totalBusStop = busStop[0]

    answer = start()

    print(f"#{t} {answer[-1] - 1}")


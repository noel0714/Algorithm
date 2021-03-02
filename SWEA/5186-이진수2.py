import sys
sys.stdin = open("input.txt")


T = int(input())
for t in range(1, T+1):
    N = float(input())

    answer = ""
    divided = 1
    count = 0
    while True:
        if N == 0:
            break

        if count == 13:
            answer = "overflow"
            break

        divided /= 2

        if N >= divided:
            answer += "1"
            N -= divided
        else:
            answer += "0"

        count += 1

    print(f"#{t} {answer}")
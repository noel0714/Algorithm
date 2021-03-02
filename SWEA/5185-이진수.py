import sys
sys.stdin = open("input.txt")


bi = ["0000", "0001", "0010", "0011",
      "0100", "0101", "0110", "0111",
      "1000", "1001", "1010", "1011",
      "1100", "1101", "1110", "1111"]


T = int(input())
for t in range(1, T+1):
    N, S = input().split()
    N = int(N)

    answer = ""
    for s in S:
        answer += bi[int(s, 16)]

    print(f"#{t} {answer}")
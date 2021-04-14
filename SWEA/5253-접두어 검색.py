import sys
sys.stdin = open("sample_input.txt")


def find_head(N_vocab, M_vocab):
    count = 0

    for m in M_vocab:
        for n in N_vocab:
            if n.find(m) == 0:
                count += 1
                break

    return count


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    N_vocab = []
    M_vocab = []

    for _ in range(N):
        N_vocab.append(input())

    for _ in range(M):
        M_vocab.append(input())

    count = find_head(N_vocab, M_vocab)

    print(f"#{t} {count}")
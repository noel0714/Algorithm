import sys
sys.stdin = open("sample_input.txt")


def common_word(fir_vocab, se_vocab):
    count = 0

    for vocab in fir_vocab:
        if vocab in se_vocab:
            count += 1

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

    if N < M:
        count = common_word(N_vocab, M_vocab)
    else:
        count = common_word(M_vocab, N_vocab)

    print(f"#{t} {count}")
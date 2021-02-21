import sys
sys.stdin = open("input.txt", 'r')


class Tree:
    def __init__(self, N):
        self.lst = [0] * (N + 1)
        self.N = N
        self.cnt = 1
        self.numbering(1)

    def numbering(self, num):
        if num <= N:
            self.numbering(num * 2)
            self.lst[num] = self.cnt
            self.cnt += 1
            self.numbering(num * 2 + 1)

    def my_result(self):
        return ' '.join(map(str, (self.lst[1], self.lst[self.N // 2])))


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = Tree(N)
    print('#{} {}'.format(test_case, tree.my_result()))
import sys
sys.stdin = open("sample_input.txt")

# 큐가 엄청 느리니까 deque 써
# class로 만들면 편하긴 한데 느려진다.

from collections import deque


class Calculate:
    def __init__(self):
        self.N, self.M = map(int, input().split())

        self.isVisit = [False] * 1000001
        self.isVisit[self.N] = True

        self.answer = self.calc()

    def calc(self):
        # N -> M
        Q = deque()
        Q.append([self.N, 0])

        while True:
            num, count = Q.popleft()
            count += 1
            oper = [num + 1, num - 1, num * 2, num - 10]

            for value in oper:
                if not self.check(value):
                     continue

                if self.isVisit[value]:
                    continue
                else:
                    if value == self.M:
                        return count

                    self.isVisit[value] = True
                    Q.append([value, count])

    def check(self, value):
        return 0 < value <= 1000000

T = int(input())
for t in range(1, T+1):
    calculate = Calculate()

    print(f"#{t} {calculate.answer}")
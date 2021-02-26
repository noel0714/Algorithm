import sys
sys.stdin = open("input.txt")


import math


class Heap():
    def __init__(self):
        self.elements = [0]
        self.ele_num = 0

    def insert(self, value):
        self.ele_num += 1
        self.elements.append(value)

        self.Heapsort(self.ele_num)

    def Heapsort(self, index):
        if index == 1:
            return

        parent_index = math.floor(index / 2)
        parent = self.elements[parent_index]
        now = self.elements[index]

        if parent > now:
            self.elements[parent_index] = now
            self.elements[index] = parent

            self.Heapsort(parent_index)

    def getAnswer(self):
        index = math.floor(self.ele_num / 2)
        answer = 0

        while index != 0:
            answer += self.elements[index]
            index = math.floor(index / 2)

        return answer



T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_input = list(map(int, input().split()))
    heap = Heap()

    for n in num_input:
        heap.insert(n)

    print(f"#{t} {heap.getAnswer()}")

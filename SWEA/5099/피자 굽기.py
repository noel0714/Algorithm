import sys
sys.stdin = open("input.txt", 'r')
import queue


class pizza:
    def __init__(self, index, cheese):
        self.next = None
        self.previous = None
        self.index = index
        self.cheese = cheese

    def melt(self):
        self.cheese = self.cheese // 2

    def complete(self):
        if self.cheese == 0:
            return True

        return False


def bake():
    first = rear = present = waiting.get()
    count = N

    for _ in range(N-1):
        tmp_pizza = waiting.get()
        rear.next = tmp_pizza
        tmp_pizza.previous = rear
        rear = tmp_pizza

    rear.next = first
    first.previous = rear

    while True:
        present.melt()

        if present.complete():
            if waiting.empty():
                count -= 1

                if count == 1:
                    return present.next.index

                present.previous.next = present.next
                present.next.previous = present.previous
            else:
                tmp_pizza = waiting.get()
                present.index = tmp_pizza.index
                present.cheese = tmp_pizza.cheese

        present = present.next


waiting = queue.Queue()

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    total_cheese = list(map(int, input().split()))

    for i in range(1, M+1):
        waiting.put(pizza(i, total_cheese[i-1]))

    result = bake()
    print(f"#{tc} {result}")
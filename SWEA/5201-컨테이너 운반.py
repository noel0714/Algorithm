import sys
sys.stdin = open("input.txt")


class Sender:
    def __init__(self):
        self.N, self.M = map(int, input().split())

        self.container_weight = list(map(int, input().split()))
        self.truck_volumne = list(map(int, input().split()))

        self.container_weight.sort()
        self.truck_volumne.sort()

        self.max = 0

    def send(self):
        if len(self.container_weight) == 0 or \
           len(self.truck_volumne) == 0:
            return False

        co_we = self.container_weight[-1]
        tr_vo = self.truck_volumne[-1]

        if co_we > tr_vo:
            self.container_weight.pop()

            return True

        self.max += co_we
        self.container_weight.pop()
        self.truck_volumne.pop()

        return True


T = int(input())
for t in range(1 ,T+1):
    sender = Sender()

    while True:
        if not sender.send():
            break

    print(f"#{t} {sender.max}")
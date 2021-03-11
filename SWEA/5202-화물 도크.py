import sys
sys.stdin = open("sample_input.txt")


class Make:
    def __init__(self):
        self.N = int(input())
        self.time_schedule = []
        self.count = 0

        for _ in range(self.N):
            self.time_schedule.append(list(map(int, input().split())))

        self.time_schedule.sort(key=lambda x : (x[1], x[0]))

        self.plan()

    def plan(self):
        while True:
            total_len = len(self.time_schedule)
            elimination_list = []

            if total_len == 0:
                break

            self.count += 1
            last_time = self.time_schedule[0][1]

            for i in range(1, total_len):
                if self.time_schedule[i][0] < last_time:
                    elimination_list.append(i)
                else:
                    break

            for _ in elimination_list:
                del self.time_schedule[1]

            del self.time_schedule[0]


T = int(input())
for t in range(1, T+1):
    make = Make()

    print(f"#{t} {make.count}")
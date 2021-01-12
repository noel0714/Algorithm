import sys
sys.stdin = open("input.txt", "r")
import queue


class block:
    def __init__(self):
        self.number = '1'
        self.weight = 99999

    def change(self, next):
        if self.weight > next:
            self.weight = next
            return True

        return False

    def not_wall(self):
        if self.number == '1':
            return False

        return True


def find_maze():
    global q, maze

    while True:
        if q.empty():
            break

        tmp = q.get()
        x, y = tmp[0], tmp[1]
        weight = maze[x][y].weight

        if maze[x+1][y].not_wall() and maze[x+1][y].change(weight+1):
            q.put((x+1, y))
        if maze[x-1][y].not_wall() and maze[x-1][y].change(weight+1):
            q.put((x-1, y))
        if maze[x][y+1].not_wall() and maze[x][y+1].change(weight+1):
            q.put((x, y+1))
        if maze[x][y-1].not_wall() and maze[x][y-1].change(weight+1):
            q.put((x, y-1))


T = int(input())
q = queue.Queue()
maze = []

for test_case in range(1, T + 1):
    N = int(input())
    maze = []
    x_st, y_st = 0, 0
    x_en, y_en = 0, 0

    for i in range(N+2):
        maze.append([0] * (N+2))

        for j in range(N+2):
            maze[i][j] = block()

    for i in range(1, N+1):
        tmp = input()

        for j in range(N):
            maze[i][j+1].number = tmp[j]

        if '3' in tmp:
            x_st, y_st = i, tmp.index('3') + 1
            maze[x_st][y_st].weight = 0
        elif '2' in tmp:
            x_en, y_en = i, tmp.index('2') + 1

    q.put((x_st, y_st))
    find_maze()

    if maze[x_en][y_en].weight == 99999:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} {maze[x_en][y_en].weight - 1}")
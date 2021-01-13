import sys
sys.stdin = open("input.txt", 'r')
import queue


class Vertex:
    def __init__(self, num):
        self.num = num
        self.edges = []
        self.count = 99999
        self.is_visit = False

    def visit(self):
        if self.is_visit:
            return True

        self.is_visit = True
        return False

    def counting(self):
        self.count += 1


def find(end, start):
    q = queue.Queue()
    vertexes[start].count = 0
    q.put(start)

    while not q.empty():
        now = q.get()

        # if vertexes[now].visit():
        #     continue

        for i in vertexes[now].edges:
            tmp = vertexes[now].count + 1
            if vertexes[i].count > tmp:
                vertexes[i].count = tmp
                q.put(i)

    tmp = vertexes[end].count
    if tmp == 99999:
        return 0
    else:
        return tmp


T = int(input())
vertexes = []
for tc in range(1, T+1):
    V, E = map(int, input().split())
    vertexes = []

    for i in range(0, V+1):
        vertexes.append(Vertex(i))

    for e in range(E):
        v1, v2 = map(int, input().split())

        vertexes[v1].edges.append(v2)
        vertexes[v2].edges.append(v1)

    end, start = map(int, input().split())

    result = find(end, start)
    print(f"#{tc} {result}")
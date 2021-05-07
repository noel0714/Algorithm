class Node:
    def __init__(self, i, v):
        self.i = i
        self.v = v


class DisjointSet:
    def __init__(self, P):
        self.P = P
        self.N = {}

        for p in P:
            self.N[p] = Node(p, 0)

    def check_in(self, x):
        if self.N[x].v == 0:
            self.N[x].v = x
            return x

        if self.N[x].v + 1 in self.P:
            return self.check_in(self.N[x].v + 1)

        self.N[x].v += 1
        return self.N[x].v


def solution(k, room_number):
    dis = DisjointSet(room_number)
    answer = []

    for r in room_number:
        answer.append(dis.check_in(r))

    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))
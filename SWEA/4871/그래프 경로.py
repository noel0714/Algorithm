# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


class Node:
    def __init__(self):
        self.isVisit = False
        self.siblings = []


sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    tree = [Node() for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())

        tree[a].siblings.append(b)

    first, last = map(int, input().split())
    stack = [first]
    answer = -1

    while True:
        if len(stack) == 0:
            answer = 0
            break

        i = stack.pop()

        if tree[i].isVisit:
            continue
        else:
            tree[i].isVisit = True

        if i == last:
            answer = 1
            break

        for s in tree[i].siblings:
            stack.append(s)

    print(f"#{test_case} {answer}")
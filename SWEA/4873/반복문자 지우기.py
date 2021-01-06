import sys


sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()
    s = [c for c in s]
    stack = [s[0]]
    s.remove(s[0])

    for c in s:
        if len(stack) != 0:
            if c == stack[-1]:
                stack.pop()
                continue

        stack.append(c)

    print(f"#{test_case} {len(stack)}")
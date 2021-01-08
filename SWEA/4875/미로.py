T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = []
    isVisit = []
    stack = []
    flag = False

    for i in range(N+2):
        maze.append([1] * (N+2))
        isVisit.append([False] * (N + 2))

    for i in range(1, N+1):
        s = input()
        maze[i][1:N+1] = [int(i) for i in s]

        if 3 in maze[i]:
            stack.append([i, maze[i].index(3)])

    while True:
        if len(stack) == 0:
            break

        tmp = stack.pop()
        x, y = tmp[0], tmp[1]

        if isVisit[x][y]:
            continue

        isVisit[x][y] = True

        if maze[x][y] == 1:
            continue
        elif maze[x][y] == 2:
            flag = True
            break
        else:
            stack.append([x+1, y])
            stack.append([x-1, y])
            stack.append([x, y+1])
            stack.append([x, y-1])

    if flag:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))
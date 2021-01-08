TC = int(input())

for tc in range(1, TC + 1):
    Data = list(input().split())
    N = len(Data)
    stack = []
    flag = 0

    # 마침표는 제외하기 위해 N-1까지 반복
    for i in range(N - 1):

        # 숫자인 경우, stack에 append
        if Data[i].isdigit():
            stack.append(Data[i])

        else:
            try:  # 후위표기 계산
                num2, num1 = int(stack.pop()), int(stack.pop())

                if Data[i] == "+":
                    result = num1 + num2
                elif Data[i] == "-":
                    result = num1 - num2
                elif Data[i] == "/":
                    result = num1 // num2
                elif Data[i] == "*":
                    result = num1 * num2

                stack.append(str(result))

            except:  # 에러 발생 예외 처리 예) 숫자 + 연산자 + 연산자
                flag = 1

    # 예외처리 조건 (X) + Stack의 길이가 1인 경우(계산이 성공적인경우)
    if flag == 0 and len(stack) == 1:
        print(f'#{tc} {stack[0]}')

    # 예외처리 조건 (O) + stack의 길이가 2이상인 경우 ex) 숫자만 입력된 경우
    elif flag == 1 or len(stack) > 1:
        print(f'#{tc} error')

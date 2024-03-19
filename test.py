N = int(input())
S = input()
if N==1: 
    print(S)
    exit()
answer = -float('inf')
def back(operation_list):
    #print(operation_list)
    global answer
    temp = 0
    stack = []
    # 우선 현재까지의 연산 실행
    for i in range(1,N,2):
        if i in operation_list:
            stack.append('('+S[i-1:i+2]+')')
        else:
            if i==1:
                stack.append(S[0])
            if i+2 in operation_list:
                stack.append(S[i])
            else:
                stack.append(S[i:i+2])
    #print(stack)
    temp = eval(''.join(stack))
    answer = max(answer, temp)
    # 두 개 뒤부터 수행 가능
    if operation_list:
        for i in range(operation_list[-1]+4,N,2):
            back(operation_list+[i])
    else:
        for i in range(1,N,2):
            back(operation_list+[i])
        

back([])
print(answer)
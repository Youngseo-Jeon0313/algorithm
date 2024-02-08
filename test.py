# 프로그래머스 올바른 괄호

def solution(s):
    answer = True
    stack = []
    for i in s:
        if i=='(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                answer = False
    if stack:
        answer = False

    return answer
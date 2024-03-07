T = 0
while True:
    T+=1
    answer = 0
    s = input()
    if s[0]=='-': break
    stack = []
    for word in s:
        if word =='{':
            stack.append(word)
        else:
            if stack:
                stack.pop()
            else:
                answer +=1
                stack.append('{')
    if stack:
        answer+=len(stack)//2
    print(str(T)+'. '+str(answer))
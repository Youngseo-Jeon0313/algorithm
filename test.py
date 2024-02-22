N = int(input())
stack = []
answer = 0
for step in range(N):
    L = list(map(int,input().split()))
    if len(L)>1 and L[0]==1:
        #일단 얘 시작해. 그리고 넣어.
        L[2]-=1
        if L[2]==0:
            answer+=L[1]
        else:
            stack.append(L)
    else:
        if stack:
            a = stack.pop()
            a[2]-=1
            if a[2]==0:
                answer+=a[1]
            else:
                stack.append(a)
#print(stack)
print(answer)
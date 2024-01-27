N = int(input())
left = 0; right = 1;
SUM = left+right
answer = 0
while left<=right:
    if SUM>N:
        SUM-=left
        left+=1
    elif SUM<N:
        right+=1
        SUM+=right
    else:
        answer+=1
        right+=1
        SUM+=right
print(answer)
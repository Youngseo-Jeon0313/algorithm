# 14426
# 순차 비교

N, M = map(int,input().split())
S = []
for _ in range(N):
    S.append(input())
L = []
for _ in range(M):
    L.append(input())
S.sort(); L.sort()

#print(S)

#print(L)
answer=0
index = 0
for i in range(len(S)):
    while index<len(L):
        #print('check',i,index)
        if len(L[index])<=len(S[i]):
            #print(S[i][:len(L[index])], L[index])
            if L[index]==S[i][:len(L[index])]:
                answer+=1
        
        #사전 순으로 나보다 앞서면 break
        if L[index]>S[i]:
            break;
        index+=1
print(answer)
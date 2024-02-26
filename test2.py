# 28081
'''
좌표로 접근하면 안됨 10^9임 !
'''

W,H,K = map(int,input().split())
N = int(input()) #가로 방향 커팅 수
List_N = list(map(int,input().split()))
M = int(input())
List_M = list(map(int,input().split()))

List_N=[0]+List_N+[H]
List_M=[0]+List_M+[W]

first = []
second = []
for i in range(N+1):
    first.append(List_N[i+1]-List_N[i])
for i in range(M+1):
    second.append(List_M[i+1]-List_M[i])
first.sort()
second.sort()
answer = 0
pointer = M
for i in first:
    #print('i',i,'pointer',pointer)
    while pointer>=0:
        if i*second[pointer]<=K:
            answer+=pointer+1
            break;
        else:
            pointer-=1

print(answer) 
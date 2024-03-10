'''
결국 같은 패턴이 반복되다가 처음 상태가 나오게 될 것이다!
'''

N = int(input())
P = list(map(int,input().split())) 
S = list(map(int,input().split()))# i번째 원소를 Si번째로
target = [0,1,2]*(N//3)

temp_P = P.copy()
answer = 0
while True:
    if temp_P==target:
        print(answer)
        break;
    answer+=1
    #처리!
    temp_List = temp_P.copy()
    for i in range(N):
        temp_List[S[i]] = temp_P[i]
    temp_P = temp_List.copy()
    
    if temp_P==P:
        print(-1)
        break


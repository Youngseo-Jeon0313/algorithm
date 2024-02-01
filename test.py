# 백준 17179
''' 간격에 들어맞니? 를 측정 '''
N, M, L = map(int,input().split())
List = []
for _ in range(M):
    List.append(int(input()))
List = sorted(List)
List=[0]+List+[L]

for _ in range(N):
    answer = 0
    num = int(input())
    left = 0; right = L;
    while left<=right:
        mid = (left+right)//2
        temp = 0; cut_point = List[0]
        for i in range(M+2):
            if List[i]-cut_point>=mid:
                temp+=1; cut_point = List[i]
        print(left, right, mid, temp)
        if temp > num:
            left = mid + 1
            answer = mid

        else: #수가 더 크거나 같으면 위로위로 !
            right = mid - 1

    print(answer)

'''
2 5 70
10
20
35
55
60
1

답 : 35

'''

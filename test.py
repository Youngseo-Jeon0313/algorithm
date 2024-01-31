# 백준 2110

N, C = map(int,input().split())
List = []
for i in range(N):
    num = int(input())
    List.append(num)
List.sort()
left = 0; right =(List[-1]-List[0])*2

while left <= right:
    mid = (right-left)//2
    temp = 0; pos = List[0]
    #일단 비교치를 위한 기준을 만든다.
    for i in List:
        if i-pos>mid:
            pos = i;
            temp+=1
    if temp<C: #범위를 좁힌다.
        mid = right-1
    else:
        mid = left
        answer = mid

print(answer)
from itertools import combinations as cb

# 16937
H, W = map(int,input().split())
N = int(input())
answer = 0
List = []
for _ in range(N):
    List.append(list(map(int,input().split())))

for i in cb(List,2):
    a=i[0]; b=i[1]
    a_=i[0][::-1]; b_=i[1][::-1]
    sorts = [[a[0]+b[0],max(a[1],b[1])],[max(a[0],b[0]),a[1]+b[1]],
             [a_[0]+b[0],max(a_[1],b[1])],[max(a_[0],b[0]),a_[1]+b[1]],
             [a[0]+b_[0],max(a[1],b_[1])],[max(a[0],b_[0]),a[1]+b_[1]],
             [a_[0]+b_[0],max(a_[1],b_[1])],[max(a_[0],b_[0]),a_[1]+b_[1]]]

    for sort in sorts:
        row,col=sort
        if row<=H and col<=W:
            answer=max(answer, (a[0]*a[1]+b[0]*b[1]))

print(answer)
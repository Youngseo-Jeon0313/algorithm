# 21921

N, X = map(int,input().split())
visitors = list(map(int,input().split()))
prefix_sum = [0 for _ in range(N+1)]
for i in range(N):
    prefix_sum[i+1]=prefix_sum[i]+visitors[i]
ans = 0; count = 0;
#print(prefix_sum)
for i in range(N-X+1):
    temp = prefix_sum[i+X]-prefix_sum[i]
    if ans<temp:
        ans = temp; count = 1
    elif ans==temp:
        count+=1
if ans ==0:
    print("SAD")
else:
    print(ans)      
    print(count)
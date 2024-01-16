#12852

N = int(input())
visited = [False for _ in range(N+1)]
path = [0 for _ in range(N+1)] #index : to, value: from
steps = [float('inf') for _ in range(N+1)]
steps[N]=0

# 덮어씌우기
for i in range(N, 0,-1):
    if   i%2==0 :
        if steps[i//2]>steps[i]+1:
            steps[i // 2] = steps[i] + 1
            path[i//2]=i
    if  i%3==0:
        if steps[i//3]>steps[i]+1:
            steps[i // 3] = steps[i] + 1
            path[i//3]=i
    if i>0 :
        if steps[i-1]>steps[i]+1:
            steps[i-1] = steps[i] + 1
            path[i-1]=i


ans = []
now = 1
while True:
    ans.append(now)
    if now==N:
        break;
    now = path[now]
# print('step', steps)
# print('path',path)
print(steps[1])
print(*ans[::-1])
N, M = map(int,input().split())
trees = list(map(int,input().split()))
# 적어도 M 만큼의 나무
start, end = 1, max(trees)
ans = 0
## 이분 탐색
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in trees:
        if i > mid:
            sum += i - mid
    if sum >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)

'''
5 20
4 42 40 26 47
36
'''
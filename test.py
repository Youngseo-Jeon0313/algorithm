# 세 용액 으로 0에 가장 가까운 용액들 찾기
import sys

n = int(input())
array = list(map(int, input().split()))

array.sort()
ans = float('inf')

for i in range(n - 2):
    start = i + 1
    end = n - 1
    while start < end:
        SUM = array[i] + array[start] + array[end]
        if abs(SUM) < ans:
            ans = abs(SUM)
            result = [array[i], array[start], array[end]]
        if SUM < 0:
            start += 1
        elif SUM > 0:
            end -= 1
        else:
            break

print(*result)
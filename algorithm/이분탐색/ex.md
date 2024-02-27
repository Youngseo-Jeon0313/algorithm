**1300**   
"경계선"을 토대로 코드 실수하지 말자!   
```
while start <= end:
    mid = (start+end) // 2
    num  = 0
    for i in range(1, N+1):
        num += min(mid//i, N)
    if num >=K: #여기 주의 !!!
        ans = mid
        end = mid-1
    else:
        start = mid+1
print(ans)
```

**PG 입국심사**   
심사를 기다리는 사람 수 n, 심사관 times   
n=6, times =[7,10] -> 28분   
비교조건은??   
Σmid//times[i] = 25//7 + 25//10 = 5 < n --> n보다 작으면 오른쪽으로 간다.   
                                            n보다 크면 왼쪽으로 간다.   
until start <= end    
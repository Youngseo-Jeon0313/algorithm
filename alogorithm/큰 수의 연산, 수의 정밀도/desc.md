# 생각
로직은 명확한데 시간 복잡도 계산이 확실하게 되지 않을 때는 while + continue + break 활용


# 에라토스테네스의 체
```
n = 10000000 # 조건에 맞게 큰 수로 지정
primes = []
for i in range(2, n+1):
    if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
```



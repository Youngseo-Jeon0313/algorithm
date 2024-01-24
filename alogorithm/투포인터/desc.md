```python
while start<end:
  	Sum = array[start] + array[end]
  	if Sum > target:
			start += 1
      elif Sum < target:
      	end -= 1
      else:
      	count += 1
          start += 1
          end -= 1
```
### testcase
경계값 되는 경우를 넣어보자 !   
예를 들어 펠린드롬일 경우   
abba ->    
ababa ->   

### 투포인터의 핵심은 ?!
투포인터로 푸는 문제인지를 파악하는 것 !!    
DP 로 착각할 가능성이 크다.   
2 또는 3이라는 숫자에 집중 !!   
3151번
O(N)

### 세 용액 -> 0에 가까운 용액 찾기
```python
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
```
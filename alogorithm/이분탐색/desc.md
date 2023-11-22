### TIP
이분 탐색의 핵심은     
|-----------------ㅇ-----|      
명확히 나누어지는 이 경계값을 찾는 것이다!   
즉 이 경계값을 찾기 위한 **비교조건**을 잘 찾자.!   

### 파이썬 upper bound, lower bound
```python
def lowerbound(array, k): #k 이상 값이 처음 나오는 위치
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

		# 📢 이 부분 주의!
        if array[mid] >= k:
            right = mid
        else:
            left = mid + 1

    return left
```

```python
def upperbound(array, k): # k 초과 값이 처음 나오는 위치
    left = 0
    right = len(array)
    
    while left < right:
        mid = (left + right) // 2
		
        # 📢 이 부분 주의!
        if array[mid] <= k:
            left = mid + 1
        else:
            right = mid

    return left  
```

### 시간복잡도
N = 10만 또는 100만 일 때 유력 !
why? -> O(NlogN) 정렬을 사용해야 하므로!
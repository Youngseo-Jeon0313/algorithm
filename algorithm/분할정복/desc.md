### 최근접 점의 쌍 찾기 
원래 주로 브루트포스를 먼저 생각해보았을 때 -> nC2의 시간복잡도 이후 생각하게 되는 방법이다.   
nC2   
ClosestPair 알고리즘   
preprocesssing 전처리 과정 덕분에 정렬에 NlogN 시간 소요      
이후 분할합병 시간복잡도 logN으로     
총 N(logN)^2 소요     

## 코드 양식
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Combine
    return merge(left_sorted, right_sorted)
    
    
def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    
    return result
```
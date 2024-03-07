### 최근접 점의 쌍 찾기 
원래 주로 브루트포스를 먼저 생각해보았을 때 -> nC2의 시간복잡도 이후 생각하게 되는 방법이다.   
nC2   
ClosestPair 알고리즘   
preprocesssing 전처리 과정 덕분에 정렬에 NlogN 시간 소요      
이후 분할합병 시간복잡도 logN으로     
총 N(logN)^2 소요     

## 코드 양식

### merge sort
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left) #재귀
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right): #차례대로 한 개씩 비교하며 merge 시킨다.
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort([2,14,5,1,4,8,23,6])) #[1, 2, 4, 5, 6, 8, 14, 23]

```
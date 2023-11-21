점의 수 n / 간선의 수 m   
시간복잡도?   
프림 - O(n^2)   
크루스칼 - O(mlogm)   
다익스트라 - O(N^2)    

## 크루스칼
크루스칼의 핵심은 union find
```python
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if b<a:
        parent[a]=b
    else:
        parent[b]=a
```

**호출과 반환 로직 이해**   
재귀적으로 부모 노드를 찾아가고 마지막에 루트 노드 반환   
예를 들어 parent = [0,1,2,3,4,5,6,7,8,9] 였으면   
<과정> find(6) 호출   
- 6의 부모는 4이므로 find(4) 호출 
  - 4의 부모는 3이므로 find(3) 호출
    - 3의 부모는 3이므로 3 반환
  - parent[4]=3으로 update하고 3반환
- parent[3]=3으로 update하고 3반환

<결과> parent= [0,1,2,3,3,3,3,7,8,9]   
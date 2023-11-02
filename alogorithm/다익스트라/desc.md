# 다익스트라 구현 시 주의
### 초기화
초기화 시 갈 수 있는 경로들에 대한 graph 초기화를 전부 해놓는다. !   
```python
distance = [float('inf) for _ in rnage(N+1)]
gratph = [[] for _ in range(N+1)]
distance[start] = 0

heappush(hq, (0,0))
```

### 로직
```python
while hq:
    dist, now = heappop(hq)
    if distance[now] < dist: continue #원천 봉쇄
    for i in graph[now]:
        cost = dist+i[1]
        if cost < distance[i[0]]: 
            distance[i[0]] = cost
            heappush(hq, (cost, i[0]))
```


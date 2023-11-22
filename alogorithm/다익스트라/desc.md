# 다익스트라 구현 시 주의
### 초기화
초기화 시 갈 수 있는 경로들에 대한 graph 초기화를 전부 해놓는다. !   
```python
distance = [float('inf) for _ in range(N+1)]
gratph = [[] for _ in range(N+1)]
distance[start] = 0

heappush(hq, (0,0))
```

### 로직
```python
while hq:
    dist, now = heappop(hq)
    if distance[now] < dist: continue #이미 온 길이다. -> 원천 봉쇄
    for i in graph[now]:
        cost = dist+i[1]
        if cost < distance[i[0]]: 
            distance[i[0]] = cost
            heappush(hq, (cost, i[0]))
```

<<<<<<< Updated upstream
### 주의!!
다익스트라에서 visited 배열 1, 0 으로 나타내는 거 쓰지 말 것 !!
***** distance 배열 !
=======
### 다익스트라 X BFS
다익스트라와 BFS의 가장 큰 차이는
맨 마지막으로 도착하는 게 하나라도 있으면 그걸 정답으로 취급하고 out 할 수 있다는 것에서 강력!

>>>>>>> Stashed changes

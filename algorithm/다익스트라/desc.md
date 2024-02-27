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

### 주의!!
다익스트라에서 visited 배열 1, 0 으로 나타내는 거 쓰지 말 것 !!
***** distance 배열 !

### 다익스트라 X BFS
다익스트라와 BFS의 가장 큰 차이는
맨 마지막으로 도착하는 게 하나라도 있으면 그걸 정답으로 취급하고 out 할 수 있다는 것에서 강력!
- ex. 알고스팟
0인 곳을 우선적으로 도는 것이 좋다. 그러다가 만약 N,M 도착지에 도달하게 되면 그대로 반환하고 끝내도 ok!

### 주목하면 좋은 아이디어
[PG] 함승 택시 요금 다익스트라
a, b 각각 따로 택시를 탔을 때 최저 비용을 계산한 후 합친 cost 와   
s를 제외한 특정 거리까지 합승했을 경우 최소 cost   
[BJ] 9370 미확인 도착지
만약 s→h→g 경로를 선택한다면, dist[g] = g-h거리 + dist[h] 일 것이고 s→g→h 경로를 선택한다면,    dist[h]= g-h거리 + dist[g] 인 점을 이용하여 두 번의 다익스트라만 계산하여 풀 수 있다.
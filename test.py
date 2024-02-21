# 백준 5972

import heapq

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int,input().split())
    adj[a].append([b,cost])
    adj[b].append([a,cost])

dist = [float('inf') for _ in range(N+1)]
def dijkstra(start):
    dist[start]=0
    hq = [[0, start]] #cost, curr_node
    heapq.heapify(hq)
    while hq:
        cost, curr_node = heapq.heappop(hq)
        for next_node, next_cost in adj[curr_node]:
            if dist[next_node]>cost+next_cost:
                dist[next_node]=cost+next_cost
                heapq.heappush(hq, [dist[next_node], next_node])
        #print(hq)
dijkstra(1)
print(dist[N])
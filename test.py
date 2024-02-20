'''
최단거리로 갈 때 g->h를 거쳤는가??
거친 곳을 저장하면서 가는 건 불가능. flag 를 두자. 
여러 미세한 잔실수가 많았다.
1. set은 정렬을 해주는가? print(set([1,2])==set([2,1])) -> True
2. for 문을 계속해서 돌 때 flag를 그냥 막바로 -1로 할당하면 뒤에 for문에 당연히,, 지장이 간다 !
'''

import heapq
INF = int(1e9)

T = int(input())
for _ in range(T):
    answer=[]
    hq = []
    heapq.heapify(hq)
    #교차로, 도로, 목적지 후보 갯수
    n,m,t = map(int,input().split()) 
    #예술가들의 출발지, 개가 지나간 교차로 g,h
    s,g,h=map(int,input().split())
    adj=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d=map(int,input().split())
        adj[a].append([b,d])
        adj[b].append([a,d])
    dest=set()
    for _ in range(t):
        #목적지 후보들
        x=int(input())
        dest.add(x)
    dist=[INF for _ in range(n+1)]
    heapq.heappush(hq, [0,0,s]) #지금까지 든 비용, g-h를 지나간 적이 있는가, 현재 위치, 
    flagList = [0 for _ in range(n+1)]
    while hq:
        #print(hq)
        cost, flag, node =heapq.heappop(hq)
        if dist[node]<=cost: continue
        
        dist[node]=cost
        flagList[node]=flag

        for next, next_dist in adj[node]:
            temp_cost = dist[node]+next_dist
            if dist[next]>=temp_cost:
                if (next, node)==(g,h) or (node, next)==(g,h): 
                    heapq.heappush(hq,[temp_cost,-1,next])
                else:
                    heapq.heappush(hq,[temp_cost,flag,next])
    #print(flagList)
    #print(dist)
    for i in dest:
        if flagList[i]:
            answer.append(i)
    answer=sorted(answer)
    print(*answer)
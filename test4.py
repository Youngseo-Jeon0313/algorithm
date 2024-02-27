import heapq
# 9694 - 다익스트라
T = int(input())
for testcase in range(T):
    N, M = map(int,input().split())
    adj = [[] for _ in range(M)]
    dist = [float('inf') for _ in range(M)]
    dist_info = [0 for _ in range(M)] # from:array[index] to:index
    for _ in range(N): # 관계의 수
        x,y,z = map(int,input().split())
        adj[x].append((y,z))
        adj[y].append((x,z))
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq, [0, 0]) #cost, start
    dist[0]=0
    while hq:
        cost, curr_node = heapq.heappop(hq)
        for next_node, next_cost in adj[curr_node]:
            if dist[next_node]>cost+next_cost:
                dist[next_node]=cost+next_cost
                dist_info[next_node]=curr_node
                heapq.heappush(hq, (dist[next_node], next_node))
    if dist[M-1]==float('inf'): 
        print('Case #{}: {}'.format(testcase+1, -1))
    else:
        to = M-1
        answer = []
        while True:
            answer.append(to)
            if to==0:break
            to=dist_info[to]
        answer_str = ''
        for i in answer:
            answer_str=str(i)+' '+answer_str
        print('Case #{}: {}'.format(testcase+1, answer_str ))
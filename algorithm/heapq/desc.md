### TIP
- heapq에 넣는 것 순위   
heapq.heappush(hq, (우선순위1, 우선순위2, 우선순위3 ..))

- heapq에서 시작점은 동시에 넣고 동시에 돌려도 된다 !!

- hq[0] 을 heappop()할지 continue() 할지 heappop 하기 전에 먼저 생각

- 시간복잡도    
push, pop 모두 O(log N)에 해당한다.
build시, 즉 heapify 시 O(N) 소요
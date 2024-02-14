# [PG] 더 맵게 - 힙
import heapq

def solution(scoville, K):
    # scoville = [1,1]; K=2
    # scoville = [2,2,2,1,1,8,10,12]; K=1000 #-1
    N = len(scoville)
    heapq.heapify(scoville)
    # -1인 경우부터 없애자
    answer = 0
    last_check = 0
    while len(scoville) > 1:
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            heapq.heappush(scoville, min_1)
            break
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_1 + min_2 * 2)
        last_check = min_1 + min_2 * 2
        answer += 1

    if answer == N - 1:
        if last_check >= K:  # 2개인 경우 한 번 더 !!
            return answer
        else:
            return -1
    return answer
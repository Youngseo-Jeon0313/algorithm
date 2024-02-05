# [PJ] 디펜스 게임
#그리디 + heapq
import heapq
def solution(n, k, enemy):
    #n=10; k=8; enemy=[100,7,10,5,9,10,5,7,8,23,6,7,8,9] #result : 10
    answer = 0
    hq = []
    for i in enemy:
        heapq.heappush(hq, i)
        if len(hq)>k: #k개보다 더 많아져서 한 개는 무조건 빼야함
            num = heapq.heappop(hq)
            if n-num>=0:
                n-=num
                answer+=1
            else: break;
        else:
            answer+=1
        #print(hq,i,answer)
    return answer
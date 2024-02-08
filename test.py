# 스택 큐 [PG] 기능 개발
# 예외 케이스 발견 실패로 1번 틀림

from collections import deque

def solution(progresses, speeds):
    # progresses = [95, 90, 99, 99, 80]; speeds = [1, 1, 1, 1, 1]
    List = []
    answer = []
    N = len(progresses)
    for i in range(N):
        List.append((100 - progresses[i]) // speeds[i] + bool((100 - progresses[i]) % speeds[i]))
    # for k in range(N-1):
    #     if List[k]<List[k+1]:
    #         answer.append(k-temp)
    #         temp = k
    # answer.append(N-1-temp)
    # while 문 두 개로 교체
    deq = deque(List)
    while deq:
        standard = deq.popleft()
        temp = 1
        while deq:
            if deq[0] <= standard:
                deq.popleft()
                temp += 1
            else:
                break;
        answer.append(temp)
    return answer


'''
    progresses = [93, 30, 55, 60, 40, 65]
    speeds = [1, 30, 5, 10, 60, 7]

    답 : [2,4]

'''

## 다른 풀이

from collections import deque
import math


def solution(progresses, speeds):
    # progresses = [95, 90, 99, 99, 80]; speeds = [1, 1, 1, 1, 1]
    List = []
    answer = []
    N = len(progresses)
    for i in range(N):
        List.append((100 - progresses[i]) // speeds[i] + bool((100 - progresses[i]) % speeds[i]))


    standard = 0
    for k in range(N):
        if List[standard] < List[k]:
            answer.append(k - standard)
            standard = k
    answer.append(N - standard)

    return answer


'''
    progresses = [93, 30, 55, 60, 40, 65]
    speeds = [1, 30, 5, 10, 60, 7]

    답 : [2,4]
'''
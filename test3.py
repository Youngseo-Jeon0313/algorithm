from copy import copy
from itertools import permutations as cb
from collections import deque
N, K = map(int,input().split())
answer_List = [str(i) for i in range(1, N+1)]
List = list(input().split())
sortedList = List.copy()
for i in sortedList:
    i=int(i)
sortedList = sorted(sortedList)
dict = {}
for i in cb(List,N):
    #print(list(i))
    dict[' '.join(list(i))]=0
deq=deque([])
deq.append([0, List])#step, status

answer = float('inf')

#test
# 1,2까지를 뒤집기
# status = deq.popleft()
# print(status)
# temp_List = status.copy()
# temp_List[1:3]=temp_List[1:3][::-1]
# print(temp_List)

while deq:
    step, status = deq.popleft()
    if status == answer_List:
        answer = min(answer, step)
    dict[' '.join(status)]=1
    #다 뒤집어본다.
    for i in range(N-K+1): #N-K+1 해보기
        temp = status.copy()
        temp[i:i+K]=temp[i:i+K][::-1]
        if dict[(' '.join(temp))]==0:
            deq.append([step+1,temp])
            dict[(' '.join(temp))]=1
    # print(deq)
    # print(dict)


if answer==float('inf'):
    print(-1)
else:
    print(answer)
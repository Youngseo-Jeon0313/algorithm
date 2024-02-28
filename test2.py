# 1141
import sys
input = sys.stdin.readline


N = int(input())
List = []
for i in range(N):
    List.append(input().rstrip())

List = sorted(List, key = lambda x:-len(x))

answerList = []
for i in List:
    flag=True
    for j in answerList:
        if j[:len(i)]==i:
            flag=False
    if flag: answerList.append(i)

print(len(answerList))
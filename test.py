#1614

'''
1 -> 8번째마다
2 -> (6,2) 번째마다
3 -> 4번째마다
4 -> (2,6) 번째마다
5 -> 8번째마다


'''
N = int(input())
M = int(input())
answer = 0 #N이 M번째 출몰하는 위치
answer = N
if N==1:
    for i in range(1,M+1):
        answer+=8
elif N==2:
    for i in range(1,M+1):
        if i%2:
            answer+=6
        else:
            answer+=2
elif N==3:
    for i in range(1,M+1):
        answer+=4
elif N==4:
    for i in range(1,M+1):
        if i%2:
            answer+=2
        else:
            answer+=6
else:
    for i in range(1,M+1):
        answer+=8
print(answer-1)
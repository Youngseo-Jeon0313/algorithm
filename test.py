'''
결국 중요한 건 어떤 게 어떤 행/열로 옮겨지냐는 것
'''
from itertools import permutations as pm
from copy import deepcopy

N,M,K = map(int,input().split())
Board = []
for _ in range(N):
    Board.append(list(map(int,input().split())))

rotateList = []
for _ in range(K):
    r,c,s = map(int,input().split())
    rotateList.append([r-1,c-1,s])


def rotate(board,r,c,s):
    temp_board = deepcopy(board)
    #오른쪽으로 가는 애들
    width = 2*s; start = 0
    for i in range(r-s, r):
        for j in range(c-s+start,c-s+start+width):
            temp_board[i][j+1]=board[i][j]
        width -= 2; start+=1;
    #print('오른쪽',temp_board)
    #왼쪽으로 가는 애들
    width = 2*s; start = 0
    for i in range(r+s,r,-1):
        for j in range(c-s+1+start,c-s+1+start+width): 
            temp_board[i][j-1]=board[i][j]
        width-=2; start+=1
    #print('왼쪽',temp_board)
    #위로 가는 애들
    height = 2*s; start = 0
    for j in range(c-s,c):
        for i in range(r-s+1+start,r-s+1+start+height):
            temp_board[i-1][j]=board[i][j]
        height -=2; start+=1
    #print('위로',temp_board)
    #아래로 가는 애들
    height = 2*s; start = 0
    for j in range(c+s,c,-1):
        for i in range(r-s+start,r-s+start+height):
            temp_board[i+1][j]=board[i][j]
        height-=2; start+=1
    #print('아래로',temp_board)
    return temp_board
answer = float('inf')
for comb in pm(rotateList, len(rotateList)):
    temp_ans = deepcopy(Board)
    #print(comb)
    for i in comb:
        r,c,s = i
        temp_ans = rotate(temp_ans,r,c,s)
    #print(temp_ans)
    for i in temp_ans:
        answer=min(answer, sum(i))
print(answer)